module Evaluate

using Main.Models
               
using Random
using RoadRunner

function runExperiment(m, enzymes=Main.Models.ENZYMES_putida)
    """
    Parameters: 
        m: Antimony str of model
        enzymes: Str list of enzyme names in m
    Returns:
        allData: float list; foldchanges of species as enzyme levels are perturbed
    """
    RoadRunner.setConfigInt("LOADSBMLOPTIONS_CONSERVED_MOIETIES", 1)
    
    model = RoadRunner.createRRInstance()
    io = open(m)
    RoadRunner.loadSBML(model, read(io, String))
    close(io)

    RoadRunner.resetAll(model) # reset all
    RoadRunner.simulateEx(model, 0, Main.Models.TIME_TO_SIMULATE, Main.Models.TIME_TO_SIMULATE)
    RoadRunner.steadyState(model) # get the steadystate of the trueModel
    spConcs = RoadRunner.getFloatingSpeciesConcentrations(model) # collect and store species concentrations (S2-S5)
    fluxes = RoadRunner.getValue(model, RoadRunner.getReactionIds(model)[1]) 

    # create empty arrays to store data
    perturbationData = Array{Float64}(undef, length(enzymes), length(spConcs))     
    fluxData = [] 
    
    for (i, e) in enumerate(enzymes) # for the number of enzymes, 
        RoadRunner.setValue(model, e, 2.0) # redefine e
        RoadRunner.steadyState(model) # calculate new steadystate
        
        spConcs_e = RoadRunner.getFloatingSpeciesConcentrations(model) # collect and store species concentrations (S2-S5)
        spfoldChange = (spConcs_e-spConcs)./spConcs
        perturbationData[i,:] = spfoldChange

        fluxes_e = RoadRunner.getValue(model, RoadRunner.getReactionIds(model)[1])
        fluxFoldChange = (fluxes_e-fluxes)./fluxes
        append!(fluxData, fluxFoldChange)

        RoadRunner.resetAll(model)
        # RoadRunner.setValue(model, e, 1.0)
    end

    allData = [reshape(perturbationData, length(perturbationData)); fluxData]

    return allData 
end
end
