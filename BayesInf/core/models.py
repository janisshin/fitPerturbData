import tellurium as te
import random
import os
from datetime import datetime


# all of the models are in String form

# the most basic model. 
tiny_MA = (""" 
    R_PGM: -> $M_2PG; (k2*M_2PG)*(PGM);
    R_ENO: M_2PG -> M_PEP; (k3*M_2PG-k4*M_PEP)*(ENO);
    R_PK: $M_ADP + M_PEP ->; (k5*(M_ADP)*(M_PEP))*(PK);
    M_2PG = 178; M_PEP = 0; M_ADP = 13.2;
    k2 = 0.013; k3 = 0.1343; k4 = 0.1079; k5 = 3.333E-4;
    PGM = 45; ENO = 6.5; PK = 34;
""")

tiny_MM = (""" 
    R_PGM: -> $M_2PG; (PGM) * (Vm1/Km1) * (M_2PG/Keq1)/(1 + M_2PG/Km2)
    R_ENO: M_2PG -> M_PEP; (ENO)* (Vm2/Km3) * (M_2PG - M_PEP/Keq2)/(1 + M_2PG/Km3 + M_PEP/Km4)
    R_PK: $M_ADP + M_PEP -> ; (PK) * (Vm3/Km5) * ((M_ADP)*(M_PEP))/(1 + (M_ADP)*(M_PEP)/Km5)
    M_2PG = 178; M_PEP = 0; M_ADP = 13.2;
    PGM = 45; ENO = 6.5; PK = 34;
    Km1 = 0.51; Km2 = 0.62; Km3 = 0.93; Km4 = 1.4; Km5 = 2.5; 
    Keq1 = 3; Keq2 = 3; Vm1 = 1; Vm2 = 2; Vm3 = 4;
""")

TIME_TO_SIMULATE = 100
N_DATAPOINTS = 100
PARAMETERS = ['Vm1','Km1','Keq1','Km2','Vm2','Km3','Keq2','Km4','Vm3','Km5']
PERTURBATIONS = {'PGM':53.2, 'ENO':5.3, 'PK':30.9}
ENZYMES = PERTURBATIONS.keys()


def generateModelFiles(n, groundTruthModel_string=tiny_MM, parameters=PARAMETERS, folderName=None):
    # make a folder 
    if not folderName:
        folderName = makeFolder("genAlgo_population")
    else:
        folderName = makeFolder(folderName + '/genAlgo_population')

    for number in range(n):
        randomModel = te.loada(groundTruthModel_string) # make a copy of the model 
        # set k values to random numbers 
        for p in parameters:
            pValue = random.uniform(0, 1000)
            randomModel.setValue(p, pValue) # redefine parameters
        fileName = folderName + "/antimonyModel_" + str(number) + ".txt"
        f = open(fileName, "w")
        f.write(randomModel.getCurrentAntimony())
        f.close()
    return folderName

# check if folder exists; if not, make a new folder
def makeFolder(folderName, date=False):
    i = 1
    if date:
        now = datetime.now() # current date and time
        folderName = folderName + now.strftime("%Y-%m-%d")
    
    numbered_folderName = folderName + "_" + str(i)
    if not os.path.exists(numbered_folderName):
        os.mkdir(numbered_folderName)
        return numbered_folderName
    while os.path.exists(numbered_folderName):
        i += 1
        numbered_folderName = folderName + "_" + str(i)
    os.mkdir(numbered_folderName)
    return numbered_folderName