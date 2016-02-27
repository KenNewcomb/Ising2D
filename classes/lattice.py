''' lattice.py: represents a Lattice object. '''
import numpy as np
import random

class Lattice:
    def __init__(self, length, width):
        self.length = length
        self.width  = width
        self.spins = np.ones((length, width), dtype=np.int)

    def randomize(self):
        '''Randomize each of the spins.'''
        for i in range(0, self.length):
            for j in range(0, self.width):
                self.spins[i,j] = random.randint(0,1)

    def getNNSpins(self, i, j):
        '''Gets the nearest neighbor spins to a given spin.'''
        if i == 0:
            if j == 0:
                left   = self.spins[i, width-1]
                right  = self.spins[i, j+1]
                top    = self.spins[length-1, j]
                bottom = self.spins[i+1, j]
            elif j = width - 1
                left   = self.spins[i, j-1]
                right  = self.spins[i, 1]
                top    = self.spins[length-1, j]
                bottom = self.spins[i-1, j]
            else
                left   = 
                right  =
                top    =
                bottom =
        elif i = length-1:
            if j == 0:
                left   =
                right  =
                top    =
                bottom =
            elif j = width - 1
                left   =
                right  =
                top    =
                bottom =
            else:
                left   =
                right  =
                top    =
                bottom =
        else:
            left =
            right =
            top =
            bottom =
        return(sum(left, right, top, bottom))

    def getEnergy(self):
        '''Get the lattice energy.'''
        energy = 0
        # Nearest neighbor sum.
        for i in range(0, self.length):
            for j in range(0, self.width):
                energy += self.spins[i,j]*getNNSpins(i, j)
        energy *= 0.5*J
