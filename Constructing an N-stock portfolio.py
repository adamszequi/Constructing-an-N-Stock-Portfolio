# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 11:31:50 2020

@author: Dell
"""

import numpy as np
import pandas as pd
import yfinance as yf
import os
import scipy as sp

#function for downloading indicators
def downloadTickerData(tickers,startDate,endDate):
    data=yf.download((tickers),start=startDate,end=endDate)
    return data['Adj Close']

#download collective data from website
data=pd.read_pickle(r'C:\Users\Dell\Desktop\data\yanMonthly (2).pkl')
IBMdata=data[data.index=='IBM']

#create a function for return of the data
def returndata(ticker):
    tickerData=data[data.index==ticker]
    prices=tickerData.VALUE.values
    returns=prices[1:]/prices[:-1]-1
    date=tickerData.DATE.values
    output=pd.DataFrame(index=date[1:])
    output[f'{ticker}returns']=returns
    return output

dataIndices=sp.unique(data.index)
dataIndicesCrop=dataIndices[dataIndices<'ZZZZ']
dataIndicesCropped=list(dataIndicesCrop)

nStocks=10

sp.random.seed(1234567)

nonStocks=['GOLDPRICE','HML','SMB','Mkt_Rf','Rf','Russ3000E_D','US_\
DEBT','Russ3000E_X','US_GDP2009dollar','US_GDP2013dollar']

for _ in range(len(nonStocks)):
    dataIndicesCropped.remove(nonStocks[_])

randomValues=sp.random.uniform(low=1,high=len(dataIndicesCropped),size=nStocks)
randomValuesIndex,dataIndicesCroppedIndex=[],[]

for i in range(nStocks):
    intValue=int(randomValues[i])
    randomValuesIndex.append(intValue)
    dataIndicesCroppedIndex.append(dataIndicesCropped[intValue])

finalDataSet=returndata(dataIndicesCroppedIndex[0])

for _  in sp.arange(1,nStocks):
    returns=returndata(dataIndicesCroppedIndex[_])
    finalDataSet=pd.merge(finalDataSet,returns,left_index=True, right_index=True)

#portfolio dataset
print(finalDataSet)
