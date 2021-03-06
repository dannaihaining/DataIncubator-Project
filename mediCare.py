# -*- coding: utf-8 -*-
"""
Author: https://www.kaggle.com/kerneler/starter-cms-estimated-uninsured-people-0208c6c7-2?scriptVersionId=6820612
"""
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt # plotting
import numpy as np # linear algebra
import os # accessing directory structure
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

file = 'the-percent-of-estimated-eligible-uninsured-people-for-outreach-targeting.csv'
def plotPerColumnDistribution(df, nGraphShown, nGraphPerRow):
    nunique = df.nunique()
    df = df[[col for col in df if nunique[col] > 1 and nunique[col] < 50]] # For displaying purposes, pick columns that have between 1 and 50 unique values
    nRow, nCol = df.shape
    columnNames = list(df)
    nGraphRow = (nCol + nGraphPerRow - 1) / nGraphPerRow
    plt.figure(num = None, figsize = (6 * nGraphPerRow, 8 * nGraphRow), dpi = 80, facecolor = 'w', edgecolor = 'k')
    for i in range(min(nCol, nGraphShown)):
        plt.subplot(nGraphRow, nGraphPerRow, i + 1)
        columnDf = df.iloc[:, i]
        if (not np.issubdtype(type(columnDf.iloc[0]), np.number)):
            valueCounts = columnDf.value_counts()
            valueCounts.plot.bar()
        else:
            columnDf.hist()
        plt.ylabel('counts')
        plt.xticks(rotation = 90)
        plt.title(f'{columnNames[i]} (column {i})')
    plt.tight_layout(pad = 1.0, w_pad = 1.0, h_pad = 1.0)
    plt.show()
    
nRowsRead = 1000 # specify 'None' if want to read whole file
# the-number-of-estimated-eligible-uninsured-people-for-outreach-targeting.csv has 2069 rows in reality, but we are only loading/previewing the first 1000 rows
df1 = pd.read_csv(file, delimiter=',', nrows = nRowsRead)
df1.dataframeName = 'the-number-of-estimated-eligible-uninsured-people-for-outreach-targeting.csv'
nRow, nCol = df1.shape
print(f'There are {nRow} rows and {nCol} columns')
plotPerColumnDistribution(df1, 10, 5)
