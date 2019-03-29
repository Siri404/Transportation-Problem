from Algorithm import Algorithm
import matplotlib.pyplot as plt

def main():
    algorithm = Algorithm()

    optimalIndividual = algorithm.run()
    print('Result: The detected minimum cost is ' + str(optimalIndividual.getFitness()))
    print("For:" + str(optimalIndividual.getChromosome()))


    mean, standardDeviation = algorithm.statistics(30)
    print("Mean:%3.9f " % mean)
    print("Standard deviation:%3.9f " % standardDeviation)
    bestFitnessList = algorithm.statisticsForPlot()
    plt.plot(bestFitnessList)
    plt.show()

main()
