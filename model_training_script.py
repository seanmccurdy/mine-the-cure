import subprocess
import os
import pandas as pd
import numpy as np
import time as t
from pandas import DataFrame,Series
from sklearn.metrics import accuracy_score
from sklearn.cross_validation import train_test_split
from keras.utils import np_utils
from mtc_library import *

#activates tensorflow backend for convnets
subprocess.call('KERAS_BACKEND=tensorflow python -c "from keras import backend; print (backend._BACKEND)"', shell=True)

"""
program needs these files to run:
/train_data
1) merge_arysm_sig_summary.csv
2) merge_arysm_sig_summary_supplement.csv
3) meta_master.csv
same directory as model_training_script
4) mtc_library.py
"""

################################################################################
################################################################################
################################################################################

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
low_freq_label_filter = y.isin(y.value_counts()[y.value_counts()>50].index.values)
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
print("xtrain shape:",x_train.shape,"ytrain shape:",y_train.shape);
print("xtest shape:",x_test.shape,"ytest shape:",y_test.shape);
print("xvalid shape:",x_valid.shape,"yvalid shape:",y_valid.shape);
print("preprocess complete...")
print()
print("building model...")

#train model
model = deep_learning_class_model(  num_inputs = x_train.shape[1],
                                    num_outputs = y_train.shape[1])

model.fit(x_train,
          y_train,
          nb_epoch = 100,
          batch_size = 100,
          verbose = 1,
          validation_data = (x_test,y_test))

print("model training complete...")
print("evaluating model performance...")

random_accuracy = model_accuracy_eval(  actual = y_train,
                                        pred = bootstrap_resample(y_train))

train_accuracy = model_accuracy_eval(   actual = y_train,
                                        pred = model.predict(x_train))

test_accuracy = model_accuracy_eval(    actual = y_test,
                                        pred = model.predict(x_test))

valid_accuracy = model_accuracy_eval(   actual = y_valid,
                                        pred = model.predict(x_valid))

print("random accuracy: {0:.2f}%".format(random_accuracy))
print("train accuracy: {0:.2f}%".format(train_accuracy))
print("test accuracy:  {0:.2f}%".format(test_accuracy))
print("valid accuracy: {0:.2f}%".format(valid_accuracy))

print("saving model architecture and weights...")

if not os.path.exists("model"):
    os.makedirs("model")
ver_num = str(len(os.listdir("model"))+1)
timestamp = str(t.strftime("%Y%m%d"))
model_filename = "V"+ver_num+"_"+timestamp+".h5"
model.save("model/"+model_filename)
print("program complete...")
