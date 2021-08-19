
import tellurium as te
import random
import numpy as np
from time import time
import models_2


# Crossover - create 5 children
params = ['k1','k11','k2','k22','k3'] #,'k33','k4','k44','k5','k55']
def generateOffspring(currentPopulation, crossOver=params):
    """
    creates new models from current model lineup
    Parameters
        currentPopulation = Str-list of Antimony strings of roadrunner models
        parameters = Str-list
            the parameters which will be crossed over in the parents to create new offspring
    Returns
        offspring = Str-list of Antimony strings of roadrunner models
            list will be the same length as currentPopulation
    """
    random.shuffle(currentPopulation) # shuffle the list
    offspring = []
    for i in range(len(crossOver)):
        indexA = i * 2
        indexB = indexA + 1
        a = te.loada(currentPopulation[indexA])
        b = te.loada(currentPopulation[indexB])
        aValues = a.getGlobalParameterValues()
        bValues = b.getGlobalParameterValues()
        for p in crossOver:
            aa = a.getValue(p)
            bb = b.getValue(p)
            a.setValue(p, bb)
            b.setValue(p, aa)
        offspring.append(a.getAntimony())
        offspring.append(b.getAntimony())
    return offspring


# Selection 
def selectFittest(population, scoreResults, n):
    """
    Orders models from most fit to least fit. Removes least fit models. 
    Parameters
        population: Str-list of Antimony strings of roadrunner models
        n: int
            number of survivors
        scoreResults: float-list
    """
    fitnessOrder = scoreResults.copy()
    fitnessOrder.sort() # sort in order of fittest to least fit
    removeList = []
    for i in range(len(scoreResults)-n):
        # pop the value from fitnessOrder
        value = fitnessOrder.pop(-1)
        # find the value's index in scoreResults
        index = scoreResults.index(value)
        removeList.append(index)
        
    removeList.sort(reverse=True)
    # remove the model from scrambledModels using index
    for i in removeList:
        population.pop(i)


# check convergence
def checkPopulationConvergence(population, tolerance=1):
    """
    Determines whether individuals in population have parameter values that are within tolerance
    
    Parameters
        population: Str-list of Antimony strings of roadrunner models
        tolerance: int
            the size of chisq differences between models in the population
    Returns Bool
    """
    f = population.pop()
    fittest = te.loada(f)
    fittestParamValues = fittest.getGlobalParameterValues()
    for m in population:
        model = te.loada(m)
        # subtract all parameter values from `fittest`
        fitDifference = model.getGlobalParameterValues() - fittestParamValues
        # square and sum all values
        fitChiSq = np.sum(np.square(fitDifference))
        print(f"fitChiSq: {fitChiSq}")
        if fitChiSq > tolerance:
            population.append(f)
            return False # the entire population has not converged
    population.append(f)
    return True


def runGeneticAlgorithm(population, lastGeneration=100, survivorRatio=(7,3), tolerance=100, crossOver=None, toFit=None):
    """
    Run genetic algorithm with a given population until convergence or last generation is reached. 
    Also prints out timestamps for each step
    Parameters
        population = Str-list of Antimony strings of roadrunner models
        lastGeneration = int
    Returns
        population = Str-list of Antimony strings of roadrunner models
    """
    converged=False
    generation = 1
    print("simulating generation 1")
    while not converged or generation < lastGeneration: 
        t1 = time()

        # generate offspring
        if not crossOver:
            offspring = generateOffspring(population, crossOver=crossOver)
        else: 
            offspring = generateOffspring(population)
        t2 = time()
        print(f"B: {t2-t1}")

        # compute fitness of starting population
        if not toFit: # if toFit is has argument
            paramResults, scoreResults = models_2.fitMultipleModels(population, toFit=toFit)
        else:
            paramResults, scoreResults = models_2.fitMultipleModels(population)
        t3 = time()
        print(f"A: {t3-t2}")

        # compute fitness of offspring
        offspring_paramResults, offspring_scoreResults = models_2.fitMultipleModels(offspring) 
        t4 = time()
        print(f"C: {t4-t3}")
        
        # select fittest parents and offspring
        selectFittest(population, scoreResults, survivorRatio[0]) # parents
        selectFittest(offspring, offspring_scoreResults, survivorRatio[1]) # offspring
        
        t5 = time()
        print(f"D: {t5-t4}")
        
        # define surviving population
        population = population + offspring
        t6 = time()
        print(f"E: {t6-t5}")

        generation += 1
        print(f"simulating generation {generation}")

        # check that genes have converged
        converged = checkPopulationConvergence(population, tolerance=tolerance)
        t7 = time()
        print(f"F: {t7-t6}")
        print()
        
    # if genes have converged or if 100 generations have been reached,
    print(f"converged? {converged}")
    return population # this may be unneccesary in an interactive script because population is a list...but may be necessary if you are submitting jobs. 
