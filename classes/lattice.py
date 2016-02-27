''' lattice.py: represents a Lattice object. '''
import numpy as np
import random
import copy

class Lattice:
    def __init__(self, length, width, J):
        self.length = length
        self.width  = width
        self.J = J
        self.oldspins = np.ones((length, width), dtype=np.int)
        self.spins = np.ones((length, width), dtype=np.int)

    def randomize(self):
        '''Randomize each of the spins.'''
        for i in range(0, self.length):
            for j in range(0, self.width):
                self.spins[i,j] = random.choice([-1,1])

    def flip(self, numspins):
        '''Flip numspins.'''
        self.oldspins = copy.copy(self.spins)
        for spin in range(0, numspins):
            i = random.randint(0, self.length-1)
            j = random.randint(0, self.width-1)
            flipvalue = random.choice([-1,1])
            self.spins[i,j] = flipvalue

    def revert(self):
        self.spins = copy.copy(self.oldspins)

    def getNNSpins(self, i, j):
        '''Gets the nearest neighbor spins to a given spin.'''
        left = 0
        right = 0
        top = 0
        bottom = 0

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

        if left == 0:
            left   = self.spins[i, j-1]
        if right == 0:
            right  = self.spins[i, j+1]
        if top == 0:
            top    = self.spins[i-1, j]
        if bottom == 0:
            bottom = self.spins[i+1, j]

        return(left + right + top + bottom)

    def getEnergy(self):
        '''Get the lattice energy.'''
        energy = 0
        # Nearest neighbor sum.
        for i in range(0, self.length):
            for j in range(0, self.width):
                energy += self.spins[i,j]*self.getNNSpins(i,j)
        energy *= -0.5*self.J
        return energy

    def getAverageSpin(self):
        average_spin = 0
        for i in range(0, self.length):
            for j in range(0, self.width):
                average_spin += self.spins[i,j]
        average_spin /= self.length*self.width
        return average_spin

    def getSpins(self):
        return self.spins
