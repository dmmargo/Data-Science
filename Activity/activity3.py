from pandas import Series, DataFrame as df
import pandas as pd
import numpy as np
import random

RandomNumbers = [random.randint(1, 100) for i in range(10)]
mixedValues = Series(RandomNumbers, index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])
mixedValues**2
print(mixedValues[-4:])