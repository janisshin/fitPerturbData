# the same things as genAlgo_MMARL, but runExperiment has been changed to runExperiment_omit
# v = Vm1/Km1*(S1 - S2/Keq)/(1 + S1/Km1 + S2/Km2)

from numpy.core.fromnumeric import sort
import tellurium as te
import random
import numpy as np
import os

from core import models
from core import evaluate

# Crossover
def generateOffspring(n, population, parameters):
    """
    creates new models from current model lineup
    Parameters
        n: number of offspring to make
        population: current gene pool
        parameters
    """
    offspring = []
    for i in range(n):
        isMutation = bool(random.getrandbits(1))
        
        if isMutation: # mutation
            offspring = performMutation(population, parameters)
        else:
            offspring = performCrossover(population, parameters)
    
        # write child to file
        j = 0
        while os.path.exists(population + "/antimonyModel_" + str(j) + ".txt"):
            j += 1
        fileName = population + "/antimonyModel_" + str(j) + ".txt"
        f = open(fileName, "w")
        f.write(offspring) 
        del offspring
        f.close()
        

def performMutation(population, parameters):
    """
    performs a mutation on a random number of parameters for each individual in population
    Parameters
        population: folder of current gene pool
    Returns
        Antimony string of child
    
    """
    p = parameters.copy()
    
    # randomly choose an existing file
    parent = population + "/" + random.choice(os.listdir(population))

    f = open(parent, "r")
    child = te.loada(f.read())

    n = random.randint(1, len(p)-1) # number of mutations to make in an individual
    
    for i in range(n):
        random.shuffle(p) # choose a random parameter
        mutation_site = p.pop() # parameter to be mutated
        param_shift = random.uniform(-0.2, 0.2) # how much to mutate the original value # the learning rate is 0.2

        original_parameter_value = child.getValue(mutation_site)
        mutated_parameter_value = original_parameter_value + original_parameter_value * param_shift
        child.setValue(mutation_site, mutated_parameter_value)
    return child.getCurrentAntimony()
    

def performCrossover(population, parameters):
    """
    Parameters
        currentPopulation = Str-list of Antimony strings of roadrunner models
        parameters = Str-list
            the parameters which will be crossed over in the parents to create new offspring
    Returns
        offspring = Str-list of Antimony strings of roadrunner models
            list will be the same length as currentPopulation
    """
    
    # choose the parents
    parentA = population + "/" + random.choice(os.listdir(population))
    parentB = population + "/" + random.choice(os.listdir(population))
    while parentA == parentB:
        parentB = population + "/" + random.choice(os.listdir(population))

    # create crossed child
    f = open(parentA, "r")
    parentA = te.loada(f.read())
    f = open(parentB, "r")
    child = te.loada(f.read())

    for p in parameters[0:3]:
        aa = parentA.getValue(p)
        child.setValue(p, aa)

    del f; del parentB; del parentA

    return child.getCurrentAntimony()

def calculateFitness(population, groundTruth):
    """
    population = name of directory containing Antimony files
    scores = dictionary of file name and score
    """
    scores = {}
    groundTruthData = evaluate.runExperiment_omit(groundTruth)
    for individual in os.listdir(population):
        f = open(population + "/" + individual, "r")
        individualData = evaluate.runExperiment_omit(f.read())
        chiSq = np.sum(np.square(groundTruthData - individualData))
        scores[individual] = chiSq
    return scores #### here might be the memory problem

# Selection 
def selectFittest(population, groundTruth, n):
    """
    Orders models from most fit to least fit. Removes least fit models. 
    Parameters
        population: Str-list of Antimony strings of roadrunner models
        n: int
            number of survivors
        scoreResults: float-list
    """
    # compute fitness of population
    scores = calculateFitness(population, groundTruth)

    sorted_scores = sorted(scores.items(), key=lambda x: x[1])
    
    del scores

    for ii in range(n):
        sorted_scores.pop(0)
    
    for s in sorted_scores:
        os.remove(population + "/" + s[0])

def extractParams(population, parameters, groundTruth, folderName=''):
    groundTruthData = evaluate.runExperiment_omit(groundTruth)
    
    if folderName: 
        scoreFile = open(folderName + "/scores.list", "w")
        paramFile = open(folderName + "/paramData.list", "w")
    else: 
        scoreFile = open("scores.list", "w")
        paramFile = open("paramData.list", "w")

    for individual in os.listdir(population):
        f = open(population + "/" + individual, "r")
        individualModel = f.read()
        individualData = evaluate.runExperiment_omit(individualModel)
        chiSq = np.sum(np.square(groundTruthData - individualData))
        scoreFile.write(str(chiSq) + "\n")
        for k in parameters:
            paramFile.write(str(te.loada(individualModel).getValue(k)) + '\n')
        f.close()
    paramFile.close()
    scoreFile.close()

def runGeneticAlgorithm(population, groundTruth=models.groundTruth_mod_e, parameters=models.K_LIST, lastGeneration=100, survivorRatio=(2,9), tolerance=1, runID=''):
    """
    Run genetic algorithm with a given population until convergence or last generation is reached. 
    Also prints out timestamps for each step
    Parameters
        population = name of Folder containing antimony files of all individuals
        lastGeneration = int
    Returns
        population = Str-list of Antimony strings of roadrunner models
    """
    converged=False
    generation = 1    
    
    if runID:
        f = open(runID + "/runningOutput.list", "a")
    else: 
        f = open("runningOutput.list", "a")

    while not converged and generation < lastGeneration: 
        f.write('generation ' + str(generation) + '\n')
        
        # select fittest
        selectFittest(population, groundTruth, survivorRatio[0])
        
        # create offspring
        offspring = generateOffspring(survivorRatio[1], population, parameters)

        # check fitness
        scores = calculateFitness(population, groundTruth)
        
        f.write('max fitness ' + '\n' + str(max(scores.values())) + '\n')
        f.write('min fitness ' + '\n' + str(min(scores.values())) + '\n') ### PRINT FITNESS LEVEL OF FITTEST INDIVIDUAL
        
        generation += 1

        if max(scores.values()) < tolerance:
            f.write("tolerance")
            converged = True
        elif max(scores.values())-min(scores.values()) < 0.0001:
            f.write("convergence")
            converged = True
        f.write(f"converged? {converged}"  + '\n')
    f.close()

    # print params and scores to files
    extractParams(population, parameters, groundTruth, folderName=runID)
