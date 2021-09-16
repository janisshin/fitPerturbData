from core import autoFit
from core import models
from core import backCheck

runID = models.makeFolder('data/',date = True)
autoFit.fitMultipleModels(100, folder=runID)
backCheck.getFoldChangeValues(data=runID+'/fittedParam.list', folder=runID)