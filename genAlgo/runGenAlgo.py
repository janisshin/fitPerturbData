from core import genAlgo_MMARL
import tellurium as te
from core import models

runID = models.makeFolder('data/',date = True)

# to run mass-action rate law model
# populationFolder = models.generateModelFiles(100, groundTruthModel_string=models.groundTruth_mod_e, parameters=models.K_LIST, folderName=runID)
# folderName = 'genAlgo_population'
# genAlgo_MMARL.runGeneticAlgorithm(populationFolder, survivorRatio=(10,90), lastGeneration=300, tolerance=0.01, runID=runID)

# to run Michaelis-Menten model
populationFolder = models.generateModelFiles(100, groundTruthModel_string=models.groundTruth_MM_e, parameters=models.Km_LIST, folderName=runID)
genAlgo_MMARL.runGeneticAlgorithm(populationFolder, groundTruth=models.groundTruth_MM_e, parameters=models.Km_LIST, survivorRatio=(10,90), lastGeneration=300, tolerance=0.01, runID=runID)