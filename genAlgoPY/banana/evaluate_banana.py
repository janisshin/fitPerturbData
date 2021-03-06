# runExperiment evaluates relative (foldchange) concentrations and fluxes

import tellurium as te
import random
import numpy as np
import pandas as pd

from banana import models_banana

def runBanana(m):
    model = te.loada(m)
    return (1.0 - model.k2)**2 + 100.0 * (model.k3 - model.k2**2)**2 

def runExperiment(m, enzymes=models.ENZYMES):
    """
    model is a roadrunner object
    """
    model = te.loada(m)
    model.resetAll() # reset all
    s = model.simulate(0, models.TIME_TO_SIMULATE, models.N_DATAPOINTS) # simulate the trueModel
    ss = model.steadyState() # get the steadystate of the trueModel
    spConcs = model.getFloatingSpeciesConcentrations() # collect and store species concentrations (S2-S5)
    fluxes = np.array([model.getValue(model.getReactionIds()[0])]) #, model.getValue(model.getReactionIds()[-1])]) # collect and store fluxes

    # create empty arrays to store data
    perturbationData = np.empty([len(enzymes), len(spConcs)])
    fluxData = np.empty([len(enzymes), 1])
    
    for i, e in enumerate(enzymes): # for the number of enzymes, 
        # model.resetAll() # reset all 
        model.setValue(e, 2) # redefine e
        ss = model.steadyState() # calculate new steadystate
        
        spConcs_e = model.getFloatingSpeciesConcentrations() # collect and store species concentrations (S2-S5)
        spfoldChange = (spConcs_e-spConcs)/spConcs
        perturbationData[i,:] = spfoldChange # species fold change

        fluxes_e = np.array([model.getValue(model.getReactionIds()[0])]) #, model.getValue(model.getReactionIds()[-1])])
        fluxFoldChange = (fluxes_e-fluxes)/fluxes
        fluxData[i,:] = fluxFoldChange

        model.setValue(e, 1)

    allData = np.concatenate((np.ravel(perturbationData), np.ravel(fluxData)))# , np.ravel(spConcs)))
    # allData = np.append(allData, fluxes)

    return allData 



def makeDataFrame(paramResultsFile):
    """
    input: paramResults from fitMultipleModels method
    
    """

    # open the results file
    f = open(paramResultsFile, "r") # "fitMultipleModelsData.txt"
    lines = f.read()
    # parse the data into an array 
    arr = np.array(lines.splitlines())
    f.close()
    arr = arr.astype('float64')
    arr = np.reshape(arr, (int(len(arr)/11), 11))

    # convert to pandas
    return pd.DataFrame(arr, columns = ['k1','k11','k2', 'k22','k3','k33','k4','k44','k5','k55','chiSq'])

def useFittedParams(data, pdIndex):
    """
    output: returns roadRunner with paramResult parameters
    """
    
    m = te.loada(models.groundTruth_e)
    
    # grab the pandas row
    series = data.loc[pdIndex]
    # for each element in the row, set the Value
    for i in models.K_LIST:
        m.setValue(i, series[i])
    
    return m

def normalizer(x, trueValue):
    return (x-trueValue)/trueValue