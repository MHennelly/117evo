import constants
import random
import time
from launcher import EvoLauncher

class Population:

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
        for _ in range(constants.POPSIZE):
            selection1 = parents[random.randint(0,len(parents)-1)]
            selection2 = parents[random.randint(0,len(parents)-1)]
            while selection2.getVel() is selection1.getVel() and selection2.getAng() is selection1.getAng():
                selection2 = parents[random.randint(0,len(parents)-1)]
            child1, child2, = selection1.mate(selection2)
            newGen.append(child1)
            newGen.append(child2)
        self._members = newGen
