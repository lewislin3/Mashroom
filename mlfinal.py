from sklearn.neighbors import KNeighborsClassifier
import csv
from sklearn.metrics import confusion_matrix
import numpy as np

def dict(alpha,lock):
    if alpha=='a':
        return '0'
    elif alpha=='b':
        return '1'
    elif alpha=='c':
        return '2' 
    elif alpha=='d':
        return '3'
    elif alpha=='e':
        return '4'
    elif alpha=='f':
        return '5'
    elif alpha=='g':
        return '6'
    elif alpha=='h':
        return '7'
    elif alpha=='i':
        return '8'
    elif alpha=='j':
        return '9'
    elif alpha=='k':
        return '10'
    elif alpha=='l':
        return '11'
    elif alpha=='m':
        return '12'
    elif alpha=='n':
        return '13'
    elif alpha=='o':
        return '14'
    elif alpha=='p':
        return '15'
    elif alpha=='q':
        return '16'
    elif alpha=='r':
        return '17'
    elif alpha=='s':
        return '18'
    elif alpha=='t':
        return '19'
    elif alpha=='u':
        return '20'
    elif alpha=='v':
        return '21'
    elif alpha=='w':
        return '22'
    elif alpha=='x':
        return '23'
    elif alpha=='y':
        return '24'
    elif alpha=='z':
        return '25'
    else:
        return '26'
    


def cross_validation(mushroom_X,mushroom_Y,neigh):
    mushroom_X1=[]
    mushroom_Y1=[]
    mushroom_X2=[]
    mushroom_Y2=[]
    mushroom_X3=[]
    mushroom_Y3=[]
    mushroom_X4=[]
    mushroom_Y4=[]
    mushroom_X5=[]
    mushroom_Y5=[]
    mushroom_X6=[]
    mushroom_Y6=[]
    mushroom_X7=[]
    mushroom_Y7=[]
    mushroom_X8=[]
    mushroom_Y8=[]
    mushroom_X9=[]
    mushroom_Y9=[]
    mushroom_X10=[]
    mushroom_Y10=[]
    
    for i in range(1200):
        mushroom_X1.append(mushroom_X[i])
        mushroom_Y1.append(mushroom_Y[i])
    for i in range(844):
        mushroom_X5.append(mushroom_X[i+4800])
        mushroom_Y5.append(mushroom_Y[i+4800])
    for i in range(1200):
        mushroom_X1.append(mushroom_X[i+1200])
        mushroom_Y1.append(mushroom_Y[i+1200])
    for i in range(1200):
        mushroom_X1.append(mushroom_X[i+2400])
        mushroom_Y1.append(mushroom_Y[i+2400])
    for i in range(1200):
        mushroom_X1.append(mushroom_X[i+3600])
        mushroom_Y1.append(mushroom_Y[i+3600])
    neigh.fit(mushroom_X1,mushroom_Y1)
    y_pred_benchmark1 = neigh.predict(mushroom_X5)
    
    
    
    for i in range(1200):
        mushroom_X2.append(mushroom_X[i])
        mushroom_Y2.append(mushroom_Y[i])
        mushroom_X6.append(mushroom_X[i+3600])
        mushroom_Y6.append(mushroom_Y[i+3600])
    for i in range(1200):
        mushroom_X2.append(mushroom_X[i+1200])
        mushroom_Y2.append(mushroom_Y[i+1200])
    for i in range(1200):
        mushroom_X2.append(mushroom_X[i+2400])
        mushroom_Y2.append(mushroom_Y[i+2400])
    for i in range(844):
        mushroom_X2.append(mushroom_X[i+4800])
        mushroom_Y2.append(mushroom_Y[i+4800])
    neigh.fit(mushroom_X2,mushroom_Y2)
    y_pred_benchmark2 = neigh.predict(mushroom_X6)
    
    
    
    for i in range(1200):
        mushroom_X3.append(mushroom_X[i+1200])
        mushroom_Y3.append(mushroom_Y[i+1200])
        mushroom_X7.append(mushroom_X[i])
        mushroom_Y7.append(mushroom_Y[i])
    for i in range(1200):
        mushroom_X3.append(mushroom_X[i+2400])
        mushroom_Y3.append(mushroom_Y[i+2400])
    for i in range(1200):
        mushroom_X3.append(mushroom_X[i+3600])
        mushroom_Y3.append(mushroom_Y[i+3600])
    for i in range(844):
        mushroom_X3.append(mushroom_X[i+4800])
        mushroom_Y3.append(mushroom_Y[i+4800])
    neigh.fit(mushroom_X3,mushroom_Y3)
    y_pred_benchmark3 = neigh.predict(mushroom_X7)
    
    for i in range(1200):
        mushroom_X4.append(mushroom_X[i])
        mushroom_Y4.append(mushroom_Y[i])
        mushroom_X8.append(mushroom_X[i+2400])
        mushroom_Y8.append(mushroom_Y[i+2400])
    for i in range(1200):
        mushroom_X4.append(mushroom_X[i+1200])
        mushroom_Y4.append(mushroom_Y[i+1200])
    for i in range(1200):
        mushroom_X4.append(mushroom_X[i+3600])
        mushroom_Y4.append(mushroom_Y[i+3600])
    for i in range(844):
        mushroom_X4.append(mushroom_X[i+4800])
        mushroom_Y4.append(mushroom_Y[i+4800])
    neigh.fit(mushroom_X4,mushroom_Y4)
    y_pred_benchmark4 = neigh.predict(mushroom_X8)

    
    
    for i in range(1200):
        mushroom_X9.append(mushroom_X[i])
        mushroom_Y9.append(mushroom_Y[i])
        mushroom_X10.append(mushroom_X[i+1200])
        mushroom_Y10.append(mushroom_Y[i+1200])
    for i in range(1200):
        mushroom_X9.append(mushroom_X[i+2400])
        mushroom_Y9.append(mushroom_Y[i+2400])
    for i in range(1200):
        mushroom_X9.append(mushroom_X[i+3600])
        mushroom_Y9.append(mushroom_Y[i+3600])
    for i in range(844):
        mushroom_X9.append(mushroom_X[i+4800])
        mushroom_Y9.append(mushroom_Y[i+4800])
    neigh.fit(mushroom_X9,mushroom_Y9)
    y_pred_benchmark5 = neigh.predict(mushroom_X10)
    
    #print('---------------------5-fold cross validation--------------------------')
    
    x1 = np.array(mushroom_Y5)
    x2 = np.array(mushroom_Y6)
    x3 = np.array(mushroom_Y7)
    x4 = np.array(mushroom_Y8)
    x5 = np.array(mushroom_Y10)
    
    #print(confusion_matrix(x1, y_pred_benchmark1,labels=['0','1'])+
    #  confusion_matrix(x2, y_pred_benchmark2,labels=['0','1'])+
    #  confusion_matrix(x3, y_pred_benchmark3,labels=['0','1'])+
    #  confusion_matrix(x4, y_pred_benchmark4,labels=['0','1'])+
    #  confusion_matrix(x5, y_pred_benchmark5,labels=['0','1']))
    a1=confusion_matrix(x1, y_pred_benchmark1,labels=['0','1'])+confusion_matrix(x2, y_pred_benchmark2,labels=['0','1'])+confusion_matrix(x3, y_pred_benchmark3,labels=['0','1'])+confusion_matrix(x4, y_pred_benchmark4,labels=['0','1'])+confusion_matrix(x5, y_pred_benchmark5,labels=['0','1'])
    #print("正確率:")
    #print((a1[1][1]+a1[0][0])/(a1[0][0]+a1[0][1]+a1[1][0]+a1[1][1]))
    #a1=confusion_matrix(x1, y_pred_benchmark1,labels=['0','1'])+confusion_matrix(x2, y_pred_benchmark2,labels=['0','1'])+confusion_matrix(x3, y_pred_benchmark3,labels=['0','1'])+confusion_matrix(x4, y_pred_benchmark4,labels=['0','1'])+confusion_matrix(x5, y_pred_benchmark5,labels=['0','1'])
    #result[0]=a1
    #result[1]=(a1[1][1]+a1[0][0])/(a1[0][0]+a1[0][1]+a1[1][0]+a1[1][1])
    return [confusion_matrix(x1, y_pred_benchmark1,labels=['0','1'])+confusion_matrix(x2, y_pred_benchmark2,labels=['0','1'])+confusion_matrix(x3, y_pred_benchmark3,labels=['0','1'])+confusion_matrix(x4, y_pred_benchmark4,labels=['0','1'])+confusion_matrix(x5, y_pred_benchmark5,labels=['0','1']),(a1[1][1]+a1[0][0])/(a1[0][0]+a1[0][1]+a1[1][0]+a1[1][1])]



