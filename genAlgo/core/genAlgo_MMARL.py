
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
        
        with open(fileName, "w") as f:
            f.write(offspring) 
        
        del offspring; del fileName
        

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

    with open(parent, "r") as f:
        child = te.loada(f.read())

    n = random.randint(1, len(p)-1) # number of mutations to make in an individual
    
    for i in range(n):
        random.shuffle(p) # choose a random parameter
        mutation_site = p.pop() # parameter to be mutated
        param_shift = random.uniform(-0.2, 0.2) # how much to mutate the original value # the learning rate is 0.2

        original_parameter_value = child.getValue(mutation_site)
        mutated_parameter_value = original_parameter_value + original_parameter_value * param_shift
        child.setValue(mutation_site, mutated_parameter_value)
    
    del p; del n; del mutation_site; del param_shift; del original_parameter_value; del mutated_parameter_value;

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
        child.setValue(p, parentA.getValue(p))

    del f; del parentB; del parentA

    return child.getCurrentAntimony()

def calculateFitness(population, groundTruth, minmax=False):
    """
    population = name of directory containing Antimony files
    scores = dictionary of file name and score
    """
    scores = {}
    groundTruthData = evaluate.runExperiment(groundTruth)
    for individual in os.listdir(population):
        with open(population + "/" + individual, "r") as f:
            individualData = evaluate.runExperiment(f.read())
        chiSq = np.sum(np.square(groundTruthData - individualData))
        scores[individual] = chiSq
    if minmax:
        return min(scores.values()), max(scores.values())
    else:
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
    groundTruthData = evaluate.runExperiment(groundTruth)
    
    if folderName: 
        scoreFile = open(folderName + "/scores.list", "w")
        paramFile = open(folderName + "/paramData.list", "w")
    else: 
        scoreFile = open("scores.list", "w")
        paramFile = open("paramData.list", "w")

    for individual in os.listdir(population):
        f = open(population + "/" + individual, "r")
        individualModel = f.read()
        individualData = evaluate.runExperiment(individualModel)
        chiSq = np.sum(np.square(groundTruthData - individualData))
        scoreFile.write(str(chiSq) + "\n")
        for k in parameters:
            paramFile.write(str(te.loada(individualModel).getValue(k)) + '\n')
        f.close()
    paramFile.close()
    scoreFile.close()

def runGeneticAlgorithm(population, groundTruth=models.groundTruth_mod_e, parameters=models.K_LIST,
                        lastGeneration=100, survivorRatio=(2,9), tolerance=1, runID=''):
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
        filename=runID + "/runningOutput.list"
    else: 
        filename="runningOutput.list"

    while not converged and generation < lastGeneration: 
        with open(filename, "a") as f:
            f.write('generation ' + str(generation) + '\n')
            
            # select fittest
            selectFittest(population, groundTruth, survivorRatio[0])
            
            # create offspring
            generateOffspring(survivorRatio[1], population, parameters)

            # check fitness
            min, max = calculateFitness(population, groundTruth, minmax=True) 
            
            f.write('least fit: ' +  str(max) + '\n')
            f.write('most fit: ' +  str(min) + '\n') 
            
            generation += 1

            if max < tolerance:
                f.write("tolerance")
                converged = True
            elif max-min < 0.000001: # cutoff is 1e-6, just like in tellurium
                f.write("convergence")
                converged = True
            f.write(f"converged? {converged}"  + '\n\n')

    
