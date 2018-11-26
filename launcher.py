import random
import math

class EvoLauncher:

    def __init__(self, arg1=random.randint(1,5), arg2=random.randint(1,90)):
        self.velocity = arg1
        self.angle = arg2
        self.cost = -1

    def mutate(self):
        mutation = random.random() - 0.5
        changeVelocity = (random.random() - 0.5) > 0
        if changeVelocity:
            self.velocity += mutation
        else:
            self.angle += mutation

    def mate(self, other):
        child1 = (self.target_y, self.target_x, self.velocity, other.angle)
        child2 = (self.target_y, self.target_x, other.velocity, self.angle)
        child1.mutate()
        child2.mutate()
        return child1, child2
