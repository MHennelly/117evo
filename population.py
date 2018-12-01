import constants
import random
import time
from launcher import EvoLauncher

class LauncherPopulation:

    def __init__(self):
        self._members = []
        random.seed(time.clock())
        for _ in range(constants.POPSIZE):
            self._members.append(EvoLauncher())

    def sortPopulation(self, sortKey):
        z = zip(self._members, sortKey)
        sortedLists = sorted(z, key = lambda x: x[1])
        sortedPop, _ = zip(*sortedLists)
        self._members = sortedPop

    def select(self, slice):
        self._members = self._members[0:slice]

    def getMembers(self):
        return self._members

    def getFittestMember(self):
        return self._members[0]

    def newGeneration(self, parents):
        newGen = []
        for _ in range(constants.POPSIZE * 3 // 8):
            selection1 = random.randint(0,len(parents)-1)
            selection2 = random.randint(0,len(parents)-1)
            while selection2 == selection1:
                selection2 = random.randint(0,len(parents)-1)
            child1, child2, = parents[selection1].mate(parents[selection2])
            #print(child1.getVel(), child1.getAng())
            newGen.append(child1)
            newGen.append(child2)
        for _ in range(constants.POPSIZE // 4):
            newGen.append(EvoLauncher())
        self._members = newGen
