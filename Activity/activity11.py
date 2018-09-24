from random import randint
from pandas import Series, DataFrame
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt

Obj = pd.read_csv('brfss.csv')


def cleanBRFSSFrame(theDF):
    del theDF['sex']
    theDF = theDF.dropna()
    return theDF


Obj = cleanBRFSSFrame(Obj)
print(Obj['weight2'].describe())
print("Mode: ", Obj['weight2'].mode())


def minMaxScale(theSeries):
    return (theSeries - theSeries.min()) / (theSeries.max() - theSeries.min())


scaledData = Obj.apply(minMaxScale)
scaledData.boxplot()
plt.show()