def resubstitution_validation(mushroom_XX,mushroom_YY,neigh):
    y_pred=neigh.predict(mushroom_XX)
    x = np.array(mushroom_YY)
    print('--------------------resubstitution validation-------------------------')
    cnf_matrix=confusion_matrix(x, y_pred,labels=['0','1'])
    print(cnf_matrix)
    #print("正確率為:")
    #print(neigh.score(wine_XX,wine_YY))

i=0
mushroom_X=[]
mushroom_Y=[]
f = open('agaricus-lepiota.data.csv', 'r')
for row in csv.reader(f):
    new=[]
    new1=[]
    lock=0
    for j in range(23):
        if j !=0:
            if dict(row[j],lock) != '26':
                new.append(dict(row[j],lock))
            else:
                lock=1
        elif j==0:
            if row[j]== '?':
                lock=1        
    if lock==0:
        i+=1
        mushroom_X.append(new)
        if row[0]=='p':
            mushroom_Y.append('1')
        else:
            mushroom_Y.append('0')

    

f.close()

correct=0

for nn in range(100):
    nn+=1
    print(nn)
    k=nn
    neigh = KNeighborsClassifier(n_neighbors=k,weights='distance',algorithm='kd_tree', metric='minkowski',p=2)   
    newcorrect=cross_validation(mushroom_X,mushroom_Y,neigh)
    if newcorrect[1] >= correct:
        correct=newcorrect[1]
        matrixfinal=newcorrect[0]
        correctfinal=newcorrect[1]
        kfinal=k
        pfinal="Euclidean_distance"


for mm in range(100):
    mm+=1
    print(mm)
    k=mm
    neigh = KNeighborsClassifier(n_neighbors=k,weights='distance',algorithm='kd_tree', metric='minkowski',p=1)   
    newcorrect=cross_validation(mushroom_X,mushroom_Y,neigh)
    if newcorrect[1] >= correct:
        correct=newcorrect[1]
        matrixfinal=newcorrect[0]
        correctfinal=newcorrect[1]
        kfinal=k
        pfinal="Manhattan_distance"




print("KNN algoritm 在 K=",end='')
print(kfinal,end='')
print(" 時")
print("用 ",end='')
print(pfinal,end='')
print(" 有最好的正確率:",end='')
print(correctfinal)
print("Confusion matrix:")
print(matrixfinal)

