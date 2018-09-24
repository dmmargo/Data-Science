import math
from pandas import Series, DataFrame as df
import statistics
import numpy as np
import pandas as pd


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