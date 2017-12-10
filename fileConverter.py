import pandas as pd
import numpy as np
import time
import datetime
from datetime import datetime
from pathlib import Path
import os 

inputfile = 'rawdataHouse4.csv'
outputfile = "convertedDataHouseTest.csv"


df = pd.read_csv(inputfile, names = ['wave'])

newDF = pd.DataFrame(columns=['labels','waves'])

waves = df['wave'].tolist()
count = 0
wavelist = []
for x in range(0, len(waves)):
    wavelist.append(waves[x])
    if len(wavelist) == 512:
        newDF.loc[count] = ['label', wavelist]
        count = count + 1
        wavelist = []

# accounting for buffer in beginning
delta = 600 - len(newDF)  #600
delta = 15 - 15 - delta # we don't want to count the first 15 seconds of data
del_index = []
for x in range (0, delta):
    del_index.append(x)
newDF.drop(newDF.index[del_index], inplace = True) # dropping 
newDF.reset_index(drop = True, inplace = True)

labels = []
for x in range(0,600):
    labels.append(x)

for x in range(0,600):
    if x < 50:
        labels[x] = 0
        continue
    if x < 60:
        labels[x] = 1
        continue
    if x < 110:
        labels[x] = 0
        continue
    if x < 120:
        labels[x] = 1
        continue
    if x < 170:
        labels[x] = 0
        continue
    if x < 180:
        labels[x] = 1
        continue
    if x < 230:
        labels[x] = 0
        continue
    if x < 240:
        labels[x] = 1
        continue
    if x < 290:
        labels[x] = 0
        continue
    if x < 300:
        labels[x] = 1
        continue
    if x < 350:
        labels[x] = 0
        continue
    if x < 360:
        labels[x] = 1
        continue
    if x < 410:
        labels[x] = 0
        continue
    if x < 420:
        labels[x] = 1
        continue
    if x < 470:
        labels[x] = 0
        continue
    if x < 480:
        labels[x] = 1
        continue
    if x < 530:
        labels[x] = 0
        continue
    if x < 540:
        labels[x] = 1
    else:
        labels[x] = 0


newDF['labels'] = labels
path = cwd = os.getcwd()

my_file = Path(path + "/" + outputfile)
if my_file.is_file():
    totalDF = pd.read_csv(outputfile)
    totalDF = totalDF.append(newDF)
    totalDF.reset_index(drop = True, inplace=True)
    totalDF.to_csv(outputfile, index = False)
else: 
    newDF.to_csv(outputfile, index = False)