# -*- coding:utf-8 -*-

import re
import matplotlib.pyplot as plt
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import cross_validation
import os
from sklearn.datasets import load_iris
from sklearn import tree
import pydotplus


def load_pop3(filename):  #加载数据
    x=[]
    with open(filename) as f:
        for line in f:
            line=line.strip('\n')
            line=line.split(',')
            x.append(line)
    return x

def get_pop3(x): #数据清洗
    v=[]
    w=[]
    y=[]
    for hulkdata in x:
        if ( hulkdata[41] in ['guess_passwd.','normal.'] ) and ( hulkdata[2] == 'pop_3' ):
            if hulkdata[41] == 'guess_passwd.':
                y.append(1)
            else:
                y.append(0)

            hulkdata = [hulkdata[0]] + hulkdata[4:8]+hulkdata[22:30]  #最终将数据清洗出来
            v.append(hulkdata)

    for hulkdata in v :
        v1=[]
        for hulkdata2 in hulkdata:
            v1.append(float(hulkdata2))
        w.append(v1)
    return w,y

if __name__ == '__main__':
    v=load_pop3("/root/pop3_data")
    x,y=get_pop3(v)
    clf = tree.DecisionTreeClassifier() #训练数据，实例化决策树算法
    print  cross_validation.cross_val_score(clf, x, y, n_jobs=-1, cv=10)
