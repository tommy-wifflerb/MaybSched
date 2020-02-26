import csv
import numpy as np
import pandas as pd
# Load data into dataframe
data = pd.read_csv('Holiday Schedule Ranking 2019.csv', index_col = 0)
print(data)
cols = []
# Get column headers
for col in data.columns:
    cols.append(col)
print(cols)
numdates = len(cols)
print(numdates)
# Make empty schedule
schedule = pd.DataFrame(np.full((3,numdates), "replace"), columns = cols)
positions = ["One","Two","Three"]
schedule.index = positions
print(schedule)

empdaysdict = {}
# This is where we figure out the schedule
for emp, row in data.iterrows():
    workcount = 0
    sortedlistofdates = row.sort_values(axis=0).index.tolist()
    for x in range(numdates):
        if workcount == 2:
            break
        if schedule.loc["One", sortedlistofdates[x]] == "replace":
            schedule.loc["One", sortedlistofdates[x]] = emp
            workcount = workcount + 1
        elif schedule.loc["Two", sortedlistofdates[x]] == "replace":
            schedule.loc["Two", sortedlistofdates[x]] = emp
            workcount = workcount + 1
        elif schedule.loc["Three", sortedlistofdates[x]] == "replace":
            schedule.loc["Three", sortedlistofdates[x]] = emp
            workcount = workcount + 1
        empdaysdict[emp] = workcount

print(empdaysdict)
# write dataframe to csv file
schedule.to_csv("Final_Mayb_Schedule.csv")