import csv
import numpy as np
with open('sars.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    rows= [row for row in reader]


X_sars = []
y_sars = []

for each_x in rows[0]:
    X_sars.append(int(each_x))

for each_y in rows[1]:
    y_sars.append(int(each_y))

print(X_sars)
print(y_sars)