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
schedule = pd.DataFrame(np.full((3,numdates), "Empty"), columns = cols)
positions = ["One","Two","Three"]
schedule.index = positions
print(schedule)

empdaysdict = {}
# This is where we figure out the schedule
for employee, row in data.iterrows():
    workcount = 0
    sortedlistofdates = row.sort_values(axis=0).index.tolist()
    for x in range(numdates):
        if workcount == 2:
            break
        if schedule.loc["One", sortedlistofdates[x]] == "Empty":
            schedule.loc["One", sortedlistofdates[x]] = employee
            workcount = workcount + 1
        elif schedule.loc["Two", sortedlistofdates[x]] == "Empty":
            schedule.loc["Two", sortedlistofdates[x]] = employee
            workcount = workcount + 1
        elif schedule.loc["Three", sortedlistofdates[x]] == "Empty":
            schedule.loc["Three", sortedlistofdates[x]] = employee
            workcount = workcount + 1
        empdaysdict[employee] = workcount

print(empdaysdict)
# write dataframe to csv file
schedule.to_csv("Final_Mayb_Schedule.csv")