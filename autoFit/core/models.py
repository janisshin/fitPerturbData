
import tellurium as te
import random
import os
from datetime import datetime

# all of the models are in String form

# the most basic model. 
groundTruth = ("""
  $S1 -> S2; k1*S1 - k2*S2
  S2 -> S3; k2*S2 - k3*S3
  S3 -> S4; k3*S3 - k4*S4
  S4 -> S5; k4*S4 - k5*S5
  S5 -> $S6; k5*S5 - k6*S6
  S1 = 1; 
  k1 = 1; 
  k2 = 2; 
  k3 = 3;
  k4 = 4; 
  k5 = 5;
  k6 = 6; 
""")

# groundTruth model with enzyme terms
groundTruth_e = ("""
  R1: $S1 -> S2; (e1) * (k1*S1 - k2*S2)
  R2: S2 -> S3; (e2) * (k2*S2 - k3*S3)
  R3: S3 -> S4; (e3) * (k3*S3 - k4*S4)
  R4: S4 -> S5; (e4) * (k4*S4 - k5*S5)
  R5: S5 -> $S6; (e5) * (k5*S5 - k6*S6)
  S1 = 1; 
  k1 = 1; 
  k2 = 2; 
  k3 = 3; 
  k4 = 4; 
  k5 = 5; 
  k6 = 6;
  e1 = 1; e2 = 1; e3 = 1; e4 = 1; e5 = 1;
""") 

# groundTruth model with reverse reaction constants replaced with Keq terms
groundTruth_mod = ("""
  v1: $S1 -> S2; k1*S1 * (1-(S2/S1)/Keq1)
  v2: S2 -> S3; k2*S2 * (1-(S3/S2)/Keq2)
  v3: S3 -> S4; k3*S3 * (1-(S4/S3)/Keq3)
  v4: S4 -> S5; k4*S4 * (1-(S5/S4)/Keq4)
  v5: S5 -> $S6; k5*S5 * (1-(S6/S5)/Keq5)
  S1 = 1; S2 = 0.1; S3 = 0.1; S4 = 0.1; S5 = 0.1;
  k1 = 1; Keq1 = 3; 
  k2 = 2; Keq2 = 3;
  k3 = 3; Keq3 = 3; 
  k4 = 4; Keq4 = 3;
  k5 = 5; Keq5 = 3; 
""")

# groundTruth model with reverse reaction constants replaced with Keq terms and enzyme terms
groundTruth_mod_e = ("""
  v1: $S1 -> S2; (e1) * k1*S1 * (1-(S2/S1)/Keq1)
  v2: S2 -> S3; (e2) * k2*S2 * (1-(S3/S2)/Keq2)
  v3: S3 -> S4; (e3) * k3*S3 * (1-(S4/S3)/Keq3)
  v4: S4 -> S5; (e4) * k4*S4 * (1-(S5/S4)/Keq4)
  v5: S5 -> $S6; (e5) * k5*S5 * (1-(S6/S5)/Keq5)
  S1 = 1; S2 = 0.1; S3 = 0.1; S4 = 0.1; S5 = 0.1;
  k1 = 1; Keq1 = 3; 
  k2 = 2; Keq2 = 3;
  k3 = 3; Keq3 = 3; 
  k4 = 4; Keq4 = 3;
  k5 = 5; Keq5 = 3; 
  e1 = 1; e2 = 1; e3 = 1; e4 = 1; e5 = 1;
""")

