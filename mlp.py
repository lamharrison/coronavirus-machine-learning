from keras.models import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt

import csv
import numpy as np

with open('sars.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    rows = [row for row in reader]

X_sars = []
y_sars = []

for each_x in rows[0]:
    X_sars.append(int(each_x))

for each_y in rows[1]:
    y_sars.append(int(each_y))

model = Sequential()
model.add(Dense(units=50, input_dim=1, activation='relu'))
model.add(Dense(units=50, activation='relu'))
model.add(Dense(units=1, activation='sigmoid'))
model.add(Dense(units=1, activation='linear'))
model.compile(optimizer='adam', loss='mean_squared_error')
model.summary()

X_sars = np.array(X_sars)
y_sars_norm = np.array(y_sars) / 10000

model.fit(X_sars, y_sars_norm, epochs=1000)
y_sars_predict = model.predict(X_sars)
y_sars_predict = y_sars_predict * 10000
fig1 = plt.figure(figsize=(7, 5))
plt.scatter(X_sars, y_sars, label='Real Confirmed')
plt.plot(X_sars, y_sars_predict, label='Predict Result')
plt.title('SARS Amount VS Dates')
plt.xlabel('Dates')
plt.ylabel('Amount')
plt.legend()
plt.show()
plt.savefig('model.png')
