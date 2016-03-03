''' ising.py: a Monte Carlo simulation of the 2 dimensional Ising model. '''
import sys
import random
import math
from classes.lattice import Lattice
import statistics

def usage():
    print("usage: python3 ising.py length width J temperature steps numflips")
    exit()

# Parse user input
try:
    length   = int(sys.argv[1]) # lattice length
    width    = int(sys.argv[2]) # lattice width
    J        = float(sys.argv[3]) # Magnetic coupling
    temp     = float(sys.argv[4]) # Temperature
    steps    = int(sys.argv[5]) # Number of MC steps
    numflips = int(sys.argv[6]) # Number of spin flips per step.
except:
    usage()

# Create spin lattice, randomize spins, and evaluate initial energy.
lattice = Lattice(length, width, J)
lattice.randomize()
energy = lattice.getEnergy()

energies = []
average_spins = []
print("Simulating {0}x{1} Ising lattice for J = {2}, T = {3}.".format(length, width, J, temp))
for step in range(0, steps):
    # Generate random spins to flip
    spinlist = lattice.genSpins(numflips)

    # Sum of delta E's due to flipping each spin.
    deltaE = 0
    for spin in spinlist:
        spinenergy = lattice.getSpinEnergy(spin)
        lattice.flip(spin)
        newspinenergy = lattice.getSpinEnergy(spin)
        deltaE += newspinenergy - spinenergy
    deltaE *= -J

    # if Enew <= E, accept
    if deltaE < 0:
        energy += deltaE
    # if Enew > E, accept with Boltzmann probability.
    else:
        x = random.random()
        boltzmann = math.exp(-deltaE/(temp))
        if x <= boltzmann:
            energy += deltaE
        else:
            lattice.revert(spinlist)

    # Calculate energy and average spin
    energies.append(energy)
    average_spins.append(lattice.getAverageSpin())

    sys.stdout.write('\rStep: {0}/{1}, Energy: {2}.'.format(step, steps, energy))
    sys.stdout.flush()
print("\nSimulation complete.")

print(lattice.getSpins())
# Write data
energyfile  = open('energy', 'w')
spinfile    = open('spin', 'w')
magnetfile  = open('magnetization', 'w')
magsucfile  = open('mag_suscept', 'w')
for step in range(0, steps):
    energyfile.write('{0} {1}\n'.format(step, energies[step]))
    spinfile.write('{0} {1}\n   '.format(step, average_spins[step]))
# Average the average spin over last 10 frames
ave_mag    = statistics.mean(average_spins[-50000:])
ave_mag_sq = statistics.mean([i ** 2 for i in average_spins[-50000:]])
magsucfile.write('{0}'.format((ave_mag_sq-ave_mag)/temp))
magnetfile.write('{0}'.format(ave_mag))
magnetfile.close()
magsucfile.close()
energyfile.close()
spinfile.close()
print("Data written.")
