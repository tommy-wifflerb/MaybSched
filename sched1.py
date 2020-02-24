import csv
import numpy as np
import pandas as pd

data = pd.read_csv('Holiday Schedule Ranking 2019.csv', index_col = 0)
cols = []
for col in data.columns:
    cols.append(col)
numdates = len(cols)

schedule = pd.DataFrame(np.full((3,numdates), "replace"), columns = cols)

positions = ["one","two","three"]

schedule.index = positions

empdaysdict = {}

for emp, row in data.iterrows():
    day_count = 0
    sortedlistofdates = row.sort_values(axis=0).index.tolist()
    for x in range(13):
        if day_count == 2:
            break

        if schedule.loc["one", sortedlistofdates[x]] == "replace":
            schedule.loc["one", sortedlistofdates[x]] = emp
            day_count +=1

        elif schedule.loc["two", sortedlistofdates[x]] == "replace":
            schedule.loc["two", sortedlistofdates[x]] = emp
            day_count +=1
        
        elif schedule.loc["three", sortedlistofdates[x]] == "replace":
            schedule.loc["three", sortedlistofdates[x]] = emp
            day_count +=1

        empdaysdict[emp] = day_count

# then write dataframe to csv file
schedule.to_csv("final_schedule.csv")