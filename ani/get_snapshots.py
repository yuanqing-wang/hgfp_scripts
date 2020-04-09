# =============================================================================
# IMPORTS
# =============================================================================
import rdkit
from rdkit import Chem
import pandas as pd
import dgl
import torch
import os
import h5py
import hgfp
import random
import numpy as np
from simtk.openmm.app import *
from simtk.openmm import *
from simtk.unit import *
from openeye import oechem
from openforcefield.topology import Molecule
from openforcefield.topology import Topology
from openforcefield.typing.engines.smirnoff import ForceField
FF = ForceField('test_forcefields/smirnoff99Frosst.offxml')

from mdtraj.reporters import DCDReporter
def get_ani_mol(coordinates, species, smiles):
    """ Given smiles string and list of elements as reference,
    get the RDKit mol with xyz.

    """

    mol = oechem.OEGraphMol()

    for symbol in species:
        mol.NewAtom(getattr(oechem, 'OEElemNo_' + symbol))

    mol.SetCoords(coordinates.reshape([-1]))
    mol.SetDimension(3)
    oechem.OEDetermineConnectivity(mol)
    oechem.OEFindRingAtomsAndBonds(mol)
    oechem.OEPerceiveBondOrders(mol)

    smiles_can = oechem.OECreateCanSmiString(mol)

    ims = oechem.oemolistream()
    ims.SetFormat(oechem.OEFormat_SMI)
    ims.openstring(smiles)
    mol_ref = next(ims.GetOEMols())
    smiles_ref = oechem.OECreateCanSmiString(mol_ref)

    assert smiles_can == smiles_ref

    g = hgfp.graph.from_oemol(mol, use_fp=True)

    return g, mol



def topology_batched_md(num=-1, batch_size=16, step_size=100, ani_path='.'):
    gs = []

    import dgl
    from dgl import data

    ofs = oechem.oemolostream()

    idx = 0
    for path in os.listdir(ani_path):
        if idx > num and num != -1:
            break
        if path.endswith('.h5'):
            f = h5py.File(path, 'r')
            for d0 in list(f.keys()):
                if idx > num and num != -1:
                    break
                for d1 in list(f[d0].keys()):

                    if idx > num and num != -1:
                        break
                
                    print(idx)
                    
                    try:
                        smiles = ''.join([
                            x.decode('utf-8') for x in f[d0][d1]['smiles'].value.tolist()])
                        coordinates = f[d0][d1]['coordinates'].value
                        energies = f[d0][d1]['energies'].value
                        species = [x.decode('utf-8') for x in f[d0][d1]['species'].value]

                        low_energy_idx = np.argsort(energies)[0]

                        g, mol = get_ani_mol(
                                    coordinates[low_energy_idx],
                                    species,
                                    smiles)

                        ofs.open('ds_md/' + str(idx) + '.sdf')
                        oechem.OEWriteMolecule(ofs, mol)                    
                        
                        # g = hgfp.graph.from_oemol(mol)
                        
                        # g = hgfp.data.mm_energy.u(mol, toolkit='openeye', return_graph=True)

                        mol = Molecule.from_openeye(mol)

                        topology = Topology.from_molecules(mol)

                        mol_sys = FF.create_openmm_system(topology)

                        integrator = LangevinIntegrator(500*kelvin, 1/picosecond, 0.002*picoseconds)

                        simulation = Simulation(topology.to_openmm(), mol_sys, integrator)

                        simulation.context.setPositions(
                            0.1 * g.ndata['xyz'].numpy())

                        simulation.reporters.append(DCDReporter('ds_md/' + str(idx) + '.dcd', 10))
                        
                        simulation.minimizeEnergy()

                        simulation.step(10000)

                        idx += 1

                    except:

                        continue

if __name__ == '__main__':
    topology_batched_md(32)
