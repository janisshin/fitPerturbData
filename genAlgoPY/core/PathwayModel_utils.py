import tellurium as te
import random
import os
from datetime import datetime

from core import PathwayModel

def generateModelFiles(n, rxnModel, folderName=None):
    """
    generates n number of models that do not contain Keq terms
    
    Parameters
        n: int number of models desired by user
        groundTruthModel_string: Str from which to make random models
        parameters: Str list of k's
        knownValues: dict. contains parameter name followed by numerical value
        folderName: Str name of folder to place folder of model files in
    Returns: 
        List of Strings. Models are expressed in String form and have random values for parameters. 
    """
    # make a folder 
    if not folderName:
        folderName = makeFolder("genAlgo_population")
    else:
        folderName = makeFolder(folderName + '/genAlgo_population')

    for number in range(n):
        randomModel = te.loada(rxnModel.antimonyStr) # make a copy of the model 
        # set k values to random numbers 
        for p in rxnModel.parameters:
            pValue = random.uniform(0, 1)
            randomModel.setValue(p, pValue) # redefine parameters
        fileName = folderName + "/antimonyModel_" + str(number) + ".txt"
        f = open(fileName, "w")
        f.write(randomModel.getCurrentAntimony())
        f.close()
    return folderName


def generateSingleModel(rxnModel):
    """
    generates n number of models that do not contain Keq terms
    
    Parameters
        n: int. number of models desired by user
        model_string: String. template to make random models
        knownValues: dict. contains parameter name followed by numerical value
    Returns: 
        List of Strings. Models are expressed in String form and have random values for parameters. 
    """    
    randomModel = te.loada(rxnModel.antimonyStr) # make a copy of the model 
    # set k values to random numbers 
    for p in rxnModel.parameters:
        pValue = random.uniform(0, 1000)
        randomModel.setValue(p, pValue) # redefine parameters
    return randomModel.getCurrentAntimony()


# check if folder exists; if not, make a new folder
def makeFolder(folderName, date=False):
    """
    Returns
        numbered_folderName: Str
    """
    i = 1

    if date:
        now = datetime.now() # current date and time
        folderName = folderName + now.strftime("%Y%m%d")
    
    numbered_folderName = folderName + "_" + str(i)
    if not os.path.exists(numbered_folderName):
        os.mkdir(numbered_folderName)
        return numbered_folderName
    while os.path.exists(numbered_folderName):
        i += 1
        numbered_folderName = folderName + "_" + str(i)
    os.mkdir(numbered_folderName)
    return numbered_folderName