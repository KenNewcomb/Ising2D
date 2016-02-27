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
#lattice.randomize()
energy = lattice.getEnergy()
numspins = 30

energies = []
for step in range(0, steps):
    # Flip spins
    lattice.flip(numspins)

    # Evaluate new energy
    newenergy = lattice.getEnergy()

    # if Enew <= E, accept
    if newenergy <= energy:
        energy = newenergy
        energies.append(energy)
    # if Enew > E, accept with Boltzmann probability.
    else:
        x = random.random()
        if x <= math.exp(-(newenergy - energy)/(temp)):
            energy = newenergy
            energies.append(energy)
        else:
            energies.append(energy)
    sys.stdout.write('\rStep: {0}/{1}, Energy: {2}'.format(step, steps, energy))
    sys.stdout.flush()
print("\nSimulation complete.")

# Write data
with open('data', 'w') as datafile:
    for step in range(0, steps):
        datafile.write('{0} {1}\n'.format(step, energies[step]))
datafile.close()
print("Data written to ./data.")
