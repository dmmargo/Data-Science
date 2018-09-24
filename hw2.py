# -*- coding: utf-8 -*-
"""
CS299
HW2
@author: Diane Margo
"""

from pandas import Series, DataFrame 
import math 
#import statistics
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
import collections 
from collections import Counter


#***************************************
#part1
#***************************************
data = np.array([0, 7, 3, 6, 2, 8, 5, 9, 4]).reshape(3, 3)
df = pd.DataFrame(data, index=['One', 'Two', 'Three'], columns=['a', 'b', 'c'])

#print(df) #a

'''
       a  b  c
One    0  7  3
Two    6  2  8
Three  5  9  4
'''

#print(df['a']) #b
'''
One      0
Two      6
Three    5
Name: a, dtype: int32
'''

#print(df.loc['Two']) #c
'''
a    6
b    2
c    8
Name: Two, dtype: int32
'''

#print(df[:2]) #d
'''
     a  b  c
One  0  7  3
Two  6  2  8
'''

#print(df.iloc[:,:]) #e
'''
       a  b  c
One    0  7  3
Two    6  2  8
Three  5  9  4
'''

#print(df.iloc[:,:2]) #f
'''
       a  b
One    0  7
Two    6  2
Three  5  9
'''

#print(list(df.columns)) #g
'''
['a', 'b', 'c']
'''

#print(list(df.index)) #h
'''
['One', 'Two', 'Three']
'''

#print(df['b']['Two']) #i
'''
2
'''

#print(list(df.iloc[2, :])) #j
'''
[5, 9, 4]
'''

#print(df.drop('a', axis=1)) #k
'''
       b  c
One    7  3
Two    2  8
Three  9  4
'''

#print(df[df.a !=5]) #l
'''
     a  b  c
One  0  7  3
Two  6  2  8
'''

#print(list(df.sum(axis=0))) #m
'''
[11, 18, 15]
'''

#print(df.iloc[:, list(df.sum(axis=0) < 17)]) #n
'''
       a  c
One    0  3
Two    6  8
Three  5  4
'''

#print(df.sort_values(by='c')) #o
'''
       a  b  c
One    0  7  3
Three  5  9  4
Two    6  2  8
'''

#print(df.sort_values(by='Two', axis=1)) #p
'''
       b  a  c
One    7  0  3
Two    2  6  8
Three  9  5  4
'''

#print(df.T) #q
'''
   One  Two  Three
a    0    6      5
b    7    2      9
c    3    8      4
'''

#print((df<=2).any(axis=0)) #r
'''
a     True
b     True
c    False
dtype: bool
'''

#print(df.applymap(lambda x: x*2-1)) #s
'''
        a   b   c
One    -1  13   5
Two    11   3  15
Three   9  17   7
'''

#print(df.apply(lambda x: max(x), axis=1)) #t
'''
One      7
Two      8
Three    9
dtype: int64
'''


#****************************************
#part2
#****************************************
#part 2 of homework 1

def summaryStatistics(listOfNums):
    
    ss = summaryStatistics
    
    ### Complete this part. 
    # You can decide to return the following statistics either in a sequence 
    # type (i.e., list, tuple), or a key-value pair (i.e., dictionary)
    
    maxVal = np.max(listofNums)
    minVal = np.min(listofNums)
    meanVal = np.mean(listofNums)
    stdev = np.std(listofNums)
    median = np.median(listofNums)
    perc75 = np.percentile(listofNums, 75)
    perc25 = np.percentile(listofNums, 25)
        

    return {'max': maxVal,
            'min': minVal, 
            'mean': meanVal, 
            'stdev': stdev,
            'median': median,
            'perc75': perc75,
            'perc25': perc25}



d1 = [random.randint(1,100) for x in range(100)]
d2 = [random.randint(1,100) for x in range(100)]
d3 = [random.randint(1,100) for x in range(100)]


read1 = ss(d1)
read2 = ss(d1)
read3 = ss(d2)

data = {"Data 1": read1,
        "Data 2": read2,
        "Data 3": read3}

df2 =DataFrame(data, index = ['max', 'min', 'mean', 'stdev', 'median', 'perc25', 'perc75'])

df2d = df2.T

ax = df2d.plot(xticks = range(3), legend=True, style=['r+','rx','bx', 'y^', 'gv', 'b>', 'b<'], title='Summary Statistics')
ax.legend(loc='center left', bbox_to_anchor=(1,0.73))

ax.set_xlabel('Data Set')
ax.set_ylabel('Values')


#****************************************
#part 3
#****************************************
#part 3 from homework 1
'''
def scaleToDigits(listOfNums):
    listOfNums.sort()
    min = listofNums[0]
    max = listofNums[(len(listofNums))-1]
    newList = []
    for x in (listOfNums):
        newList.append((x - min)/(max - min))
	
    return newList
'''
def scaleToDigits(listOfNums):
    
    max = np.max(listOfNums)
    min = np.min(listOfNums)
    newList = [ round(9 * (x - min) / (max - min)) for x in listOfNums]
    
    return newList

sd = scaleToDigits


newList1 = sd(d1)
newList2 = sd(d2)
newList3 = sd(d3)

data1 = Counter(newList1)
data2 = Counter(newList2)
data3 = Counter(newList3)


dataa3 = {"data 1": data1,
          "data 2": data2,
          "data 3": data3}

dfp3 = DataFrame(dataa3)

ax = dfp3.plot(xticks = range(10), legend=True, style=['r+-','gx-','b*-'], title='Frequency of Dataset')
ax.legend(loc='center left', bbox_to_anchor=(1,.85))

ax.set_xlabel('Values')
ax.set_ylabel('Frequency')



