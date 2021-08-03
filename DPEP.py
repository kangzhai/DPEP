# DPEP for predicting plant miRNA-lncRNA interaction

import numpy as np
import math
from Path import PathInput, PathOutput
from DataProcessing import PairConstruction, FusionComplexFeature, ConvertToMatrix, ConvertToVector
from PredictionProcessing import LoadBaseModel, LoadDecisionModel, SemiDynamicMechanism, ConvertLabel

# Load data
PathmiRNA, PathlncRNA = PathInput()
ListmiRNA = open(PathmiRNA, 'r').readlines()
ListlncRNA = open(PathlncRNA, 'r').readlines()
print('Data Loading Complete')
# Construct miRNA-lncRNA pair
ListPair = PairConstruction(ListmiRNA, ListlncRNA)
print('Pair Construction Complete')
# Extract features and construct complex feature
ListOriginalComplexFeatureVector, ListBriefComplexFeatureVector = FusionComplexFeature(ListPair)
print('Feature Extraction and Complex Feature Vector Construction Complete')
# Format brief complex feature vector
X_test_b = ConvertToVector(ListBriefComplexFeatureVector)
# Convert original complex feature vector to matrix
X_test_o = ConvertToMatrix(ListOriginalComplexFeatureVector, 4)
print('Vector Format and Matrix Conversion Complete')
# Dual-path parallel ensemble pruning method
Species = ['1', '2', '3', '4', '5', '6']
NumTestSample = len(ListPair)
PruningVector = np.zeros(6)
ScoreMatrix = np.zeros((NumTestSample, 6))
Output = []
for it in range(10): # 10 independent predictions
    for t in range(6): # 6 species data for training
        # Load decision model
        DecisionModel = LoadDecisionModel(Species[t])
        # Decision model prediction
        DecisionLabel = DecisionModel.predict(X_test_b)
        # Semi-dynamic mechanism
        PruningLabel = SemiDynamicMechanism(DecisionLabel, NumTestSample)
        # Combine into Pruning Vector
        PruningVector[t] = PruningLabel
        # Load base model
        BaseModel = LoadBaseModel(Species[t], it)
        # Base model prediction
        ScoreVector = BaseModel.predict(X_test_o)
        ScoreVector = ScoreVector[:, 1]
        # Combine into score matrix
        ScoreMatrix[:, t] = ScoreVector
    if PruningVector.sum() == 0:
        PruningVector = np.ones(6)
    EnsembleScoreVector = np.dot(ScoreMatrix, PruningVector) / PruningVector.sum()
    # Add label
    FinalLabel = ConvertLabel(EnsembleScoreVector, ListPair, it)
    Output += FinalLabel
    print('The ' + str(it + 1) + ' st/nd/rd/th Independent Prediction Complete')
print('The predicted results have been output!')
PathResult = PathOutput()
w = open(PathResult, 'w')
w.writelines(Output)
w.close()
