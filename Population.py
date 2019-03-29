from Individual import *

class Population:

    def __init__(self, size, length):
        """
        count: the number of individuals in the population
        length: the number of values per individual
        vmin: the minimum possible value
        vmax: the maximum possible value
        """
        self.__size = size
        self.__pop = [Individual(Problem.generateIndividual(length)) for x in range(size)]

    def evaluate(self):
        return self.__pop[-1]

    def selection(self):
        """
        Select a parent for recombination
        :return:
        """
        return self.__pop[randint(0, self.__size - 1)]

    def getPopulation(self):
        return self.__pop
