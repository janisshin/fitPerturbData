module GenAlgo

using RoadRunner
using Random
using Main.Models

import Distributions: Uniform 


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
        while isdir(population * "/SBMLModel_" * string(i, base = 10, pad=3) * ".xml")
            j += 1
        end
        fileName = population * "/SBMLModel_" * string(i, base = 10, pad=3) * ".xml"
        
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
    child = RoadRunner.createRRInstance()
    io = open(parent, "r");
    RoadRunner.loadSBML(child, read(io, String))
    close(io)

    n = rand(1: length(p)-1) # number of mutations to make in an individual

    for i in 1:n
        shuffle!(p) # shuffle parameters
        mutation_site = pop!(p) # choose a random parameter to be mutated
    
        # how much to mutate the original value
        param_shift = rand(Uniform(-0.2, 0.2))
        original_parameter_value = RoadRunner.getValue(child, mutation_site)
        mutated_parameter_value = original_parameter_value + original_parameter_value * param_shift
        RoadRunner.setValue(child, mutation_site, mutated_parameter_value)
    end
    return RoadRunner.getCurrentSBML(child)   
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
    pA = population * "/" * rand(readdir(population))
    pB = population * "/" * rand(readdir(population))
    while pA == pB
        pB = population * "/" * rand(readdir(population))
    end

    parentA = RoadRunner.createRRInstance()
    child = RoadRunner.createRRInstance()
    A = open(pA, "r")
    RoadRunner.loadSBML(parentA, read(A, String))
    close(A)
    B = open(pB, "r")
    RoadRunner.loadSBML(child, read(B, String))
    close(B)    

    for p in parameters[1:end-length(parameters)] 
        RoadRunner.setValue(child, p, RoadRunner.getValue(parentA, p))
    end

    return RoadRunner.getCurrentSBML(child) 

end

function calculateFitness(population, groundTruth) 
    #="""
    population = name of directory containing Antimony files
    scores = dictionary of file name and score
    """=#
    scores = Dict()

    groundTruthData = Main.Evaluate.runExperiment(groundTruth) #, omit=omission
    for individual in readdir(population)
        individualData = Main.Evaluate.runExperiment(population * "/" * individual)# , omit=omission)
        if individualData !== nothing
            chiSq = sum((groundTruthData - individualData).^2)
            scores[individual] = chiSq
        end
    end
    return scores 
end

function selectFittest(population, groundTruth, n)
    
    # compute fitness of population
    scores = calculateFitness(population, groundTruth)

    sorted_scores = reverse(sort(collect(scores), by=x->x[2]))

    # remove the survivors from the list of sorted scores. 
    for ii in 1:n
        pop!(sorted_scores)
    end

    for s in sorted_scores
        rm(population * "/" * s[1], force=true)
    end 
end

function extractParams(population, parameters, groundTruth, folderName)
    scores = calculateFitness(population, groundTruth)

    for score in values(scores)
        open(folderName * "/scores.list", "a") do scoreFile
            write(scoreFile, string(score) * "\n")
        end
    end
end

function runGeneticAlgorithm(runID, groundTruth=Main.Models.groundTruth_e, parameters=Main.Models.K_LIST, lastGeneration=10, survivorRatio=(2,8), tolerance=1)

    converged=false
    generation = 1    
    population = runID*"/population_1"

    while !converged && generation < lastGeneration + 1
        open(runID * "/runningOutput.list", "a") do io
            write(io, "generation " * string(generation) * "\n")
        end
            
        # select fittest
        selectFittest(population, groundTruth, survivorRatio[1])
            
        # create offspring
        offspring = generateOffspring(survivorRatio[2], population, parameters)

        # check fitness
        scores = calculateFitness(population, groundTruth) 

        open(runID * "/runningOutput.list", "a") do io
            write(io, "most fit: " * string(minimum(values(scores))) * "\n")
            write(io, "least fit: " *  string(maximum(values(scores))) * "\n\n") 
        end 
            
        generation += 1

    end
    # print params and scores to files
    extractParams(population, parameters, groundTruth, runID)
end

end
