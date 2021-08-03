# Model process

import numpy as np
from keras.models import load_model
from sklearn.externals import joblib

def LoadBaseModel(species, it):
    basemodel = load_model('BaseModel\\BM' + species + str(it) + '.h5')
    return basemodel

def LoadDecisionModel(species):
    decisionmodel = joblib.load('DecisionModel\\DM' + species + '.pkl')
    return decisionmodel

def SemiDynamicMechanism(labelvector, numtestsample):
    numberselectedsample = labelvector.sum()
    pruninglabel = 1 if numberselectedsample > numtestsample / 2 else 0
    return pruninglabel

def ConvertLabel(EnsembleScoreVector, ListPair, it):
    FinalLabel = []
    FinalLabel.append('The ' + str(it + 1) + ' st/nd/rd/th independent prediction result \n')
    for indresult in range(len(EnsembleScoreVector)):
        Sample = ListPair[indresult]
        miRNAname, lncRNAname, miRNAsequence, lncRNAsequence, miRNAstructure, lncRNAstructure = Sample.split(',')
        score = EnsembleScoreVector[indresult]
        if score >= 0.5:
            StrResult = miRNAname + ',' + lncRNAname + ',' + ',' + str(score) + ',' + 'Interaction\n'
        else:
            StrResult = miRNAname + ',' + lncRNAname + ',' + ',' + str(score) + ',' + 'Non-Interaction\n'
        FinalLabel.append(StrResult)
    FinalLabel.append('\n')
    return FinalLabel