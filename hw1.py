# -*- coding: utf-8 -*-
"""
CS141
HW1
@author: 
"""
import math
import statistics
import numpy as np
import random

"""Given two list of numbers that are already sorted, 
 return a single merged list in sorted order.
"""
sortedListA = [1, 2, 3, 4, 5] 
sortedListB = [2, 4, 5, 6, 8, 9]
listofNums = [4, 5, 6, 10]
 
def merge(sortedListA, sortedListB):
   
    ### Complete this part 

    betalist = sortedListA + sortedListB
    sortedList = sorted(betalist)

    return sortedList 

print(merge(sortedListA, sortedListB))



"""Givne a list of numbers in random order, return the summary statistics 
that includes the max, min, mean, population standard deviation, median,
75 percentile, and 25 percentile.
"""    

def summaryStatistics(listOfNums):
    
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
print(summaryStatistics(listofNums))

        

"""Given a list of real numbers in any range, scale them to be 
between 0 and 1 (inclusive). For each number x in the list, the new number 
is computed with the formula ((x - min)/(max - min)) where max is the 
maximum value of the original list and min is the minimum value of the list. 
"""	

def scaleToDigits(listOfNums):
    listOfNums.sort()
    min = listofNums[0]
    max = listofNums[(len(listofNums))-1]
    newList = []
    for x in (listOfNums):
        newList.append((x - min)/(max - min))
	
    return newList

listofNums = [random.randint(1,10) for i in range(10)]
print(listofNums)
print(scaleToDigits(listofNums))
