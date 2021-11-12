import os
import tellurium as te
import numpy as np
from core import models
from core import evaluate

    
def extractParams(population, parameters, groundTruth, folderName='', omit=None):
    groundTruthData = evaluate.runExperiment(groundTruth, omit=omit)
    
    if folderName: 
        scoreFile = open(folderName + "/scores.list", "w")
        paramFile = open(folderName + "/paramData.list", "w")
    else: 
        scoreFile = open("scores.list", "w")
        paramFile = open("paramData.list", "w")

    for individual in os.listdir(population):
        f = open(population + "/" + individual, "r")
        individualModel = f.read()
        individualData = evaluate.runExperiment(individualModel, omit=omit)
        chiSq = np.sum(np.square(groundTruthData - individualData))
        scoreFile.write(str(chiSq) + "\n")
        for k in parameters:
            paramFile.write(str(te.loada(individualModel).getValue(k)) + '\n')
        f.close()
    paramFile.close()
    scoreFile.close()


def getFoldChangeValues(testModel=te.loada(models.groundTruth_mod_e), parameters=models.K_LIST, 
                        data='', folder='', n_individuals=100):
    """
    Create 'allData.list' file which lists the values of foldchanges for each model per line

    Parameters
        testModel: roadrunner object of groundtruth model
        parameters: Str list of parameter names
        data: Str name of file with parameters
        folder: Str name of folder to place results file
        n_individuals: number of individuals in population
    """
    # take in the file paramData.list
    # open the results file
    f = open(data, "r")
    lines = f.read()
    
    # parse the data into an array 
    list_of_lines = lines.splitlines()
    f.close()
    
    # reshape into numpy
    arr = np.array(list_of_lines)
    arr = arr.astype('float64')
    # (number of models, number of parameters per model)
    arr = np.reshape(arr, (n_individuals, len(parameters))) 
    
    
    with open(folder + "/allData.list", "w") as f:
        for row in arr:
            for i, parameter in enumerate(row):
                testModel.setValue(parameters[i], parameter) 
            alteredModel = testModel.getCurrentAntimony()
            allData = evaluate.runExperiment(alteredModel).tolist()
            s = " ".join(str(datum) for datum in allData)
            f.write(s + '\n') # possible problem if not a string
