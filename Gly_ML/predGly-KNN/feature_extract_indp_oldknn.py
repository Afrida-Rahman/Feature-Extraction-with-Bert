import math
import numpy as np
import pandas as pd


def AAC(frag):
    lines = frag
    L=len(lines[1])
    n=int(len(lines))
    AAs='ACDEFGHIKLMNPQRSTVWYO'
    m=len(AAs)
    aac=np.zeros((n,m))
    for i in range(n):
        for j in range(m):
            frequency=lines[i].count(AAs[j])
            frequency=float('%.2f'%frequency)
            aac[i][j]=frequency/L
    aac=aac[:,0:20]
    return np.array(aac)

def KNN(frag):
    lines_train=frag
    L=len(lines_train[1])
    rtrain=int(len(lines_train))
    f2=open('background.txt')
    lines_test=f2.read().splitlines()
    rtest=int(len(lines_test)/2)
    df=pd.read_csv('blosum62.csv')
    matrix=np.array(df)
    matrixmax=np.max(matrix)
    matrixmin=np.min(matrix)
    AAs='CSTPAGNDEQHRKMILVFYWO'
    K=[2,4,8,16,32]
    Knum=len(K)
    KNNScore=[]
    for i in range(rtrain):
        Dist=[]
        for j in range(rtest):
            sim=[]
            for k in range(L):
                line=AAs.index(lines_test[2*j+1][k])
                row=AAs.index(lines_train[i][k])
                matrixscores=matrix[line,row]
                S=float('%.2f'%(matrixscores-matrixmin))
                X=float('%.2f'%(matrixmax-matrixmin))
                sim.append(S/X)
            Dist.append(1-np.sum(sim)/L)
        pos_index=np.argsort(np.array(Dist))
        KNN=[]
        for dim in range(Knum):
            pos=pos_index[0:K[dim]]
            posnum=K[dim]
            count=0.
            for l in range(posnum):
                if pos[l]<=rtest/2:
                    count+=1
            KNN.append(count/K[dim])
        KNNScore.append(KNN)
    KNNScore=np.array(KNNScore)
    return KNNScore


def get_xy():
    pass


def get_file(filename):
    x_test = []
    y_test = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.split('\t')
            x_temp = ''
            for i in line[1]:
                if i not in [' ', '\n']:
                    x_temp += i
            x_test.append(x_temp)
            y_test.append(int(line[0]))
    return x_test,y_test


def get_feature(f_train, f_test=0, file_save=0):
    train, y_train = get_file(f_train)

    train_f1 = pd.DataFrame(AAC(train))
    train_f2 = pd.DataFrame(KNN(train))

    feature_train = pd.concat([train_f1,train_f2],axis=1)
    if f_test != 0:
        test, y_test = get_file(f_test)
        test_f1 = pd.DataFrame(AAC(test))
        test_f2 = pd.DataFrame(KNN(test))
        feature_test = pd.concat([test_f1, test_f2], axis=1)
        feature_train.to_csv(file_save+ '/f_train_oldknn.csv', header=False, index=False)
        feature_test.to_csv(file_save+ '/f_test_oldknn.csv', header=False, index=False)
        return feature_train, feature_test
    return feature_train

if __name__ == '__main__':
    f_train = './train.tsv'
    f_test = './test.tsv'
    f_save = './indp_feature/'

    get_feature(f_train, f_test, f_save)




