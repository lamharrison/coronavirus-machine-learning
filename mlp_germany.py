import numpy as np
np.random.seed(1337)
from keras.models import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt

model = Sequential()
model.add(Dense(units=50, input_dim=1, activation='relu'))
model.add(Dense(units=50, activation='relu'))
model.add(Dense(units=1, activation='sigmoid'))
model.add(Dense(units=1, activation='linear'))
model.compile(optimizer='adam', loss='mean_squared_error')
model.summary()

import csv

with open('data/germany_history.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    rows = [row for row in reader]


ger_corn_y = []

for each_y in rows:
    ger_corn_y.append(int(each_y[0]))


dates = len(ger_corn_y)
ger_corn_x = list(range(1, dates + 1))

ger_corn_x = np.array(ger_corn_x)
ger_corn_y = np.array(ger_corn_y)

ger_dates_length = len(ger_corn_x)
ger_absorb = ger_corn_y[ger_dates_length-1]

corn_y_norm = ger_corn_y / ger_absorb

model.fit(ger_corn_x, corn_y_norm, epochs=10000, shuffle=False)
corn_y_predict = model.predict(ger_corn_x)
corn_y_predict = corn_y_predict * ger_absorb
fig_italy = plt.figure(figsize=(7, 5))
plt.scatter(ger_corn_x, ger_corn_y, label='Real Confirmed')
plt.plot(ger_corn_x, corn_y_predict, label='Predict Result')
plt.title('Germany Confirmed VS Dates')
plt.xlabel('Dates')
plt.ylabel('Amount')
plt.legend()
plt.show()