''' ising.py: a Monte Carlo simulation of the 2 dimensional Ising model. '''
import sys
import random
import math
from classes.lattice import Lattice

def usage():
    print("usage: python3 ising.py length width J temperature steps")
    exit()

# Parse user input
try:
    length = int(sys.argv[1])
    width  = int(sys.argv[2])
    J      = float(sys.argv[3])
    temp   = float(sys.argv[4])
    steps  = int(sys.argv[5])
except:
    usage()

# Create spin lattice, randomize spins, and evaluate initial energy.
lattice = Lattice(length, width, J)
lattice.randomize()
energy = lattice.getEnergy()
numspins = 5

energies = []
for step in range(0, steps):
    # Flip spins
    lattice.flip(numspins)

    # Evaluate new energy
    newenergy = lattice.getEnergy()

    # Check energy difference
    if newenergy <= energy:
        energy = newenergy
        # sample
        energies.append(energy)
    else:
        x = random.random()
        if x <= math.exp(-(newenergy - energy)/(temp)):
            energy = newenergy
            # sample
            energies.append(energy)
        else:
            energies.append(energy)
    sys.stdout.write('\rEnergy: {0}'.format(energy))
    sys.stdout.flush()
