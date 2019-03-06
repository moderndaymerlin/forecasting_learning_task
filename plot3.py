# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 23:12:21 2017

@author: John
"""

from pandas import Series
from matplotlib import pyplot
series = Series.from_csv('dataset.csv')
pyplot.figure(1)
pyplot.subplot(211)
series.hist()
pyplot.subplot(212)
series.plot(kind='kde')
pyplot.show()