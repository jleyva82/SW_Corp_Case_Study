import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as dts
import seaborn as sns
import pandas as pd
import numpy as np
import statsmodels as stat

#get data from files and concat
data1 = pd.read_csv('Desalination_Unit_File_001.csv', header = 1, index_col = 'TIMEFRAME')
data2 = pd.read_excel('Desalination_Unit_File_002.xlsx', header = 1, index_col = 'TIMEFRAME')
data3 = pd.read_excel('Desalination_Unit_File_003.xlsx', header = 1, index_col = 'TIMEFRAME')

data = pd.concat([data1, data2, data3], axis =0)

#sanity check
print(data.info())
print(data.describe())