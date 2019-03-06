# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 22:58:57 2017

@author: John
"""

from pandas import Series
series = Series.from_csv('dataset.csv')
print(series.describe())