#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

sys.path.append("../tools/")
from email_preprocess import preprocess
from time_utils import TimeMeasuring


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


#########################################################
### your code goes here ###
features_train = features_train[:len(features_train)/100]
labels_train = labels_train[:len(labels_train)/100]

clf = SVC(kernel='rbf', C=10000)

print 'starting fit'

fit_time = time()
clf.fit(features_train, labels_train)
TimeMeasuring.print_fit_time(fit_time)

print 'starting predict'

predict_time = time()
pred = clf.predict(features_test)
TimeMeasuring.print_prediction_time(predict_time)

print "Accuracy: ", accuracy_score(labels_test, pred, normalize=True)

chris = 0
for l in pred:
    if l == 1:
        chris = chris + 1

print "chris: ", chris


#########################################################


