module Banana_Models

using PyCall
using Random
import Distributions: Uniform 

te = pyimport("tellurium")

import Dates

# the most basic model. 
groundTruth = (""" 
  \$S1 -> S2; k1*S1 - k2*S2
  S2 -> S3; k2*S2 - k3*S3
  S3 -> \$S4; k3*S3 - k4*S4
  S1 = 1; 
  k1 = 1; k2 = 2; k3 = 3; k4 = 4;
""")

# groundTruth model with enzyme terms
groundTruth_e = ("""
  R1: \$S1 -> S2; (e1) * (k1*S1 - k2*S2)
  R2: S2 -> S3; (e2) * (k2*S2 - k3*S3)
  R3: S3 -> \$S4; (e3) * (k3*S3 - k4*S4)
  S1 = 1; 
  k1 = 1; 
  k2 = 2; 
  k3 = 3; 
  k4 = 4; 
  e1 = 1; e2 = 1; e3 = 1; 
""") 

TIME_TO_SIMULATE = 100
N_DATAPOINTS = 100

# PARAMETERS = te.loada(groundTruth).getGlobalParameterIds() # parameters for groundTruth model

K_LIST = ["k1", "k2", "k3", "k4"]
ENZYMES = ["e1", "e2", "e3"] 

function generateModelFiles(n, folderName, groundTruthModel_string=groundTruth_e, parameters=K_LIST)
    #=
    generates n number of models that do not contain Keq terms
        
        Parameters
            n: int number of models desired by user
            groundTruthModel_string: Str from which to make random models
            parameters: Str list of k's
            knownValues: dict. contains parameter name followed by numerical value
            folderName: Str name of folder to place folder of model files in
        Returns: 
            List of Strings. Models are expressed in String form and have random values for parameters. 
    =#    
    # make a folder 
    folderName = makeFolder(folderName * "/banana_population")

    for number in 1:n
        randomModel = te.loada(groundTruthModel_string) # make a copy of the model 
        # set k values to random numbers 
        for p in parameters
            pValue = rand(Uniform(0, 10))
            randomModel.setValue(p, pValue) # redefine parameters
        end 
        fileName = folderName * "/antimonyModel_" * string(number) * ".txt"
        open(fileName, "w") do io
            write(io, randomModel.getCurrentAntimony())
        end
    end
    return folderName
end

# check if folder exists; if not, make a new folder
function makeFolder(folderName::String, date::Bool=false)
    #="""
    Returns
        numbered_folderName: Str
    """=#
    i = 1

    if date
        now = Dates.now() # current date and time
        folderName = folderName * Dates.format(now, "yyyymmdd")
    end
    
    numbered_folderName = folderName * "_" * string(i, base = 10, pad=1)
    if ! isdir(numbered_folderName)
        mkdir(numbered_folderName)
        return numbered_folderName
    end
    while isdir(numbered_folderName)
        i += 1
        numbered_folderName = folderName * "_" * string(i, base = 10, pad=1)
    end
    mkdir(numbered_folderName)
    return numbered_folderName

end

end