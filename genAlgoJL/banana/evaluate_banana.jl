module Banana_Evaluate

using Main.Banana_Models
               
using Random
using PyCall
te = pyimport("tellurium")

function runBanana(m)
    model = te.loada(m)
    return (1.0 - model.k2)^2 + 100.0 * (model.k3 - model.k2^2)^2 
end

function runExperiment(m, enzymes=Main.Banana_Models.ENZYMES)
    #="""
    model is a roadrunner object
    """=#
    model = te.loada(m)
    model.resetAll() # reset all
    s = model.simulate(0, Main.Banana_Models.TIME_TO_SIMULATE, Main.Banana_Models.N_DATAPOINTS) # simulate the trueModel
    ss = model.steadyState() # get the steadystate of the trueModel
    spConcs = model.getFloatingSpeciesConcentrations() # collect and store species concentrations (S2-S5)
    fluxes = model.getValue(model.getReactionIds()[1]) #, model.getValue(model.getReactionIds()[-1])]) # collect and store fluxes

    # create empty arrays to store data
    perturbationData = Array{Float64}(undef, length(enzymes), length(spConcs))     
    fluxData = []
    
    for (i, e) in enumerate(enzymes) # for the number of enzymes, 
        # model.resetAll() # reset all 
        model.setValue(e, 2) # redefine e
        ss = model.steadyState() # calculate new steadystate
        
        spConcs_e = model.getFloatingSpeciesConcentrations() # collect and store species concentrations (S2-S5)
        spfoldChange = (spConcs_e-spConcs)./spConcs
        perturbationData[i,:] = spfoldChange # species fold change

        fluxes_e = model.getValue(model.getReactionIds()[1]) #, model.getValue(model.getReactionIds()[-1])])
        fluxFoldChange = (fluxes_e-fluxes)./fluxes
        append!(fluxData, fluxFoldChange)

        model.setValue(e, 1)

    end

    allData = [reshape(perturbationData, length(perturbationData)); fluxData]
    # allData = np.append(allData, fluxes)

    return allData 
end
end