"""
Module that contains utility functions for molecule
analysis
"""

import numpy as np
import matplotlib.pyplot as plt

from molecool.measure import calculate_distance
from molecool.atom_data import atomic_weights

def build_bond_list(coordinates, max_bond=1.5, min_bond=0):
    
    # Find the bonds in a molecule (set of coordinates) based on distance criteria.
    bonds = {}
    num_atoms = len(coordinates)

    for atom1 in range(num_atoms):
        for atom2 in range(atom1, num_atoms):
            distance = calculate_distance(coordinates[atom1], coordinates[atom2])
            if distance > min_bond and distance < max_bond:
                bonds[(atom1, atom2)] = distance

    return bonds


def bond_histogram(bond_list, save_location=None, dpi=300, graph_min=0, graph_max=2):
    # Draw a histogram of bond lengths based on a bond_list (output from build_bond_list function)
    
    
    lengths = []
    for atoms, bond_length in bond_list.items():
        lengths.append(bond_length)
    
    bins = np.linspace(graph_min, graph_max)
    
    fig = plt.figure()
    ax = fig.add_subplot(111)
    
    plt.xlabel('Bond Length (angstrom)')
    plt.ylabel('Number of Bonds')
    
    
    ax.hist(lengths, bins=bins)
    
    # Save figure
    if save_location:
        plt.savefig(save_location, dpi=dpi)
    
    return ax


def compute_molecular_mass(symbols):
    """This function computes the molecular mass given its element symbols"""
    
    mass = 0.0
    for atom in symbols:
        mass += atomic_weights[atom]

    return mass