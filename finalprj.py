# -*- coding: utf-8 -*-
"""
Created on Sun May 21 19:51:19 2017

@author: Yi-hao, Mo
"""

import numpy as np
import pandas as pd
#from sklearn import naive_bayes as nb
#import matplotlib.pyplot as plt

class naive_bayes:
    def fit(self, data, target, smoothing=False, k=3, f_domain=None,c_domain=None):
        dataset = pd.DataFrame(data.copy())
        num_feature = len(dataset.axes[1])
        if c_domain == None:
            p = dict()
            p_cond = dict()
        else:
            p = c_domain.copy()
            p_cond = c_domain.copy()
        for x in pd.unique(target):
            p[x] = target.count(x)/len(dataset)
            temp_list = []
            for y in range(num_feature):
                domain = pd.unique(dataset[y])
                if f_domain == None:
                    temp = dict()
                else:
                    temp = f_domain[y].copy()
                base = 0
                for z in domain:
                    temp[z] = 0
                for z in range(len(dataset)):
                    if target[z] == x:
                        temp[dataset.get_value(z,y)] += 1
                        base += 1
                for z in temp.keys():
                    #print(str(y)+' '+z+' sum: '+str(temp[z])+' base: '+str(base)+' domain: '+str(len((domain))))
                    if smoothing:
                        temp[z] = (temp[z]+k)/(base+k*len(domain))
                    else:
                        temp[z] /= base
                temp_list.append(temp)
            p_cond[x] = temp_list
        self.p = p
        self.p_cond = p_cond
    def predict(self, query):
        estimate_p = 0
        num = len(query)
        e_list = []
        e_value = []
        for w in range(num):
            for x in self.p.keys():
                temp = 1
                for y in self.p_cond[x]:
                    temp *= y[query[w][self.p_cond[x].index(y)]]
                temp *= self.p[x]
                if temp > estimate_p:
                    estimate_p = temp
                    estimate = x
            e_value.append(estimate_p)
            e_list.append(estimate)
        self.est_prob = e_value
        return e_list
    def get_predict_prob(self):
        return self.est_prob
    def get_p_cond(self):
        return self.p_cond
    def clear(self):
        self.p=None
        self.p_cond=None
        self.est_prob=None
###############################################################################
#read file
fp = open("agaricus-lepiota.data")
data = []
target = []
for x in fp.readlines():
    x = x.strip('\n')
    data.append(x.split(sep=',')[1:])
    target.append(x.split(sep=',')[0])
fp.close()
fp = open("attr.txt")
domain = []
flag = False
for x in fp.readlines():
    temp = dict()
    if 'class' in x:
        cdomain = dict()
        for y in x.strip().split(sep=':')[-1].split(sep=','):
            cdomain[y] = list()
        continue
    for y in x.strip().split(sep=','):
        temp[y] = 0
    domain.append(temp)
fp.close()

###############################################################################
#replace missing value by most value
temp = pd.DataFrame(data)
most = []
for x in range(len(data[0])):#find the most value in each feature
    sdomain = pd.unique(temp[x])
    value = 0
    for y in sdomain:
        if value < list(temp[x]).count(y):
            value = list(temp[x]).count(y)
            m = y
    most.append(m)
for x in data:#handle missing value
    for y in range(len(x)):
        if x[y] == '?':
            data[data.index(x)][y] = most[y]
###############################################################################

test = naive_bayes()
'''
test.fit(data,target,smoothing=False,f_domain=domain,c_domain=cdomain)
#print(test.get_p_cond())
e = test.predict([['x','s','n','t','p','f','c','n','k','e','e','s','s','w','w','p','w','o','p','k','s','u']])
print(e)
test.clear()
test.fit(data,target,smoothing=True,f_domain=domain,c_domain=cdomain)
#print(test.get_p_cond())
e = test.predict([['x','s','n','t','p','f','c','n','k','e','e','s','s','w','w','p','w','o','p','k','s','u']])
print(e)
'''

stp = 0
sfp = 0
stn = 0
sfn = 0

num = len(data)
for x in range(0,5):
    test.clear()
    test.fit(data[0:x*num//5] + data[(x+1)*num//5:]
        ,target[0:x*num//5] + target[(x+1)*num//5:]
        ,smoothing=True
        ,k=25
        ,f_domain=domain
        ,c_domain=cdomain)
    result = test.predict(data[x*num//5:(x+1)*num//5])
    tp = 0
    fp = 0
    tn = 0
    fn = 0
    for y in range(len(result)):
        temp = target[x*num//5:(x+1)*num//5]
        if result[y] == temp[y]:
            if temp[y] == pd.unique(target)[0]:
                tp += 1#poision
            else:
                tn += 1#edible
        else:
            if temp[y] == pd.unique(target)[0]:
                fn += 1
            else:
                fp += 1
    
    print("\tPrediction")
    print("\t" + pd.unique(target)[0] + "\t" +pd.unique(target)[1])
    print(pd.unique(target)[0] + "\t" + str(tp) + "\t" +str(fn))
    print(pd.unique(target)[1] + "\t" + str(fp) + "\t" +str(tn))
    #print(test.p_cond)
    #print(test.p)
    stp += tp
    stn += tn
    sfp += fp
    sfn += fn
    
#print("Accuracy: "+str((stp+stn)/(stp+stn+sfp+sfn)))
    
