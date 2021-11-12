module GenAlgo

using PyCall
using Random
using Main.Models

import Distributions: Uniform 

# Python packages
te = pyimport("tellurium")
np = pyimport("numpy")

# Crossover
function generateOffspring(n, population, parameters)
     #="""
    creates new models from current model lineup
    Parameters
        n: number of offspring to make
        population: current gene pool
        parameters
    """=#
    for i in 1:n
        isMutation = rand(Bool, 1)
        
        if isMutation == [1] # mutation
            offspring = performMutation(population, parameters)
        else
            offspring = performCrossover(population, parameters)
        end
    
        # write child to file
        j = 0
        while isdir(population * "/antimonyModel_" * string(i, base = 10, pad=3) * ".txt")
            j += 1
        end
        fileName = population * "/antimonyModel_" * string(i, base = 10, pad=3) * ".txt"
        
        open(fileName, "w") do io
            write(io, offspring) 
        end;
    end
end
        
        
function performMutation(population, parameters)
    #="""
    performs a mutation on a random number of parameters for each individual in population
    Parameters
        population: folder of current gene pool
    Returns
        Antimony string of child
    """=#
    p = copy(parameters)
    
    # randomly choose an existing file
    parent = population * "/" * rand(readdir(population))

    io = open(parent, "r");
    child = te.loada(read(io, String))
    close(io)

    n = rand(1: length(p)-1) # number of mutations to make in an individual

    for i in 1:n
        shuffle!(p) # shuffle parameters
        mutation_site = pop!(p) # choose a random parameter to be mutated
    
        # how much to mutate the original value
        param_shift = rand(Uniform(-0.2, 0.2))
        original_parameter_value = child.getValue(mutation_site)
        mutated_parameter_value = original_parameter_value + original_parameter_value * param_shift
        child.setValue(mutation_site, mutated_parameter_value)
    end
    return child.getCurrentAntimony()
end


function performCrossover(population, parameters)
    #="""
    Parameters
        currentPopulation = Str-list of Antimony strings of roadrunner models
        parameters = Str-list
            the parameters which will be crossed over in the parents to create new offspring
    Returns
        offspring = Str-list of Antimony strings of roadrunner models
            list will be the same length as currentPopulation
    """=#
    
    # choose the parents
    parentA = population * "/" * rand(readdir(population))
    parentB = population * "/" * rand(readdir(population))
    while parentA == parentB
        parentB = population * "/" * rand(readdir(population))
    end

    A = open(parentA, "r")
    parentA = te.loada(read(A, String))
    close(A)
    B = open(parentB, "r")
    child = te.loada(read(B, String))
    close(B)    

    for p in parameters[1:end-length(parameters)] 
        child.setValue(p, parentA.getValue(p))
    end

    return child.getCurrentAntimony()
end


function calculateFitness(population, groundTruth) 
    #="""
    population = name of directory containing Antimony files
    scores = dictionary of file name and score
    """=#
    scores = Dict()

    groundTruthData = Main.Evaluate.runExperiment(groundTruth) #, omit=omission
    for individual in readdir(population)
        
        io = open(population * "/" * individual, "r")
        individualData = Main.Evaluate.runExperiment(read(io, String))# , omit=omission)
        close(io)
    
        chiSq = sum((groundTruthData - individualData).^2)
        scores[individual] = chiSq
    end
    return scores #### here might be the memory problem
end


function selectFittest(population, groundTruth, n)
    #="""
    Selection step of genetic algorithm. Orders models from most fit to least fit. 
    Removes least fit models. 
    Parameters
        population: Str-list of Antimony strings of roadrunner models
        n: int
            number of culled members
        scoreResults: float-list
    """=#
    
    # compute fitness of population
    scores = calculateFitness(population, groundTruth)

    sorted_scores = reverse(sort(collect(scores), by=x->x[2]))

    for ii in 1:n
        pop!(sorted_scores)
    end

    for s in sorted_scores
        rm(population * "/" * s[1], force=true)
    end 
end

function runGeneticAlgorithm(population, runID, groundTruth=Main.Models.groundTruth_e, parameters=Main.Models.K_LIST, lastGeneration=10, survivorRatio=(2,8), tolerance=1)
#function runGeneticAlgorithm(population, gt, parameters, lastGeneration, survivorRatio, tolerance, runID, lr, omit)
    #="""
    Run genetic algorithm with a given population until convergence or last generation is reached. 
    Also prints out timestamps for each step
    Parameters
        population = name of folder containing antimony files of all individuals
        groundTruth = Antimony Str representation of model to be evaluated
        parameters = Str list of parameter names in groundTruth model
        lastGeneration = int, max number of generations to run
        survivorRatio = tuple (survive, culled). survive + culled = total number of individuals 
            in population
        tolerance = float. genetic algorithm will stop running if fitting score < tolerance
        runID = name of folder in which to put output file (runningOutput.list)
        lr = float. learning rate of algorithm. Recommended to put between 0.1 and 1
        omit = int list. each int signifies a position to be omitted in the fitness evaluation. 
            see ReadMe for positions and numbers. 

    Returns
        population = Str-list of Antimony strings of roadrunner models
    """=#

    converged=false
    generation = 1    
    
    fileName = runID * "/runningOutput.list"
    
    while !converged && generation < lastGeneration + 1
        open(fileName, "a") do io
            write(io, "generation " * string(generation) * "\n")
        end
            
        # select fittest
        selectFittest(population, groundTruth, survivorRatio[1])
            
        # create offspring
        offspring = generateOffspring(survivorRatio[2], population, parameters)

        # check fitness
        scores = calculateFitness(population, groundTruth) 

        open(fileName, "a") do io
            write(io, "most fit: " * string(minimum(values(scores))) * "\n")
            write(io, "least fit: " *  string(maximum(values(scores))) * "\n") 
        end 
            
        generation += 1

        open(fileName, "a") do io
            write(io, "\n")
        end
    end
end
end
