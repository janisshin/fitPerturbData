import tellurium as te

from core import genAlgo_MMARL
from core import models
from core import backCheck

modelMenu = dict({'groundTruth': models.groundTruth, 
                'groundTruth_e': models.groundTruth_e, 
                'groundTruth_mod': models.groundTruth_mod,
                'groundTruth_mod_e': models.groundTruth_mod_e,
                'groundTruth_MM': models.groundTruth_MM,
                'groundTruth_MM_e': models.groundTruth_MM_e,

                'K_LIST': models.K_LIST,
                'Km_LIST': models.Km_LIST
                })


# configure run
modeltype='groundTruth_MM_e'
p = 'Km_LIST'
sr = (2,9) # survivor ratio
n_individuals=sr[0] + sr[1]
maxGen = 10
lr = 0.2 # learning rate
omit=None
refinement=False

runID = models.makeFolder('data/',date = True)
# runID = 'data/20210920_1' # for refining

# make a run report
with open(runID + "/protocol.txt","a") as f:
    f.write(f"model type: {modeltype}" + '\n')
    f.write(f"parameters: {p}" + '\n')
    f.write(f"survivorRatio: {sr}" + '\n')
    f.write(f"learning rate: {lr}" + '\n')
    f.write(f"omitted positions: {omit}" + '\n')
    f.write(f"refinement: {refinement}" + '\n\n')

    
if refinement:
    genAlgo_MMARL.runGeneticAlgorithm(runID+'/genAlgo_population_1', 
                                    gt=modelMenu[modeltype], parameters=modelMenu[p], 
                                    survivorRatio=sr, lastGeneration=maxGen, tolerance=0.001, 
                                    runID=runID, omit=omit, lr=lr)
else: 
    # to run Michaelis-Menten model
    populationFolder = models.generateModelFiles(n_individuals, 
                                                    groundTruthModel_string=modelMenu[modeltype], 
                                                    parameters=modelMenu[p], folderName=runID)
    # populationFolder = runID + '/genAlgo_population_1'

    genAlgo_MMARL.runGeneticAlgorithm(populationFolder, gt=modelMenu[modeltype],
                                    parameters=modelMenu[p], survivorRatio=sr, lastGeneration=maxGen, 
                                    tolerance=0.01, runID=runID, omit=omit, lr=lr)
    
    # print params and scores to files
    backCheck.extractParams(populationFolder, modelMenu[p], modelMenu[modeltype], folderName=runID,
                            omit=omit)
    
    backCheck.getFoldChangeValues(testModel=te.loada(modelMenu[modeltype]), 
                                    parameters=modelMenu[p], data=runID + '\paramData.list', 
                                    folder=runID, n_individuals=n_individuals)

