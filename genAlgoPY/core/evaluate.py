import tellurium as te
import random
import numpy as np
from core import PathwayModel

TIME_TO_SIMULATE = 100
N_DATAPOINTS = 100

def runExperiment(m, enzymes, omit=None):
    """
    Parameters: 
        m: Antimony str of model. PathwayModel.rxnModel(antimonyStr)
        enzymes: Str list of enzyme names in m. PathwayModel.rxnModel.enzymes
    Returns:
        allData: float list; foldchanges of species as enzyme levels are perturbed
    """
    model = te.loada(m)
    model.resetAll() # reset all
    s = model.simulate(0, TIME_TO_SIMULATE, N_DATAPOINTS) # simulate the trueModel
    ss = model.steadyState() # get the steadystate of the trueModel
    spConcs = model.getFloatingSpeciesConcentrations() # collect and store species concentrations (S2-S5)
    fluxes = np.array([model.getValue(model.getReactionIds()[0])])  # collect and store fluxes

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

        fluxes_e = np.array([model.getValue(model.getReactionIds()[0])]) 
        fluxFoldChange = (fluxes_e-fluxes)/fluxes
        fluxData[i,:] = fluxFoldChange

        model.setValue(e, 1)

    allData = np.concatenate((np.ravel(perturbationData), np.ravel(fluxData)))
    
    if omit: 
        trimmedData = np.delete(allData,omit)
        return trimmedData
    else:
        return allData 


def normalizer(x, trueValue):
    return (x-trueValue)/trueValue