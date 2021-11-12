# make sure to pwd to genAlgo\\banana before running this code

include("models.jl")
include("evaluate.jl")
include("genAlgo.jl")

using Main.Models
using Main.GenAlgo

using PyCall
te = pyimport("tellurium")

# cd("genAlgo\\banana")

runID = Main.Models.makeFolder("data/", true)

# to run Michaelis-Menten model
populationFolder = Main.Models.generateModelFiles(10, runID)

Main.GenAlgo.runGeneticAlgorithm(populationFolder, runID)


