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

populationFolder = Main.Models.generateModelFiles(10, runID, "putida_shikimate_MM.py", Main.Models.KM_LIST)

Main.GenAlgo.runGeneticAlgorithm(populationFolder, runID, Main.Models.groundTruth_MM_e, Main.Models.KM_LIST)
