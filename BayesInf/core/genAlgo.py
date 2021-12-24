from numpy.core.fromnumeric import sort
import tellurium as te
import random
import numpy as np
import os

from core import evaluate

# Crossover
def generateOffspring(n, population, parameters):
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
    p = parameters.copy()
    
    # randomly choose an existing file
    parent = population + "/" + random.choice(os.listdir(population))

    with open(parent, "r") as f:
        child = te.loada(f.read())

    n = random.randint(1, len(p)-1) # number of mutations to make in an individual
    
    for i in range(n):
        random.shuffle(p) # choose a random parameter
        mutation_site = p.pop() # parameter to be mutated
        # how much to mutate the original value
        param_shift = random.uniform(-learnRate, learnRate) 
        original_parameter_value = child.getValue(mutation_site)
        mutated_parameter_value = original_parameter_value + original_parameter_value * param_shift
        child.setValue(mutation_site, mutated_parameter_value)
    
    del p; del n; del mutation_site; del param_shift; del original_parameter_value; 
    del mutated_parameter_value;

    return child.getCurrentAntimony()
    

def performCrossover(population, parameters):
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


def calculateFitness(population, minmax=False):
    scores = {}
    groundTruthData = [-0.039525692,-0.110671937,0.079051383,0.00621118,-0.01242236,-0.105590062] ################
    
    for individual in os.listdir(population):
        with open(population + "/" + individual, "r") as f:
            individualData = evaluate.runExperiment(f.read())
        chiSq = np.sum(np.square(groundTruthData - individualData))
        scores[individual] = chiSq
    if minmax:
        return min(scores.values()), max(scores.values())
    else:
        return scores #### here might be the memory problem


def selectFittest(population, n):
    # compute fitness of population
    scores = calculateFitness(population)

    sorted_scores = sorted(scores.items(), key=lambda x: x[1])
    
    del scores

    for ii in range(n):
        sorted_scores.pop(0)
    
    for s in sorted_scores:
        os.remove(population + "/" + s[0])


def runGeneticAlgorithm(population, gt, parameters, lastGeneration, survivorRatio, 
                        runID, lr=0.5):
    global learnRate; learnRate = lr
    global groundTruth; groundTruth = gt

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
            selectFittest(population, survivorRatio[0])
            
            # create offspring
            generateOffspring(survivorRatio[1], population, parameters)

            # check fitness
            min, max = calculateFitness(population, minmax=True) 
            
            f.write('least fit: ' +  str(max) + '\n')
            f.write('most fit: ' +  str(min) + '\n\n') 
            
            generation += 1
            

