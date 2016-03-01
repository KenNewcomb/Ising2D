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
                self.spins[i,j] = random.choice([-1,1])

    def genSpins(self, numspins):
        '''Generate a unique list of spins to be flipped.'''
        spinlist = []
        for spin in range(0, numspins):
            i = random.randint(0, self.length-1)
            j = random.randint(0, self.width-1)
            if (i, j) not in spinlist:
                spinlist.append((i, j))
            return spinlist

    def flip(self, spin):
        '''Flip spin (i, j).'''
        self.spins[spin[0],spin[1]] *= -1

    def revert(self, spinlist):
        for spin in spinlist:
            self.spins[spin[0], spin[1]] *= -1

    def getNNSpins(self, i, j):
        '''Gets the nearest neighbor spins to a given spin.'''
        # Top neighbor
        if i == 0:
            top = self.spins[self.length-1, j]
        else:
            top = self.spins[i-1, j]

        # Bottom neighbor
        if i == self.length-1:
            bottom = self.spins[0, j]
        else:
            bottom = self.spins[i+1, j]

        # Left neighbor
        if j == 0:
            left = self.spins[i, self.width-1]
        else:
            left = self.spins[i, j-1]

        # Right neighbor
        if j == self.width-1:
            right = self.spins[i, 0]
        else:
            right = self.spins[i, j+1]

        return(left + right + top + bottom)

    def getSpinEnergy(self, spin):
        return self.spins[spin[0],spin[1]]*self.getNNSpins(spin[0],spin[1])

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
