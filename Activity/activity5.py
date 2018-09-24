from pandas import Series, DataFrame
import pandas as pands
import numpy as numps
import random

nData = numps.random.randint(1, 101, (3, 5))
dFrame = DataFrame(nData, index = ['a', 'b', 'c'], columns = range(1, 6))
dFrame[dFrame < 40] = 0
print(dFrame.T)