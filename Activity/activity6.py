import pandas as pd
import numpy as np
from pandas import Series, DataFrame
import math
 

array = np.random.random_integers(1, 100, (3, 5))
print(array)
frame = DataFrame(array, index=['a', 'b', 'c'], columns=range(1, 6)) #My option: columns=[1, 2, 3, 4, 5]
print(frame.T) #<---This is how you transpose/switch columns/index
frame = frame.T
frame[frame<40] = 0
print(frame)
print(frame.applymap(lambda x: math.sqrt(x)))