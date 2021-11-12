# install and import PyCall
# using Pkg
# Pkg.add("PyCall")
using PyCall

# np = pyimport("numpy")
te = pyimport("tellurium")
# random = pyimport("random")
dt = pyimport("datetime")

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

TIME_TO_SIMULATE = 100
N_DATAPOINTS = 100

PARAMETERS = te.loada(groundTruth).getGlobalParameterIds() # parameters for groundTruth model

K_LIST = ["k1", "k2", "k3", "k4", "k5"]
Km_LIST = ["Km1", "Km2", "Km3", "Km4", "Km5", "Km6","Km7","Km8","Km9","Km10"]
ENZYMES = ["e1", "e2", "e3", "e4", "e5"]



function generateModelFiles(n, groundTruthModel_string=groundTruth_e, parameters=PARAMETERS, folderName=nothing)
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
    if folderName === nothing
        folderName = makeFolder("genAlgo_population")
    else
        folderName = makeFolder(folderName + "/genAlgo_population")
    end

    for number in range(n)
        randomModel = te.loada(groundTruthModel_string) # make a copy of the model 
        # set k values to random numbers 
        for p in parameters
            randomModel.setValue(p, pValue) # redefine parameters
        end 
        fileName = folderName + "/antimonyModel_" + str(number) + ".txt"
        open(fileName, "w") do io
            write(io, randomModel.getCurrentAntimony())
        end;
    end
    return folderName
end

# check if folder exists; if not, make a new folder
function makeFolder(folderName, date=False)
    """
    Returns
        numbered_folderName: Str
    """
    i = 1

    if date
        now = dt.datetime.now() # current date and time
        folderName = folderName + now.strftime("%Y%m%d")
    end
    numbered_folderName = folderName + "_" + string(i, base = 10, pad=3)
    if ! isdir(numbered_folderName)
        mkdir(numbered_folderName)
        return numbered_folderName
    end
    while isdir(numbered_folderName)
        i += 1
        numbered_folderName = folderName + "_" + string(i, base = 10, pad=3)
    end
    mkdir(numbered_folderName)
    return numbered_folderName

end