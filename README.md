# DPEP
The related data and scoure codes of DPEP are provided by Q. Kang.

The latest version is updated on August 3, 2021.

# Introduction
DPEP is a novel ensemble pruning protocol for predicting plant miRNA-lncRNA interactions. It adaptively prunes the base models based on dual-path parallel ensemble method to meet the challenge of cross-species prediction. It is effective for mining endogenous target mimics. 

# Dependency
Windows operating system

Python 3.6.5

Kreas 2.2.4

# Details
### BaseModel folder
60 trained base models. BM11 indicates the 1st based model trained by Training set 1. The other base models use the same naming rule. The details of training sets are shown in our paper.

### DecisionModel folder
6 decision base models. DM1 indicates the decision model trained by Decision training set 1. The other decision models use the same naming rule. The details of decision training sets are shown in our paper.

### Example folder
The examples of input. This input format can't be changed, otherwise it may cause the program error. This format can be obtained directly by using RNAfold (a RNA secondary structure extraction tool) in ViennaRNA package. The latest version of ViennaRNA package can be also downloaded from https://www.tbi.univie.ac.at/RNA/.

### Path.py
Paths of input and output.

### DataProcessing.py
Function of data processing.

### PredictionProcessing.py
Function of prediction process.

### DPEP.py
Code for predicting whether there has been interaction in unlabeled miRNA-lncRNA pairs.

# Usage
Open the console or powershell in the local folder and copy the following commands to run DPEP. It is also feasible to run the codes using python IDE (such as pyCharm).

Command: python DPEP.py

Explanation:

It can predict whether there has been interaction in the unlabeled miRNA-lncRNA pairs. It can quickly predict large-scale interactions by loading and integrating the trained base models. The users can adjust the path of input and output in "Path.py" to realize the prediction of local data. The input format must be consistent with that in the "Example" folder. This input format can be obtained directly through RNAfold in ViennaRNA package. The output is the predicted results, which lists miRNA name, lncRNA name, ensemble score and interaction/non-interaction. We will add more predicted information in future versions. To show the authenticity of the codes, we provide all 10 groups of base models mentioned in the paper. By default, 10 groups of base models independently predict the unlabeled samples and output the results. Due to the differences between the base models, the 10 groups of results will also vary. Users can comprehensively refer to these results, or manually adjust to use a group of base models for prediction. We will also integrate these results in future versions.

# Reference
If you use the codes, please cite the reference as below.

The paper has been submitted, please wait for updating.
