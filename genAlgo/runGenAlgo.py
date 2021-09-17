import tellurium as te
from tellurium.tellurium import model

from core import genAlgo_MMARL
from core import models

import backCheck

# configure run
modeltype=models.groundTruth_MM_e
p = models.Km_LIST
runID = models.makeFolder('data/',date = True)

# to run Michaelis-Menten model
populationFolder = models.generateModelFiles(100, groundTruthModel_string=modeltype, 
                                                parameters=p, folderName=runID)
genAlgo_MMARL.runGeneticAlgorithm(populationFolder, groundTruth=modeltype,
                                    parameters=p, survivorRatio=(10,90), 
                                    lastGeneration=300, tolerance=0.01, runID=runID)

# print params and scores to files
genAlgo_MMARL.extractParams(populationFolder, p, modeltype, folderName=runID)


backCheck.getFoldChangeValues(testModel=te.loada(modeltype), 
                                parameters=p, data='', folder='', n_individuals=100)