# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 23:00:13 2017

@author: John
"""

from pandas import Series
from matplotlib import pyplot
series = Series.from_csv('dataset.csv')
series.plot()
pyplot.show()