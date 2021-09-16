# 20210819

import tellurium as te
import numpy as np
from core import models
from core import evaluate

def getFoldChangeValues(testModel=te.loada(models.groundTruth_mod_e), parameters=models.K_LIST, data='', folder='', n_individuals=100):
    """
    Parameters

    Returns

    Create 'allData.list' file which lists the values of foldchanges for each model per line
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
    
    # open file
    with open(folder + "/allData.list", "w") as f:
        for row in arr:
            for i, parameter in enumerate(row):
                testModel.setValue(parameters[i], parameter) 
            alteredModel = testModel.getCurrentAntimony()
            allData = evaluate.runExperiment(alteredModel).tolist()
            s = " ".join(str(datum) for datum in allData)
            f.write(s + '\n') # possible problem if not a string
    