module Models

using RoadRunner
using Random
import Distributions: Uniform 
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

K_LIST = ["k1", "k2", "k3", "k4", "k5"]
KM_LIST = ["Km1", "Km2", "Km3", "Km4", "Km5","Km6", "Km7", "Km8", "Km9", "Km10"]
ENZYMES = ["e1", "e2", "e3", "e4", "e5"]

K_LIST_putida = ["Km","Km1","Km3","Km5","Km7","Km9","Km11","Km13","Km15","Km17","Km19","Km20","Km21","Km22","Km23","Km24","Km25","Km26","Km27","Km28","Km29","Km30","Km31","Km32","Km33","Km34","Km35","Km36","Km37","Km38","Km39","Km40","Km41","Km42","Km43","Km44","Km47","Km48","Km49","Km50","Km51","Km52","Km53","Km54","Km55","Km56","Km57","Km58","Km59","Km60","Km61","Km62","Km63","Km64","Km65","Km66","Km67","Km68","Km69","Km70","Km71","Km72","Km73","Km74","Km75","Km76","Km77","Km78","Km79","Km80","Km81","Km82","Km83","Km84","Km85","Km86","Km87","Km88","Km89","Km90","Km91","Km92","Km93","Km94","Km95","Km96","Km97","Km98","Km99","Km100","Km101","Km102","Km103","Km104","Km105","Km106","Km107","Km108","Km109","Km110","Km111","Km112","Km113","Km114","Km115","Km116","Km117","Km118","Km119","Km120","Km121","Km122","Km123","Km124","Km125","Km126","Km129","Km130","Km131","Km132","Km133","Km134","Km135","Km136","Km137","Km138","Km139","Km140","Km143","Km144","Km145","Km146","Km147","Km148","Km149","Km150","Km151","Km152","Km153","Km154","Km155","Km156","Km157","Km158","Km159","Km160"]
# 78 total enzymes
ENZYMES_putida = ["e1","e2","e3","e4","e5","e6","e7","e8","e9","e10","e11","e12","e13","e14","e15","e16","e17","e18","e19","e20","e21","e22","e23","e25","e26","e27","e28","e29","e30","e31","e32","e33","e34","e35","e36","e37","e38","e39","e40","e41","e42","e43","e44","e45","e46","e47","e48","e49","e50","e51","e52","e53","e54","e55","e56","e57","e58","e59","e60","e61","e62","e63","e64","e66","e67","e68","e69","e70","e71","e73","e74","e75","e76","e77","e78","e79","e80","e81"]

function generateModelFiles(n, folderName, makeFolder=true, groundTruthModel_File=nothing, parameters=K_LIST_putida)
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
    if makeFolder
        folderName = makeFolder(folderName * "/population")
    end

    rr = RoadRunner.createRRInstance()

    io = open(groundTruthModel_File)
    RoadRunner.loadSBML(rr, read(io, String)) 
    close(io)
    
    for number in 1:n
        
        # set k values to random numbers 
        for p in parameters
            pValue = rand(Uniform(0.1, 1))
            RoadRunner.setValue(rr, p, pValue) # redefine parameters
        end 
        fileName = folderName * "/SBMLModel_" * string(number, base = 10, pad=1) * ".xml"
        open(fileName, "w") do io
            write(io, RoadRunner.getCurrentSBML(rr))
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