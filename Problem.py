from random import randint


class Problem:

    @staticmethod
    def w(a, b):
        return a*b

    @staticmethod
    def d(a, b):
        return abs(a-b)

    @staticmethod
    def generateIndividual(length):
        individual = []
        while len(individual) < length:
            i = randint(0, length-1)
            if i not in individual:
                individual.append(i)
        return individual
