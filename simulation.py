import constants
import math
from container import newContainer
from population import LauncherPopulation

class Simulation:

    def __init__(self, distance, height):
        self.target = [distance, height]
        self._population = None
        self._population_num = 0
        self._costs = None

    def changeTarget(self, distance, height):
        self.target = [distance, height]

    def calculateCost(self, launcher):
        time = self.target[0] / (math.cos(launcher.getAng() * math.pi / 180) * launcher.getVel())
        height_at_x = (math.sin(launcher.getAng() * math.pi / 180) * launcher.getVel()) * time - constants.G/2 * (time ** 2)
        return (self.target[1] - height_at_x)**2 + launcher.getVel()

    def updateCosts(self):
        self._costs = []
        for member in self._population.getMembers():
            self._costs.append(self.calculateCost(member))

    def sortPopulation(self):
        self._population.sortPopulation(self._costs)

    def createParentDistribution(self, parents):
        parentDistribution = []
        totalCost = 0
        for member in parents:
            totalCost += self.calculateCost(member)
        for member in parents:
            percentage = (totalCost - self.calculateCost(member)) / totalCost
            for _ in range(int(percentage * constants.POPSIZE)):
                parentDistribution.append(member)
        return parentDistribution

    def firstGen(self):
        self._population = LauncherPopulation()
        self.updateCosts()
        self.sortPopulation()
        self._population_num += 1

    def naturalSelection(self):
        self._population.select(constants.POPSIZE // 10)
        parents = self._population.getMembers()
        parentDistribution = self.createParentDistribution(parents)
        self._population.newGeneration(parentDistribution)
        self.updateCosts()
        self._population_num += 1

    def run(self):
        self.firstGen()
        fittest = self._population.getFittestMember()
        while self.calculateCost(fittest) > 1:
            self.naturalSelection()
            print(self.calculateCost(fittest))
            print(self._population_num)
