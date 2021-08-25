# 20210819

import tellurium as te
import numpy as np
from core import models
from core import evaluate

def getFoldChangeValues(testModel=te.loada(models.groundTruth_mod_e), paramData="paramData.list", folderName='data'):
    """
    Parameters

    Returns

    Create 'allData.list' file which lists the values of foldchanges for each model per line
    """
    # take in the file paramData.list
    # open the results file
    f = open(paramData, "r")
    lines = f.read()
    
    # parse the data into an array 
    list_of_lines = lines.splitlines()
    f.close()
    
    # reshape into numpy
    arr = np.array(list_of_lines)
    arr = arr.astype('float64')
    arr = np.reshape(arr, (100, 5)) # should replace these numbers with variables
    

    # for each row in array
        # set the test model's parameters to the 5 parameters
        # runExperiment
        # print allData

    # open file
    f = open(folderName + "/allData.list", "w")

    for row in arr:
        for i, parameter in enumerate(row):
            testModel.setValue(models.K_LIST[i], parameter) 
        alteredModel = testModel.getCurrentAntimony()
        allData = evaluate.runExperiment(alteredModel).tolist()
        s = " ".join(str(datum) for datum in allData)
        f.write(s + '\n') # possible problem if not a string
    f.close()