# v = Vm1/Km1*(S1 - S2/Keq)/(1 + S1/Km1 + S2/Km2)
# Michaelis-Menten model
groundTruth_MM = ("""
  v1: $S1 -> S2; Vm1/Km1*(S1 - S2/Keq1)/(1 + S1/Km1 + S2/Km2)
  v2: S2 -> S3; Vm2/Km3*(S2 - S3/Keq2)/(1 + S2/Km3 + S3/Km4)
  v3: S3 -> S4; Vm3/Km5*(S3 - S4/Keq3)/(1 + S3/Km5 + S4/Km6)
  v4: S4 -> S5; Vm4/Km7*(S4 - S5/Keq4)/(1 + S4/Km7 + S5/Km8)
  v5: S5 -> $S6; Vm5/Km9*(S5 - S6/Keq5)/(1 + S5/Km9 + S6/Km10)
  S1 = 1; S2 = 0.1; S3 = 0.1; S4 = 0.1; S5 = 0.1;
  Km1 = 0.51; Km2 = 0.62; Km3 = 0.93; Km4 = 1.4; Km5 = 2.5; 
  Km6 = 2.6; Km7 = 3.51; Km8 = 2.62; Km9 = 3.93; Km10 = 4.4;
  Keq1 = 3; Keq2 = 3; Keq3 = 3; Keq4 = 3; Keq5 = 3; 
  Vm1 = 1; Vm2 = 2; Vm3 = 4; Vm4 = 5; Vm5 = 7; 
""")

# Michaelis-Menten model with e 
groundTruth_MM_e = ("""
  v1: $S1 -> S2; e1 * Vm1/Km1*(S1 - S2/Keq1)/(1 + S1/Km1 + S2/Km2)
  v2: S2 -> S3; e2 * Vm2/Km3*(S2 - S3/Keq2)/(1 + S2/Km3 + S3/Km4)
  v3: S3 -> S4; e3 * Vm3/Km5*(S3 - S4/Keq3)/(1 + S3/Km5 + S4/Km6)
  v4: S4 -> S5; e4 * Vm4/Km7*(S4 - S5/Keq4)/(1 + S4/Km7 + S5/Km8)
  v5: S5 -> $S6; e5 * Vm5/Km9*(S5 - S6/Keq5)/(1 + S5/Km9 + S6/Km10)
  S1 = 1; S2 = 0.1; S3 = 0.1; S4 = 0.1; S5 = 0.1; S6 = 0.1;
  Km1 = 0.51; Km2 = 0.62; Km3 = 0.93; Km4 = 1.4; Km5 = 2.5; 
  Km6 = 2.6; Km7 = 3.51; Km8 = 2.62; Km9 = 3.93; Km10 = 4.4;
  Keq1 = 3; Keq2 = 3; Keq3 = 3; Keq4 = 3; Keq5 = 3; 
  e1 = 1; e2 = 1; e3 = 1; e4 = 1; e5 = 1;
  Vm1 = 1; Vm2 = 2; Vm3 = 4; Vm4 = 5; Vm5 = 7; 
""")

ENZYMES = ["e1", "e2", "e3", "e4", "e5"] 
PARAMETERS = te.loada(groundTruth).getGlobalParameterIds() # parameters for groundTruth model
MOD_PARAMETERS = ['Keq1','Keq2','Keq3','Keq4','Keq5']
TIME_TO_SIMULATE = 100
N_DATAPOINTS = 100
K_LIST = ['k1', 'k2', 'k3', 'k4', 'k5']
Km_LIST = ['Km1', 'Km2', 'Km3', 'Km4', 'Km5', 'Km6','Km7','Km8','Km9','Km10']

def generateModelFiles(n, groundTruthModel_string=groundTruth_e, parameters=PARAMETERS, knownValues={}, folderName=None):
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
        randomModel = te.loada(groundTruthModel_string) # make a copy of the model 
        # set k values to random numbers 
        for p in parameters:
            if p in knownValues.keys():
                pValue = knownValues.get(p)
            else:
                pValue = random.uniform(0, 1000)
            randomModel.setValue(p, pValue) # redefine parameters
        fileName = folderName + "/antimonyModel_" + str(number) + ".txt"
        f = open(fileName, "w")
        f.write(randomModel.getCurrentAntimony())
        f.close()
    return folderName

def generateSingleModel(groundTruthModel_string=groundTruth_e, parameters=PARAMETERS):
    """
    generates n number of models that do not contain Keq terms
    
    Parameters
        n: int. number of models desired by user
        model_string: String. template to make random models
        knownValues: dict. contains parameter name followed by numerical value
    Returns: 
        List of Strings. Models are expressed in String form and have random values for parameters. 
    """    
    randomModel = te.loada(groundTruthModel_string) # make a copy of the model 
    # set k values to random numbers 
    for p in parameters:
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