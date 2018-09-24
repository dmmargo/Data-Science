import numpy as np
from pandas import Series, DataFrame
import pandas as pd

frame = pd.read_csv('values.csv')
print(frame)
print('mean:', frame.factor_1.mean())
print('stdev:', frame.factor_1.std())