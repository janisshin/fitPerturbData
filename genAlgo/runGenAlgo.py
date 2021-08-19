# for MMARL runs

import genAlgo_MMARL
import tellurium as te
import models

folderName = models.generateModelFiles(100, groundTruthModel_string=models.groundTruth_mod_e, parameters=models.K_LIST)
# folderName = 'genAlgo_population'
genAlgo_MMARL.runGeneticAlgorithm(folderName, survivorRatio=(10,90), lastGeneration=300, tolerance=0.1)