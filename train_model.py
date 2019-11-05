# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 20:25:26 2019

@author: Marek
"""

import pandas as pd
import numpy as np
import statsmodels.api as sm
#from sklearn.preprocessing import scale

#log - square root transformation
train = np.log(np.sqrt(pd.read_csv(r'data/Train.csv').Count))
test = pd.read_csv(r'data/Test.csv')


model = sm.tsa.ExponentialSmoothing(np.asarray(train), seasonal_periods=168 ,trend="add", seasonal= "add",).fit(
                                   use_brute=False, use_basinhopping=True)

pred = model.forecast(len(test))
pred = np.exp(pred)**2


sub = pd.DataFrame(test.ID)
sub['Count'] = pred
