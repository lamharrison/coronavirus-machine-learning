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
import numpy as np

with open('data/italy_history.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    rows = [row for row in reader]


corn_y = []

for each_y in rows:
    corn_y.append(int(each_y[0]))


dates = len(corn_y)
corn_x = list(range(1, dates + 1))


corn_x = np.array(corn_x)
corn_y = np.array(corn_y)
corn_y_norm = corn_y / 115000

model.fit(corn_x, corn_y_norm, epochs=1000)
corn_y_predict = model.predict(corn_x)
corn_y_predict = corn_y_predict * 115000
fig1 = plt.figure(figsize=(7, 5))
plt.scatter(corn_x, corn_y, label='Real Confirmed')
plt.plot(corn_x, corn_y_predict, label='Predict Result')
plt.title('Italy Confirmed VS Dates')
plt.xlabel('Dates')
plt.ylabel('Amount')
plt.legend()
plt.show()

# uk corona
import json

url = 'https://api.covid19uk.live/historyfigures'


def read_url_to_json(url):
    import urllib.request as request
    webpage = request.urlopen(url)
    get_data = webpage.read()
    data = json.loads(get_data)
    return data


read_data = read_url_to_json(url)
each_data = read_data['data']
uk_comfirmed_data = []

for each in each_data:
    uk_comfirmed_data.append(each['confirmed'])

uk_date_length = len(uk_comfirmed_data)
uk_dates = list(range(1, uk_date_length + 1))

uk_comfirmed_data = np.array(uk_comfirmed_data)
uk_dates = np.array(uk_dates)

uk_comfirmed_data_norm = uk_comfirmed_data / 21000

# fit model
model.fit(uk_dates, uk_comfirmed_data_norm, epochs=1000)

uk_comfirmed_data_predict = model.predict(uk_dates)
uk_comfirmed_data_predict = uk_comfirmed_data_predict * 21000
fig2 = plt.figure(figsize=(7, 5))
plt.scatter(uk_dates, uk_comfirmed_data, label='Real Confirmed')
plt.plot(uk_dates, uk_comfirmed_data_predict, label='Predict Result')
plt.title('UK Confirmed VS Dates')
plt.xlabel('Dates')
plt.ylabel('Amount')
plt.legend()
plt.show()

uk_comfirmed_data_predict = np.array(list(range(1, 101)))
uk_comfirmed_predict_100 = model.predict(uk_comfirmed_data_predict)
fig3 = plt.figure(figsize=(7, 5))
plt.scatter(uk_dates, uk_comfirmed_data, label='Real Confirmed')
plt.plot(uk_comfirmed_data_predict, uk_comfirmed_predict_100*21000, label='Predict Result')
plt.title('UK Prediction Confirmed VS Dates')
plt.xlabel('Dates')
plt.ylabel('Amount')
plt.legend()
plt.show()
