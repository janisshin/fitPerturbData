# make sure to pwd to genAlgo\\banana before running this code

include("models_banana.jl")
include("evaluate_banana.jl")
include("genAlgo_banana.jl")

using Main.Banana_Models
using Main.Banana_GenAlgo

using PyCall
te = pyimport("tellurium")

# cd("genAlgo\\banana")

runID = Main.Banana_Models.makeFolder("data/", true)

# to run Michaelis-Menten model
populationFolder = Main.Banana_Models.generateModelFiles(100, runID)
# runID = "data/20211108_4"
# populationFolder = "data/20211108_4/banana_population_1"

Main.Banana_GenAlgo.runGeneticAlgorithm(populationFolder, runID)


