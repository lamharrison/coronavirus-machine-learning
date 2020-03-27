import csv
import numpy as np
with open('data/italy_history.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    rows= [row for row in reader]


corn_y = []

for each_y in rows:
    corn_y.append(int(each_y[0]))

dates = len(corn_y)

corn_x = list(range(1, dates+1))

print('dates:')
print(corn_x)
print('confirmed:')
print(corn_y)