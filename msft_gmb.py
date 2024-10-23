# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 16:31:10 2024
     
@author: Josh
"""

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

msft = yf.Ticker('MSFT')     #get MSFT ticker using Yahoo!Finance API
msftYear = msft.history(period='1y')     #take last 1y

msftYearClose = msftYear['Close']    #take only the close price
msftInitialPrice = msftYearClose.iloc[0]    #take price at the start of period

length = len(msftYearClose)
dt = 1 / length     #discrete timestep
mu = 0.22
sigma = 0.2


nPaths = 10     #n of realisations of brownian motion

St = pd.DataFrame(1. , index = msftYearClose.index, columns = list(range(1, nPaths + 1)))   #initialise dataframe
St.loc[St.index[0]] = St.loc[St.index[0]] * msftInitialPrice    #set initial price


for i in range(1, length):  #generate random paths
    dStSt = (mu * dt) + (sigma * np.random.normal(scale = np.sqrt(dt), size = nPaths)) 
    St.loc[St.index[i]] = St.loc[St.index[i-1]] + ( St.loc[St.index[i-1]] * dStSt )
    
fig, ax = plt.subplots()

plt.plot(St, c='b', lw=0.5)
plt.plot(msftYearClose, c='r', lw=0.75, label='MSFT')
ax.set(ylim = [200, 800], xlabel='Time', ylabel='Price (USD)')
ax.legend()
plt.title('1Y MSFT performance, with 10 realisations of GBM')
