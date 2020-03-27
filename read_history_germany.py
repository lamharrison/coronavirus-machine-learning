import csv
import numpy as np
with open('data/germany_history.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    rows= [row for row in reader]


ger_corn_y = []

for each_y in rows:
    ger_corn_y.append(int(each_y[0]))

dates = len(ger_corn_y)

ger_corn_x = list(range(1, dates+1))

print('dates:')
print(ger_corn_x)
print('confirmed:')
print(ger_corn_y)