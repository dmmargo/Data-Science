from pandas import Series, DataFrame
import pandas as pd
import numpy as np 
import math 

list1 = np.random.randint(100, size=1000)
list2 = np.random.randint(100, size=1000)
list3 = np.random.randint(100, size=1000)

dictionary = {'Data 1' : list1, 
              'Data 2' : list2, 
              'Data 3' : list3}

frame = DataFrame(dictionary)
ax = frame.plot(legend=True)
ax.set_xlabel('Data Set')
ax.set_ylabel('Random Numbers')
ax.legend(loc='center left', bbox_to_anchor=(1,0.9))