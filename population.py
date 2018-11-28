import constants
import random
import time
from launcher import EvoLauncher

class LauncherPopulation:

    def __init__(self, parents = None):
        self._members = []
        random.seed(time.clock())
        if parents:
            for _ in range(constants.POPSIZE // 2):
                selection1 = random.randint(0,len(parents))
                selection2 = random.randint(0,len(parents))
                child1, child2, = parents[selection1].mate(parents[selection2])
                self._members.append(child1)
                self._members.append(child2)
        else:
            for _ in range(constants.POPSIZE):
                self._members.append(EvoLauncher())

    def sortPopulation(self, sortKey):
        z = zip(self._members, sortKey)
        sortedLists = sorted(z, key = lambda x: x[1])
        sortedPop, _ = zip(*sortedLists)
        self._members = sortedPop

    def select(self, slice):
        newPop = self
        newPop._members = self._members[0:slice]
        return newPop
