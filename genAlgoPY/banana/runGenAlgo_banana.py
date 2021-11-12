from banana import genAlgo_banana
import tellurium as te
from banana import models_banana

runID = models_banana.makeFolder('data/',date = True)


# to run Michaelis-Menten model
populationFolder = models_banana.generateModelFiles(100, groundTruthModel_string=models_banana.groundTruth_e, parameters=models_banana.K_LIST, folderName=runID)
genAlgo_banana.runGeneticAlgorithm(populationFolder, groundTruth=models_banana.groundTruth_e, parameters=models_banana.K_LIST, survivorRatio=(10,90), lastGeneration=300, tolerance=0.001, runID=runID)