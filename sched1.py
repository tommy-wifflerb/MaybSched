import csv
import numpy as np
import pandas as pd

infile = open('Holiday Schedule Ranking 2019.csv','r')

prefs = csv.reader(infile, delimiter = ',')
header_row = next(prefs)
header_row[0] = 'Employee'
#print(header_row)
names_list = []
totalfile = {}
for row in prefs:
    names_list.append(row[0])
    totalfile[row[0]] = row[1:]

df = pd.DataFrame(totalfile)
df = df.T
df = df.astype(int)

array = np.array(df.sum(axis=0))
maxday = array.max()
day = np.where(array == maxday)
print(day[0])

dayarray = df[7]
index = dayarray.argsort()
daysorted = dayarray[index]
print(daysorted[:3])

zeros = np.zeros((20,14))
print(zeros)



