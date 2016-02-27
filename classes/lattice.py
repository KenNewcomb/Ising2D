''' lattice.py: represents a lattice object.'''
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
                print(self.spins[i,j])
