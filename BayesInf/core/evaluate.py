import tellurium as te
import numpy as np
import pandas as pd

from core.models import PERTURBATIONS


def runExperiment(m, enzymes=PERTURBATIONS):
    model = te.loada(m)
    model.resetAll() # reset all
    s = model.simulate(0, 40) # simulate the trueModel
    ss = model.steadyState() # get the steadystate of the trueModel
    spConcs = model.getFloatingSpeciesConcentrations() # collect and store species concentrations (S2-S5)
    fluxes = np.array([model.getValue(model.getReactionIds()[0])])  # collect and store fluxes

    # create empty arrays to store data
    perturbationData = np.empty([len(enzymes), len(spConcs)])
    fluxData = np.empty([len(enzymes), 1])
    
    for i, e in enumerate(enzymes.keys()): # for the number of enzymes, 
        model.setValue(e, enzymes.get(e)) # redefine e
        ss = model.steadyState() # calculate new steadystate
        
        spConcs_e = model.getFloatingSpeciesConcentrations() # collect and store species concentrations (S2-S5)
        spfoldChange = (spConcs_e-spConcs)/spConcs
        perturbationData[i,:] = spfoldChange # species fold change

        fluxes_e = np.array([model.getValue(model.getReactionIds()[0])]) 
        fluxFoldChange = (fluxes_e-fluxes)/fluxes
        fluxData[i,:] = fluxFoldChange

        model.resetToOrigin()

    allData = np.concatenate((np.ravel(perturbationData), np.ravel(fluxData)))
    
    return allData 