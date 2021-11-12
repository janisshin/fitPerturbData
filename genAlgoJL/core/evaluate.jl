using Random

import Distributions:Uniform 
using PyCall

te = pyimport("tellurium")

include("models.jl")

function runExperiment(m, enzymes=models.ENZYMES, omit=None)
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
    fluxes = model.getValue(model.getReactionIds()[0])  # collect and store fluxes

    # create empty arrays to store data
    perturbationData = Array{Float64}(undef, length(enzymes), length(spConcs))     
    # [len(enzymes), len(spConcs)]
    fluxData = [] # np.empty([len(enzymes), 1])
    
    for (i, e) in enumerate(enzymes) # for the number of enzymes, 
        # model.resetAll() # reset all 
        model.setValue(e, 2) # redefine e
        ss = model.steadyState() # calculate new steadystate
        
        spConcs_e = model.getFloatingSpeciesConcentrations() # collect and store species concentrations (S2-S5)
        spfoldChange = (spConcs_e-spConcs)/spConcs
        perturbationData[i,:] = spfoldChange
        # append !(perturbationData, spfoldChange) # species foldchange

        fluxes_e = model.getValue(model.getReactionIds()[0])
        fluxFoldChange = (fluxes_e-fluxes)/fluxes
        append!(fluxData, fluxFoldChange)

        model.setValue(e, 1)
    end

    allData = [reshape(perturbationData, length(perturbationData)); fluxData]
    
    if ! isnothing(omit)
        trimmedData = deleteat!(allData, omit)
        return trimmedData
    end
    return allData 
end
