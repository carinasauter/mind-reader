import pandas as pd
import numpy as np
import time
import datetime
from datetime import datetime
from pathlib import Path
import os 

df = pd.read_csv('rawdata.csv', names = ['wave'])
newDF = pd.DataFrame(columns=['label','waves'])
waves = df['wave'].tolist()

count = 0
wavelist = []
for x in range(0, len(waves)):
    wavelist.append(waves[x])
    if len(wavelist) == 512:
        newDF.loc[count] = ['label', str(wavelist)]
        count = count + 1
        wavelist = []

path = cwd = os.getcwd()
my_file = Path(path + "/convertedData.csv")
if my_file.is_file():
    totalDF = pd.read_csv('convertedData.csv', index_col = 0)
    totalDF = totalDF.append(newDF)
    totalDF.reset_index(drop = True, inplace=True)

    totalDF.to_csv('convertedData.csv')
else: 
    newDF.to_csv('convertedData.csv')