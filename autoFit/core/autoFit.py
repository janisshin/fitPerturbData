# autoFit_single_MMARL_4.py

## this script fits the model to the concentration and flux fold change

import tellurium as te
import numpy as np
import lmfit

from core import models
from core import evaluate


def fitMultipleModels(n, folder=None, groundTruthModel=models.groundTruth_mod_e, toFit=models.K_LIST, enzymes=models.ENZYMES):
    """
    Takes in a list of different scrambled models and tries to find parameters which match them to the ground truth model

    Parameters
        n = number of iterations
        groundTruthModel = ground truth model with elasticity parameters
        toFit = String-list, model parameters
        enzymes = Str-list, elasticity terms

    Returns 
        paramResults: list of lists of parameter values for each model
        scoreResults: list of sum of squared residuals (chi-sq)

    Creates
        fitMultipleModelsData.list
    """
    def residuals(p): # p for parameters that change when lmfitting
        y1 =  groundTruth - runExperiment_pFit(p) # this is a list of differences
        return y1

    def runExperiment_pFit(p):

        m = te.loada(model)
        v = p.valuesdict()

        for i in range(0, len(toFit)): # declare all k's as parameters in fitting 
            m[toFit[i]] = v[toFit[i]] # set a parameter based on its name
        
        s = m.simulate(0, models.TIME_TO_SIMULATE, models.N_DATAPOINTS) # simulate the trueModel
        ss = m.steadyState() # get the steadystate of the trueModel
        spConcs = m.getFloatingSpeciesConcentrations() # collect and store initial species concentrations (S2-S5)
        fluxes = np.array([m.getValue(m.getReactionIds()[0])]) #, m.getValue(m.getReactionIds()[-1])])

        perturbationData = np.empty([len(enzymes), len(spConcs)]) # number of steps vs number of concentrations
        fluxData = np.empty([len(enzymes), 1]) # number of steps vs first + last flux

        for i, e in enumerate(enzymes): # for the number of enzymes, 
            
            m.resetAll()
            m.setValue(e, 2) # redefine e
            ss = m.steadyState() # calculate new steadystate
            spConcs_e = m.getFloatingSpeciesConcentrations() # collect and store species concentrations (S2-S5)

            spfoldChange = evaluate.normalizer(evaluate.normalizer(spConcs_e, spConcs), groundTruth[(i*4):(i*4+4)]) # 4 each time # (spConcs_e-spConcs)/spConcs
            perturbationData[i,:] = spConcs_e # spfoldChange

            fluxes_e = np.array([m.getValue(m.getReactionIds()[0])]) #, m.getValue(m.getReactionIds()[-1])])

            fluxFoldChange = evaluate.normalizer(evaluate.normalizer(fluxes_e, fluxes), groundTruth[20+i]) # 1 each time # (fluxes_e-fluxes)/fluxes
            fluxFoldChange = evaluate.normalizer(fluxes_e, fluxes)

            fluxData[i,:] = fluxFoldChange

        allData = np.concatenate((np.ravel(perturbationData), np.ravel(fluxData))) # , np.ravel(spConcs)))
        # allData = np.append(allData, fluxes)

        return allData 

    groundTruth = evaluate.runExperiment(groundTruthModel)
    params = lmfit.Parameters()

    if folder:
        fileName = folder + '/fittedParam.list'
    else: 
        fileName = 'fittedParam.list'
    
    with open(fileName, "a") as f:
    
        for i in range(n): 
            model = models.generateSingleModel(groundTruthModel_string=models.groundTruth_mod_e, parameters=models.K_LIST)

            for param in toFit: 
                params.add(param, value=1, min=0, max=1000) # add each parameter to the list of params that lmfit will fit

            minimizer = lmfit.Minimizer(residuals, params)  
            result = minimizer.minimize(method='differential_evolution') # DETERMINISTIC 
            
            for ii in models.K_LIST:
                f.write(str(result.params[ii].value) + '\n')
                # print(str(result.params[ii].value) + '\n')
            f.write(str(result.chisqr) + '\n')
            # print(str(result.chisqr) + '\n')
    
