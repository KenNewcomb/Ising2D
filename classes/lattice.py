''' lattice.py: represents a Lattice object. '''
import numpy as np
import random

class Lattice:
    def __init__(self, length, width, J):
        self.length = length
        self.width  = width
        self.J = J
        self.spins = np.ones((length, width), dtype=np.int)

    def randomize(self):
        '''Randomize each of the spins.'''
        for i in range(0, self.length):
            for j in range(0, self.width):
                self.spins[i,j] = random.randint(0,1)

    def flip(self, numspins):
        '''Flip numspins.'''
        for spin in range(0, numspins):
            i = random.randint(0, self.length-1)
            j = random.randint(0, self.width-1)
            flipvalue = random.randint(0,1)
            self.spins[i,j] = flipvalue

    def getNNSpins(self, i, j):
        '''Gets the nearest neighbor spins to a given spin.'''
        left = -1
        right = -1
        top = -1
        bottom = -1

        if i == 0:
            if j == 0:
                left   = self.spins[i, self.width-1]
                top    = self.spins[self.length-1, j]
            elif j == self.width - 1:
                right  = self.spins[i, 1]
                top    = self.spins[self.length-1, j]
            else:
                top    = self.spins[self.length-1, j]
        elif i == self.length-1:
            if j == 0:
                left   = self.spins[i, self.width-1]
                bottom = self.spins[0, j]
            elif j == self.width - 1:
                right  = self.spins[i, 0]
                bottom = self.spins[0, j]
            else:
                bottom = self.spins[0, j]
        if j == 0:
            left = self.spins[i, self.width-1]
        elif j == self.width-1:
            right = self.spins[i, 0]

        if left == -1:
            left   = self.spins[i, j-1]
        if right == -1:
            right  = self.spins[i, j+1]
        if top == -1:
            top    = self.spins[i-1, j]
        if bottom == -1:
            bottom = self.spins[i+1, j]

        return(left + right + top + bottom)

    def getEnergy(self):
        '''Get the lattice energy.'''
        energy = 0
        # Nearest neighbor sum.
        for i in range(0, self.length):
            for j in range(0, self.width):
                energy += self.spins[i,j]*self.getNNSpins(i, j)
        energy *= 0.5*self.J
        return energy
