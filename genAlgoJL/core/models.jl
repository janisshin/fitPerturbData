module Models

using PyCall
using Random
import Distributions: Uniform 

te = pyimport("tellurium")

import Dates

# the most basic model. 
groundTruth = (""" 
  \$S1 -> S2; k1*S1 - k2*S2
  S2 -> S3; k2*S2 - k3*S3
  S3 -> S4; k3*S3 - k4*S4
  S4 -> S5; k4*S4 - k5*S5
  S5 -> \$S6; k5*S5 - k6*S6
  S1 = 1; 
  k1 = 1; k2 = 2; k3 = 3; k4 = 4; k5 = 5; k6 = 6; 
""")
groundTruth_e = (""" 
  \$S1 -> S2; e1 * k1*S1 - k2*S2
  S2 -> S3; e2 * k2*S2 - k3*S3
  S3 -> S4; e3 * k3*S3 - k4*S4
  S4 -> S5; e4 * k4*S4 - k5*S5
  S5 -> \$S6; e5 * k5*S5 - k6*S6
  S1 = 1; 
  k1 = 1; k2 = 2; k3 = 3; k4 = 4; k5 = 5; k6 = 6; 
  e1 = 1; e2 = 1; e3 = 1; e4 = 1; e5 = 1;
""")

# Michaelis-Menten model
groundTruth_MM = ("""
  v1: \$S1 -> S2; Vm1/Km1*(S1 - S2/Keq1)/(1 + S1/Km1 + S2/Km2)
  v2: S2 -> S3; Vm2/Km3*(S2 - S3/Keq2)/(1 + S2/Km3 + S3/Km4)
  v3: S3 -> S4; Vm3/Km5*(S3 - S4/Keq3)/(1 + S3/Km5 + S4/Km6)
  v4: S4 -> S5; Vm4/Km7*(S4 - S5/Keq4)/(1 + S4/Km7 + S5/Km8)
  v5: S5 -> \$S6; Vm5/Km9*(S5 - S6/Keq5)/(1 + S5/Km9 + S6/Km10)
  S1 = 1; S2 = 0.1; S3 = 0.1; S4 = 0.1; S5 = 0.1;
  Km1 = 0.51; Km2 = 0.62; Km3 = 0.93; Km4 = 1.4; Km5 = 2.5; 
  Km6 = 2.6; Km7 = 3.51; Km8 = 2.62; Km9 = 3.93; Km10 = 4.4;
  Keq1 = 3; Keq2 = 3; Keq3 = 3; Keq4 = 3; Keq5 = 3; 
  Vm1 = 1; Vm2 = 2; Vm3 = 4; Vm4 = 5; Vm5 = 7; 
""")

# Michaelis-Menten model with e 
groundTruth_MM_e = ("""
  v1: \$S1 -> S2; e1 * Vm1/Km1*(S1 - S2/Keq1)/(1 + S1/Km1 + S2/Km2)
  v2: S2 -> S3; e2 * Vm2/Km3*(S2 - S3/Keq2)/(1 + S2/Km3 + S3/Km4)
  v3: S3 -> S4; e3 * Vm3/Km5*(S3 - S4/Keq3)/(1 + S3/Km5 + S4/Km6)
  v4: S4 -> S5; e4 * Vm4/Km7*(S4 - S5/Keq4)/(1 + S4/Km7 + S5/Km8)
  v5: S5 -> \$S6; e5 * Vm5/Km9*(S5 - S6/Keq5)/(1 + S5/Km9 + S6/Km10)
  S1 = 1; S2 = 0.1; S3 = 0.1; S4 = 0.1; S5 = 0.1; S6 = 0.1;
  Km1 = 0.51; Km2 = 0.62; Km3 = 0.93; Km4 = 1.4; Km5 = 2.5; 
  Km6 = 2.6; Km7 = 3.51; Km8 = 2.62; Km9 = 3.93; Km10 = 4.4;
  Keq1 = 3; Keq2 = 3; Keq3 = 3; Keq4 = 3; Keq5 = 3; 
  e1 = 1; e2 = 1; e3 = 1; e4 = 1; e5 = 1;
  Vm1 = 1; Vm2 = 2; Vm3 = 4; Vm4 = 5; Vm5 = 7; 
""")

TIME_TO_SIMULATE = 100
N_DATAPOINTS = 100

K_LIST = ["k1", "k2", "k3", "k4", "k5"]
KM_LIST = ["Km1", "Km2", "Km3", "Km4", "Km5","Km6", "Km7", "Km8", "Km9", "Km10"]
ENZYMES = ["e1", "e2", "e3", "e4", "e5"]

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
    folderName = makeFolder(folderName * "/population")

    for number in 1:n
        randomModel = te.loada(groundTruthModel_string) # make a copy of the model 
        # set k values to random numbers 
        for p in parameters
            pValue = rand(Uniform(0, 1000))
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