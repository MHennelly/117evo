import constants
import math
from population import Population

class Simulation:

    def __init__(self, distance, height):
        self._target = [distance, height]
        self._population = None
        self._generation = 0
        self._costs = None

    def changeTarget(self, distance, height):
        self._target = [distance, height]

    def getHeight(self, launcher):
        time = self._target[0] / (math.cos(launcher.getAng() * math.pi / 180) * launcher.getVel())
        height_at_x = (math.sin(launcher.getAng() * math.pi / 180) * launcher.getVel()) * time - constants.G/2 * (time ** 2)
        return height_at_x

    def calculateCost(self, launcher):
        height = self.getHeight(launcher)
        return (math.fabs(self._target[1] - height) + 1)**2

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
        self._population = Population()
        self.updateCosts()
        self.sortPopulation()
        self._generation += 1

    def naturalSelection(self):
        self._population.select(constants.SELECTSIZE)
        parents = self._population.getMembers()
        parentDistribution = self.createParentDistribution(parents)
        self._population.newGeneration(parentDistribution)
        self.updateCosts()
        self._generation += 1

    def getValues(self):
        fittest = self._population.getFittestMember()
        return fittest.getVel(), fittest.getAng()

    def run(self):
        self.firstGen()
        fittest = self._population.getFittestMember()
        while self.calculateCost(fittest) > 2:
            self.naturalSelection()
            print(self.getHeight(fittest))
