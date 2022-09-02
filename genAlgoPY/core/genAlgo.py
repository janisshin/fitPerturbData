from numpy.core.fromnumeric import sort
import tellurium as te
import random
import numpy as np
import os

from core import (PathwayModel, PathwayModel_utils, evaluate)

# one class to store all variables, all settings
# one class to store hyperparameters
# one class that brings the two together and runs the computation


class Hyper():
    """
    lastGeneration = int, max number of generations to run
    survivorRatio = tuple (survive, culled). survive + culled = total number of individuals 
        in population
    tolerance = float. genetic algorithm will stop running if fitting score < tolerance
    learnRate = float. learning rate of algorithm. Recommended to put between 0.1 and 1
    omit = int list. each int signifies a position to be omitted in the fitness evaluation. see ReadMe for positions and numbers. 
    """
    def __init__(self, n, lastGeneration=10, survivorRatio=None, tolerance=10, learnRate=0.1, omit=[]):

        self.lastGeneration = lastGeneration

        if not survivorRatio:
            self.survivorRatio = (int(n*0.9), int(n*0.2))

        self.tolerance = tolerance
        self.learnRate = learnRate
        self.omit = omit


class Engine():
    
    """
    Run genetic algorithm with a given population until convergence or last generation is reached. 
    Also prints out timestamps for each step
    Parameters
        population = name of folder containing antimony files of all individuals    
        runID = name of folder in which to put output file (runningOutput.list)
        
    Returns
        population = Str-list of Antimony strings of roadrunner models
    """
    
    def runGeneticAlgorithm(population, rxnModel, hyper, runID=None):

        parameters=rxnModel.parameters

        converged=False
        generation = 1    
        
        if runID:
            filename=runID + "/runningOutput.list"
        else: 
            filename="runningOutput.list"

        while not converged and generation < hyper.lastGeneration: 
            with open(filename, "a") as f:
                f.write('generation ' + str(generation) + '\n')
                
                # select fittest
                Engine.selectFittest(population, hyper.survivorRatio[0],rxnModel.antimonyStr, hyper.omit)
                
                # create offspring
                Engine.generateOffspring(hyper.survivorRatio[1], population, rxnModel.parameters, hyper.learnRate)

                # check fitness
                min, max = Engine.calculateFitness(population, rxnModel.antimonyStr, hyper.omit, True) 
                
                f.write('least fit: ' +  str(max) + '\n')
                f.write('most fit: ' +  str(min) + '\n') 
                
                generation += 1

                if max < hyper.tolerance:
                    f.write("tolerance")
                    converged = True
                elif max-min < 0.000001: # cutoff is 1e-6, just like in tellurium
                    f.write("convergence")
                    converged = True
                f.write(f"converged? {converged}"  + '\n\n')

    # Crossover
    def generateOffspring(nOffspring, population, parameters, learnRate):
        """
        creates new models from current model lineup
        Parameters
            n: number of offspring to make
            population: current gene pool
            parameters
        """
        for i in range(nOffspring):
            isMutation = bool(random.getrandbits(1))
            
            if isMutation: # mutation
                offspring = Engine.performMutation(population, parameters, learnRate)
            else:
                offspring = Engine.performCrossover(population, parameters)
        
            # write child to file
            j = 0
            while os.path.exists(population + "/antimonyModel_" + str(j) + ".txt"):
                j += 1
            fileName = population + "/antimonyModel_" + str(j) + ".txt"
            
            with open(fileName, "w") as f:
                f.write(offspring) 
            
            del offspring; del fileName
            

    def performMutation(population, parameters, learnRate):
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
            # how much to mutate the original value
            param_shift = random.uniform(-learnRate, learnRate) 
            original_parameter_value = child.getValue(mutation_site)
            mutated_parameter_value = original_parameter_value + original_parameter_value * param_shift
            child.setValue(mutation_site, mutated_parameter_value)
        
        del p; del n; del mutation_site; del param_shift; del original_parameter_value; 
        del mutated_parameter_value;

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


    def calculateFitness(population, groundTruth, omit, minmax=False):
        """
        population = name of directory containing Antimony files
        scores = dictionary of file name and score
        """
        scores = {}
        groundTruthData = evaluate.runExperiment(groundTruth, omit) ################
        for individual in os.listdir(population):
            with open(population + "/" + individual, "r") as f:
                individualData = evaluate.runExperiment(f.read(), omit)
            chiSq = np.sum(np.square(groundTruthData - individualData))
            scores[individual] = chiSq
        if minmax:
            return min(scores.values()), max(scores.values())
        else:
            return sorted(scores.items(), key=lambda x: x[1])
        return scores #### here might be the memory problem


    def selectFittest(population, nSurvivors, groundTruth, omit):
        """
        Selection step of genetic algorithm. Orders models from most fit to least fit. 
        Removes least fit models. 
        Parameters
            population: Str-list of Antimony strings of roadrunner models
            n: int
                number of survivors
            scoreResults: float-list
        """
        # compute fitness of population
        scores = Engine.calculateFitness(population, groundTruth, omit)

        # sorted_scores = sorted(scores.items(), key=lambda x: x[1])

        for ii in range(nSurvivors):
            scores.pop(0)
        
        for s in scores:
            os.remove(population + "/" + s[0])



