import math
from launcher import EvoLauncher

class LauncherPopulation:

    launchers = []

    def __init__(vel, ang):
        for i in range(100):
            launchers.append(EvoLauncher(vel, ang))
            launchers[i].mutate()
            launchers[i].calculateCost()

    def calculateCost(self):
        g = 9.8
        radians = math.radians(self.angle)
        time = self.target_x / (math.cos(radians)*self.velocity)
        heightAtX = ((math.sin(radians)*self.velocity)*time) - (g*(time**2))
        self.cost = (self.target_y - heightAtX) ** 2

    def selectFittest(self):
        for launcher in self.launchers:
            launcher.calculateCost()
        sorted(self.launchers, key = lambda launcher: launcher.cost)

    def mateVelocity(self, launcher1, launcher2):
        child1 = launcher1
        child1.swapVelocity(launcher2)
        child2 = launcher2
        child2.swapVelocity(launcher1)
        return child1, child2

    def mateAngle(self, launcher1, launcher2):
        child1 = launcher1
        child1.swapAngle(launcher2)
        child2 = launcher2
        child2.swapVelocity(launcher1)
        return child1, child2
