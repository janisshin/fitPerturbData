# revised 20210816
# evaluate_4
# runExperiment evaluates relative (foldchange) concentrations and fluxes

import tellurium as te
import random
import numpy as np
import pandas as pd

from core import models

def runExperiment(m, enzymes=models.ENZYMES):
    """
    Parameters: 
        m: Antimony str of model
        enzymes: Str list of enzyme names in m
    Returns:
        allData: float list; foldchanges of species as enzyme levels are perturbed
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

def runExperiment_omit(m, enzymes=models.ENZYMES):
    """
    Parameters: 
        m: Antimony str of model
        enzymes: Str list of enzyme names in m
    Returns:
        trimmedData: float list; foldchanges of species as enzyme levels are perturbed with some values omitted
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
    trimmedData = np.delete(allData,[0,4])

    return trimmedData

def normalizer(x, trueValue):
    return (x-trueValue)/trueValue