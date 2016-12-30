import subprocess
import os
import sys
import pandas as pd
import numpy as np
import time as t
from pandas import DataFrame,Series
from sklearn.metrics import accuracy_score,precision_score
from sklearn.cross_validation import train_test_split
from keras.utils import np_utils
from mtc_library import *

#activates tensorflow backend (faster than theano)
subprocess.call('KERAS_BACKEND=tensorflow python -c "from keras import backend; print (backend._BACKEND)"', shell=True)

"""
program needs these files to run:

/train_data
1) merge_arysm_sig_summary.csv (arysm normalized data)
2) merge_arysm_sig_summary_supplement.csv (added arysm normalized data)
3) meta_master.csv (meta data on training data)

same directory as model_training_script
4) mtc_library.py (settings and model archectiture)

"""

print()
print("libraries and functions loaded...")

data2 = pd.read_csv("train_data/merge_arysm_sig_summary.csv",
                    encoding = "latin1",
                    index_col = 1).iloc[:,1:]

print("imported train data...")

data = pd.read_csv( "train_data/merge_arysm_sig_summary_supplement.csv",
                    encoding = "latin1",
                    index_col = 1).iloc[:,1:]

print("imported train data supplment...")

#removes columns with null values, some column names have weird characters
merged_data = pd.concat([data2, data],
                        axis = 0,
                        ignore_index = False)

merged_data.dropna( axis = 1,
                    inplace = True)

meta = pd.read_csv("train_data/meta_master.csv")
meta.index = meta.geo_id
print("imported meta data...")

y = meta.loc[merged_data.index.values].path_simple #keeps same order as transcriptome data
x = merged_data
x.index = merged_data.index.values
low_freq_label_filter = y.isin(y.value_counts()[y.value_counts()>40].index.values)
y = y[low_freq_label_filter]
x = x[low_freq_label_filter]
x = x.as_matrix() #input x must be a numpy array for the classifier

#convert to one hot encoding for target variable
y_factorized = y.factorize()
y_onehot = np_utils.to_categorical(y_factorized[0],len(y_factorized[1]))


# performs train test valid split on x,y, and labels
x_train,x_test,y_train,y_test,labels_train,labels_test = train_test_split( x,
                                                                           y_onehot,
                                                                           y.index.values,
                                                                           test_size = 0.4,
                                                                           random_state = seed)

x_test,x_valid,y_test,y_valid,labels_test,labels_valid = train_test_split( x_test,
                                                                           y_test,
                                                                           labels_test,
                                                                           test_size = 0.50,
                                                                           random_state = seed)

#confirms appropriate train/test split
print()
print("xtrain shape:",x_train.shape,"ytrain shape:",y_train.shape);
print("xtest shape:",x_test.shape,"ytest shape:",y_test.shape);
print("xvalid shape:",x_valid.shape,"yvalid shape:",y_valid.shape);
print()
print("preprocess complete...")
print()
print("building model...")
print()

#train model
model = deep_learning_class_model(num_inputs = x_train.shape[1],
                                  num_outputs = y_train.shape[1])

model.fit(x_train,
          y_train,
          nb_epoch = 200,
          batch_size = 100,
          verbose = 1,
          validation_data = (x_test,y_test))

print()
print("model training complete...")
print("evaluating model performance...")

random_accuracy = accuracy_score(y_true = y_train.argmax(axis=1),
                                 y_pred = bootstrap_resample(y_train).argmax(axis=1))

train_accuracy = accuracy_score(y_true = y_train.argmax(axis=1),
                                y_pred = (model.predict(x_train)).argmax(axis=1))

test_accuracy = accuracy_score(y_true = y_test.argmax(axis=1),
                               y_pred = (model.predict(x_test)).argmax(axis=1))

valid_accuracy = accuracy_score(y_true = y_valid.argmax(axis=1),
                                y_pred = (model.predict(x_valid)).argmax(axis=1))

random_precision = precision_score(y_true = y_train.argmax(axis=1),
                                  y_pred = bootstrap_resample(y_train).argmax(axis=1),
                                  average = "weighted")

train_precision = precision_score(y_true = y_train.argmax(axis=1),
                                  y_pred = (model.predict(x_train)).argmax(axis=1),
                                  average = "weighted")

test_precision = precision_score(y_true = y_test.argmax(axis=1),
                                 y_pred = (model.predict(x_test)).argmax(axis=1),
                                 average = "weighted")

valid_precision = precision_score(y_true = y_valid.argmax(axis=1),
                                  y_pred = (model.predict(x_valid)).argmax(axis=1),
                                  average = "weighted")

#feature/output labels
Series(y_factorized[1]).to_csv("output_labels.csv",
                               index= False)

Series(merged_data.columns.values).to_csv("feature_labels.csv",
                                          index= False)

print("generating report...")

if not os.path.exists("model"):
    os.makedirs("model")

ver_num = str(len(os.listdir("model"))+1)
timestamp = str(t.strftime("%Y%m%d"))
model_filename = "V"+ver_num+"_"+timestamp

if not os.path.exists("reports"):
    os.makedirs("reports")

temp = sys.stdout
sys.stdout = open("reports/"+model_filename+".txt", 'w')
print("Algorithm: ","V"+ver_num)
print("Date: ",str(t.strftime("%Y-%m-%d")))
print()
print("Function: Outputs the probability of various diseases given gene expression data")
print("Sample Type:  Human Patient Samples")
print("Conditions Evaluated: ",y_valid.shape[1])
print()
print("-----------Statistics------------")
print()
print("Train Size: ",x_train.shape[0])
print("Test Size: ",x_test.shape[0])
print("Validation Size:",x_valid.shape[0])
print()
print("Bootstrapped Accuracy:  {0:.3f}".format(random_accuracy))
print("Train Accuracy:         {0:.3f}".format(train_accuracy))
print("Test Accuracy:          {0:.3f}".format(test_accuracy))
print("Validation Accuracy:    {0:.3f}".format(valid_accuracy))
print()
print("Bootstrapped Precision: {0:.3f}".format(random_precision))
print("Train Precision:        {0:.3f}".format(train_precision))
print("Test Precision:         {0:.3f}".format(test_precision))
print("Validation Precision:   {0:.3f}".format(valid_precision))
print()
print("Notable Sample Sources: GTeX, TCGA, ADNI, ArrayExpress, Gene Expression Omnibus (GEO)")
sys.stdout.close()
sys.stdout = temp

print("saving model architecture and weights...")
model.save("model/"+model_filename+".h5")
print("model"+model_filename+".h5 saved...")
print("program complete...")
