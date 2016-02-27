''' ising.py: a Monte Carlo simulation of the 2 dimensional Ising model. '''
import sys
import random
import Math
from classes.lattice import Lattice

def usage():
    print("usage: python3 ising.py length width temperature steps")
    exit()

# Parse user input
try:
    length = int(sys.argv[1])
    width  = int(sys.argv[2])
    temp   = float(sys.argv[3])
    steps  = float(sys.argv[4])
except:
    usage()

# Create spin lattice, randomize spins, and evaluate initial energy.
lattice = Lattice(length, width)
lattice.randomize()
energy = lattice.getEnergy()

for step in range(0, steps):
    # Flip spins
    lattice.flip(numspins)

    # Evaluate new energy
    newenergy = lattice.getEnergy()

    # Check energy difference
    if newenergy <= energy:
        energy = newenergy
        # sample
        pass
    else:
        x = random.random()
        if x <= Math.exp(-(newenergy - energy)/(Kb*temp))
            energy = newenergy
            # sample
            pass
        else:
            # sample
