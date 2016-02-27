'''ising.py: A Monte Carlo simulation of the 2 dimensional Ising model.'''
import sys
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

# Create spin lattice and randomize spins
lattice = Lattice(length, width)
lattice.randomize()
