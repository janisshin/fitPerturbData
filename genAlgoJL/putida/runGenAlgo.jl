# make sure to pwd to genAlgo\\banana before running this code

include("models.jl")
include("evaluate.jl")
include("genAlgo.jl")

using Main.Models
using Main.GenAlgo

using PyCall
te = pyimport("tellurium")

# cd("genAlgo\\banana")
# runID = Main.Models.makeFolder("data/", true)
# populationFolder = Main.Models.generateModelFiles(10, runID, "putida_4aca_MM_rdmfill.py", Main.Models.K_LIST_putida)
runID = "data/20211113_3"
populationFolder = "data/20211113_3/population_1/"
Main.GenAlgo.runGeneticAlgorithm(populationFolder, runID, "putida_4aca_MM_rdmfill.py", Main.Models.K_LIST_putida, 1)
