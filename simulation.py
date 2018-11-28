import constants
import math
from container import newContainer
from population import LauncherPopulation

class Simulation:

    def __init__(self, distance_x):
        self._distance_x = distance_x
        self._population = None
        self._generation_num = 0

    def changeTarget(self, target):
        self._distance_x = target

    def calculateCost(self, launcher):
        time = self._distance_x / (math.cos(launcher.getAng()) * launcher.getVel())
        height_at_x = (math.sin(launcher.getAng()) * launcher.getVel()) * time - constants.G * (time ** 2)
        return height_at_x ** 2

    def firstGen(self):
        nextGen = LauncherPopulation()
        costKey = []
        for member in nextGen._members:
            cost = self.calculateCost(member)
            costKey.append(cost)
        nextGen.sortPopulation(costKey)
        self._generation = nextGen
        self._generation_num += 1

    def naturalSelection(self):
        selection = self._generation.select(constants.POPSIZE // 10)
        parentDistribution = []
        totalCost = 0
        for member in selection:
            totalCost += self.calculateCost(member)
        for member in selection:
            percentage = (totalCost - self.calculateCost(member)) / totalCost
            for _ in range(int(percentage * constants.POPSIZE)):
                parentDistribution.append(member)
        nextGen = LauncherPopulation(parentDistribution)
        for member in nextGen._members:
            cost = self.calculateCost(member._launcher)
            member._cost = cost
        self._generation = nextGen
        self._generation_num += 1

    def run(self):
        self.newGeneration()
        while self._generation[0]._cost > 25:
            self.newGeneration()
            print(self._generation[0]._cost)
            print(self._generation_num)
