from random import random, randint
from Problem import Problem

class Individual:
    '''
    A member of the population - an individual

    length: the number of genes (components)
    vmin: the minimum possible value
    vmax: the maximum possible value
    '''
    def __init__(self, chromosome):
        self.__chromosome = chromosome
        self.__size = len(self.__chromosome)
        self.__fitness = self.fitness()

    def getFitness(self):
        return self.__fitness

    def getChromosome(self):
        return self.__chromosome

    def __eq__(self, other):
        return self.getChromosome() == other.getChromosome()

    def __lt__(self, other):
        return self.getFitness() < other.getFitness()

    def mutate(self, pM):
        """
        Performs a mutation on an individual with the probability of pM.
        If the event will take place, at a random position a new value will be
        generated in the interval [vmin, vmax]

        individual:the individual to be mutated
        pM: the probability the mutation to occure
        vmin: the minimum possible value
        vmax: the maximum possible value
        """
        if pM > random():
            i = randint(0, len(self.getChromosome()) - 1)
            j = randint(0, len(self.getChromosome()) - 1)
            while i == j:
                j = randint(0, len(self.getChromosome()) - 1)
            self.__chromosome[i], self.__chromosome[j] = self.__chromosome[j], self.__chromosome[i]
            self.__fitness = self.fitness()

    @staticmethod
    def crossover(parent1, parent2):
        """
        crossover between 2 parents
        """
        size = len(parent1.getChromosome())
        child = [-1] * size
        i = randint(0, size - 1)
        j = randint(0, size - 1)
        if i > j:
            i, j = j, i
        for x in range(i, j+1):
            child[x] = parent1.getChromosome()[x]
        aux = j
        j += 1
        while j < size:
            if aux < size - 1:
                aux += 1
            else:
                aux = 0
            if parent2.getChromosome()[aux] not in child:
                child[j] = parent2.getChromosome()[aux]
                j += 1
        j = 0
        while j < i:
            if aux < size - 1:
                aux += 1
            else:
                aux = 0
            if parent2.getChromosome()[aux] not in child:
                child[j] = parent2.getChromosome()[aux]
                j += 1
        return Individual(chromosome=child)

    def fitness(self):
        """
        Determine the fitness of an individual. Lower is better.(min problem)
        For this problem we have the Rastrigin function

        individual: the individual to evaluate
        """
        S = 0
        for a in range(self.__size):
            for b in range(self.__size):
                S += Problem.w(a, b) * Problem.d(self.__chromosome[a], self.__chromosome[b])
        return S
