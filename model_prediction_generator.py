import subprocess as sp
import os
import sys
import pandas as pd
import numpy as np
import time as t
from pandas import DataFrame,Series
from keras.models import load_model

filename = str(sys.argv[1])
filemodel = str(sys.argv[2])

#activates tensorflow backend for convnets
sp.call('KERAS_BACKEND=tensorflow python -c "from keras import backend; print (backend._BACKEND)"', shell = True)
print("running normaliazation program...")
sp.call('/usr/local/bin/Rscript sig_score_processing.R ' + filename, shell = True)

print("loading input data...")
model = load_model(filemodel)
data = pd.read_csv("output_sig_summary.csv",
                   encoding = "latin1",
                   index_col = 0)

xlabel = pd.read_csv("feature_labels.csv",
                     header = -1,
                     squeeze = True)

ylabel = pd.read_csv("output_labels.csv",
                     header = -1,
                     squeeze = True)

labels = data.index.values

print("generating predictions...")
predictions = DataFrame(model.predict(data.ix[:,xlabel.tolist()].as_matrix()),
                        index = labels,
                        columns = ylabel.tolist())

print("saving predictions...")
predictions.to_csv("model_predictions.csv")
print("program complete...")
