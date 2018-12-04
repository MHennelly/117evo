import time
import constants
import random

class EvoLauncher:

    def __init__(self, velocity = None, angle = None):
        self._genes = [0, 0]
        if velocity:
            self._genes[0] = velocity
        else:
            random.seed(time.clock())
            self._genes[0] = random.randint(1,constants.MAXVEL)
        if angle:
            self._genes[1] = angle
        else:
            random.seed(time.clock())
            self._genes[1] = random.randint(1,90)

    def getVel(self):
        return self._genes[0]

    def getAng(self):
        return self._genes[1]

    def mutate(self):
        random.seed(time.clock())
        chngVel = random.random() < constants.MUTATION_RATE
        chngAng = random.random() < constants.MUTATION_RATE
        if chngVel:
            self._genes[0] += random.random() - 0.5
        else:
            self._genes[1] += random.random() - 0.5

    def mate(self, other):
        child1 = EvoLauncher(self.getVel(), other.getAng())
        child2 = EvoLauncher(other.getVel(), self.getAng())
        child1.mutate()
        child2.mutate()
        return child1, child2
