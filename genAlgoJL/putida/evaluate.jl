module Evaluate

using Main.Models
               
using Random
using PyCall
te = pyimport("tellurium")

function runExperiment(m, enzymes=Main.Models.ENZYMES_putida)
    """
    Parameters: 
        m: Antimony str of model
        enzymes: Str list of enzyme names in m
    Returns:
        allData: float list; foldchanges of species as enzyme levels are perturbed
    """
    model = te.loada(m)
    model.resetAll() # reset all
    model.simulate(0, Main.Models.TIME_TO_SIMULATE) # simulate the trueModel
    model.conservedMoietyAnalysis = true
    println("pass") #####################################################
    model.steadyState() # get the steadystate of the trueModel
    spConcs = model.getFloatingSpeciesConcentrations() # collect and store species concentrations (S2-S5)
    fluxes = model.getValue(model.getReactionIds()[1]) #, model.getValue(model.getReactionIds()[-1])]) # collect and store fluxes

    # create empty arrays to store data
    perturbationData = Array{Float64}(undef, length(enzymes), length(spConcs))     
    fluxData = [] 
    
    for (i, e) in enumerate(enzymes) # for the number of enzymes, 
        model.setValue(e, 2) # redefine e
        ss = model.steadyState() # calculate new steadystate
        
        spConcs_e = model.getFloatingSpeciesConcentrations() # collect and store species concentrations (S2-S5)
        spfoldChange = (spConcs_e-spConcs)./spConcs
        perturbationData[i,:] = spfoldChange

        fluxes_e = model.getValue(model.getReactionIds()[1])
        fluxFoldChange = (fluxes_e-fluxes)./fluxes
        append!(fluxData, fluxFoldChange)

        model.setValue(e, 1)
    end

    allData = [reshape(perturbationData, length(perturbationData)); fluxData]

    return allData 
end
end
