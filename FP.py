import numpy as np
import pandas as pd
import csv
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_val_predict
from sklearn import tree




dataset = np.genfromtxt('agaricus-lepiota.data.txt', delimiter=",",dtype='str')
attribute = dataset[:,1:22]
target = dataset[:,0]

#import data and seperate attributes/targets
###############################################

size=attribute.shape[0]
print(target.shape)
attribute_int=np.zeros((size,attribute.shape[1]),int)
target_int=np.zeros(size)

for x in range (0,size,1):
    for y in range (0,attribute.shape[1],1):
        attribute_int[x][y]=ord(attribute[x][y])

for x in range (0,size,1):
    target_int[x]=ord(target[x])


#convert string data into interger data
###############################################



print("\nK-fold cross validation (pre-pruning depth<3)")
print("\n[K-Fold K=5]")

kf2= KFold(n_splits=5, shuffle=True)
normal= []
#set 5-fold cross validation
###############################################

for train, test in kf2.split(attribute_int, target_int):
    # run 5 times in 5-fold cross validation, with train/test
    ###############################################

    dtc= tree.DecisionTreeClassifier(max_depth=5)
    r= dtc.fit(attribute_int[train], target_int[train])
    #pre-pruning tree with max-depth=5
    ###############################################

    score = r.score(attribute_int[test], target_int[test])
    normal.append(score)
    pred= dtc.predict(attribute_int[test])
    print(pred)
    cnf= confusion_matrix(target_int[test], pred)
    print(cnf)
    #print predict target and confusion matrix
    ###############################################

print("|||||||||||||||||||||||||||")
print("Overall Classification accuracy= ", np.asarray(normal).mean())
#calculate accuracy
###############################################



