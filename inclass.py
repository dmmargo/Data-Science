# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 14:30:06 2018

@author: Diane
"""

from pandas import Series, DataFrame as df
import math 
#import statistics
import pandas as pd
import numpy as np
import random
from scipy.spatial import distance
from pandas.plotting import scatter_matrix



'''
#making a list from 0-9 and then squaring it
list2 = [x**2 for x in range(10)]
print(list2) # prints 0, 1, 4, 9, 16, 25, 36, 49, 64, 81

#creating list
list1 = [(x,y) for x in range(10)
for y in range(5)]
print(list1)

items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, items))

print(squared) #prints 1, 4, 9, 16, 25


#Activity2
Celsius = [39.2, 36.2, 37.3, 37.8]
F = list(map(lambda c: ((9/5)*c) +32, Celsius))
print(F)


names = ['James', 'Tom', 'Mary']
grades = [100, 90, 95]
M = list(zip(names, grades))
print(M) # prints [('James', 100), ('Tom', 90), ('Mary', 95)]

'''
#*********************************************************************
"""
myRandomList = [random.randint(1, 11)]
print(myRandomList) #just prints one number
"""
"""
myRandomList = [random.randint(1, 11) for i in range(5)] 
print(myRandomList) # prints 5 random numbers
"""
#*********************************************************************** 
'''
list = [5, 6, 2, 4, -1]
obj = Series(list, index = ['a', 'b', 'c', 'd', 'e'])
print(obj) 
"""
prints
0    5
1    6
2    2
3    4
4   -1
    dtype: int64
"""
print(obj.index)
#prints RangeIndex(start=0, stop=5, step=1) with just list 
# prints Index(['a', 'b', 'c', 'd', 'e'], dtype='object') with index = ...
print(obj.values)
"""
prints:
[ 5  6  2  4 -1]
"""
print(obj**2)
'''
#**********************************************************************
#4/4/2018
#**********************************************************************

'''
#obj2 = Series([4, 7, -5, 3] , index=['d', 'b', 'a', 'c'])
obj2 = Series([4, 7, -5, 3], index=range(4))
obj3 = obj2[:2]
print(obj3)
#print (obj2[-2]) 
#print(obj2[:2].values)
#print(obj2[:2].index)

sdata = {'Texas': 10, 'Ohio': 20, 'Oregon': 15, 'Utah': 18}
states = ['Texas', 'Ohio', 'Oregon', 'Iowa']
obj4 = Series(sdata, index=states)
print(obj4)

sdata = {'Texas': 10, 'Ohio': 20, 'Oregon': 15, 'Utah': 18}
states = ['Texas', 'Ohio', 'Oregon', 'Utah']
obj5 = Series(sdata, index=states)
print(obj5)
'''

#***************************************************************
#activity3
"""
RandomNumbers = [random.randint(1, 100) for i in range(10)]
mixedValues = Series(RandomNumbers, index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])
mixedValues**2
print(mixedValues[-4:])


'''
rands = [random.randint(1, 100) for i in range(10)]
obj = Series(rands, index = range(1,11))
#print(obj)
obj2 = obj**2
print(obj2[-4:])
'''
"""
#**************************************************************
'''
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
'year': [2000, 2001, 2002, 2001, 2002],
'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
frame = df(data) #frame = DataFrame(data)
frame = df(data, index = ['a', 'b', 'c', 'd', 'e'])
print(frame)

frame2 = df(data, columns=['year', 'state', 'pop', 'debt'], index=['A', 'B', 'C', 'D', 'E'])
print(frame2)

pop = {'Nevada': {2001: 2.9, 2002: 2.9}, 'Ohio': {2002: 3.6, 2001: 1.7, 2000: 1.5}}
frame3 = df(pop)
print(frame3)

#transpose - shift colums and rows
print(frame3.T)
'''
#***********************************************
#Activity 3
'''
frame = pd.read_csv('values.csv')
print(frame)

print('mean:', frame.factor_1.mean())
print('stdev:', frame.factor_1.std())
'''
#***********************************************
'''
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
'year': [2000, 2001, 2002, 2001, 2002],
'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}

frame2 = df(data, columns=['year', 'state', 'pop', 'debt'], index=['A', 'B', 'C', 'D', 'E'])
print(frame2)
#print(frame2.loc['A':'C'])
#print(frame2.iloc[1:3]) 
print(frame2.iloc[1:2])
'''



#********************************************************
# 4/11/18

#*********************************************************

'''
data = {'default': [32, 9, 0, 0, 0],
'TedEd': [0, 18, 30, 14, 2],
'League': [0, 0, 0, 1, 18],
'both': [0, 18, 30, 15, 20]}
frame2 = df(data, columns=['default', 'TedEd', 'League', 'both'], index=['default', 'video_1', 'video_2', 'video_3', 'video_4'])
print(frame2)
print(frame2.iloc[[],[]])
'''
data = {'No theme': [22, 14, 6, 5, 1],
'Hero Movies': [3, 17, 20, 14, 12],
'Scary Videos': [0, 0, 0, 8, 8],
'both': [0, 0, 0, 22, 20]}
frame2 = df(data, columns=['No theme', 'Hero Movies', 'Scary Videos', 'both'], index=['default', 'video_1', 'video_2', 'video_3', 'video_4'])
print(frame2)
print(frame2.iloc[[],[]])
'''
data = {'default': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
'year': [2000, 2001, 2002, 2001, 2002],
'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
frame2 = df(data, columns=['year', 'state', 'pop', 'debt'], index=['A', 'B', 'C', 'D', 'E'])


print(frame2)
print(frame2.iloc[[],[]])
'''


#***********************************************************
'''
data = np.random.random_integers(1, 100, (3, 5))
print(data)
df = DataFrame(data, index = ['a', 'b', 'c'], columns = [1, 2, 3, 4, 5])
print(df)
df = df.T
df[df < 40] = 0
print(df)

print(df.applymap(lambda x: math.sqrt(x)))
'''
#*************************************************************

'''

df3 = DataFrame(np.random.randint(0, 10, (4, 3)), index=['A', 'B', 'C', 'D'], columns=['i', 'ii', 'iii'])

print(df3)
ax = df3.plot(xticks = range(4), legend=False, style=['r+-','gx-','b*-'], title='My Chart')
ax.set_xlabel('Index')
ax.set_ylabel('Columns')
'''

#***********************************************************************
#4/18
#***********************************************************
'''
brfssData = pd.read_csv('brfss.csv', index_col=0)
print(brfssData)

def cleanBRFSSData(df):
    df = df.drop(['sex'],axis=1)
    df = df.dropna(axis=0)
    return df

cleanBrfss = cleanBRFSSData(brfssData)

print(cleanBrfss)

print(cleanBrfss['weight2'].describe())
print(cleanBrfss.mode()['weight2'])

cleanBrfss.boxplot()


#***********************************************
#4/23
#*************************************************

def minmaxScaling(series):
    return (series-series.min())/(series.max()-series.min())

scaledData = cleanBrfss.apply(minmaxScaling)
scaledData.boxploy()
'''













