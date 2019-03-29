import numpy

from Individual import Individual
from Population import Population
from Problem import Problem


class Algorithm:
    __populationSize = int
    __mutationProbability = float
    __chromosomeLength = int
    __noGenerations = int

    def __init__(self):
        self.__problem = Problem()
        self.readParameters("param.in")
        self.__population = Population(self.__populationSize, self.__chromosomeLength)

    def readParameters(self, fileName):
        fileHandler = open(fileName, "r")
        fileContent = fileHandler.readlines()
        for line in fileContent:
            line = line.split(":")
            if line[0].strip() == "populationSize":
                self.__populationSize = int(line[1].strip())
            elif line[0].strip() == "chromosomeLength":
                self.__chromosomeLength = int(line[1].strip())
            elif line[0].strip() == "mutationProbability":
                self.__mutationProbability = float(line[1].strip())
            elif line[0].strip() == "noGenerations":
                self.__noGenerations = int(line[1].strip())
            else:
                print("param.in is faulty")

    def iteration(self):
        """
        an iteration
        pop: the current population
        pM: the probability the mutation to occure
        vmin: the minimum possible value
        vmax: the maximum possible value
        """
        i1 = self.__population.selection()
        i2 = self.__population.selection()
        if i1 != i2:
            child = Individual.crossover(i1, i2)
            child.mutate(self.__mutationProbability)
            self.__population.getPopulation().append(child)
            self.__population.getPopulation().sort(reverse=True)
            self.__population.getPopulation().pop(0)

    def run(self):
        for index in range(self.__noGenerations):
            self.iteration()
        return self.__population.evaluate()

    def statRun(self):
        for index in range(1000):
            self.iteration()
        return self.__population.evaluate()

    def statistics(self, numberOfRuns):
        self.resetPopulation()
        bestIndividuals = []
        for index in range(numberOfRuns):
            bestIndividuals.append(self.statRun())
            self.resetPopulation()
        fitnessValues = [individual.getFitness() for individual in bestIndividuals]
        return numpy.mean(fitnessValues), numpy.std(fitnessValues)

    def statisticsForPlot(self):
        self.__population = Population(self.__populationSize, self.__chromosomeLength)

        bestFitnessList = [min(individual.getFitness() for individual in self.__population.getPopulation())]
        for index in range(self.__noGenerations):
            self.iteration()
            bestFitnessList.append(min(individual.getFitness() for individual in self.__population.getPopulation()))

        return bestFitnessList

    def resetPopulation(self):
        self.__population = Population(40, self.__chromosomeLength)
