# importing experiment data
from psychopy.misc import fromFile
import numpy as np
dirs = "/home/rubi/Documents/psychopy/typing_task/data/"
datFile = fromFile(dirs+'rubi3_typingtask_2020_Nov_30_0949.psydat')

# for trialHandler data
trialHandler = datFile.loops[0]
# see list of trialHandler parameters
trialHandlerParams = dir(datFile.loops[0])
# View data
print(trialHandler.data)

