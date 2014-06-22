# -*- coding: utf-8 -*-
"""
Some methods
from 2001 to 2013
"""
__author__ = 'chen hsueh-min'


import datetime
import numpy as np
from RawDataProcessing import *
from scipy.stats.stats import pearsonr

def str2date(dateStr):
	return datetime.datetime.strptime(dateStr, '%Y/%m/%d').date()

def StrategyTesting(beginDate, endDate, strategy, optionData=None, stockData=None):
	beginDate = datetime.datetime.strptime( beginDate, '%Y/%m/%d' ).date()
	endDate   = datetime.datetime.strptime( endDate,   '%Y/%m/%d' ).date()
	dtIdx = OptionDailyData.invKeys['Date']

	if optionData is None and stockData is None:
		raise 'No data'

	if optionData is not None:
		i = 0
		while optionData[i][dtIdx] < beginDate: i += 1

	if stockData is not None:
		j = 0
		while stockData[j][dtIdx]  < beginDate: j += 1

	while (i != None) or (j != None) or (optionData[i][dtIdx] <= endDate) or (stockData[j][dtIdx] <= endDate):
		strategy( optionData=optionData[i], stockData=stockData[j] )
		i += 1
		j += 1


def returnRate(data):
	return np.diff(data) / map(float, data[:len(data)-1])

def nCorelation(x, y, n=None, pValue=False):
	if n is None:
		if pValue:
			return pearsonr(x, y)
		else:
			return pearsonr(x, y)[0]
	else:
		if pValue:
			return [pearsonr(x[k-n:k], y[k-n:k])    for k in range(n,len(x)+1)]
		else:
			return [pearsonr(x[k-n:k], y[k-n:k])[0] for k in range(n,len(x)+1)]


