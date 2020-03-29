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

# italy
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
italy_dates_length = len(corn_x)

# set italy absorb
italy_absorb = corn_y[italy_dates_length-1]

corn_y_norm = corn_y / italy_absorb

model.fit(corn_x, corn_y_norm, epochs=25000, shuffle=False)
corn_y_predict = model.predict(corn_x)
corn_y_predict = corn_y_predict * italy_absorb
fig1 = plt.figure(figsize=(7, 5))
plt.scatter(corn_x, corn_y, label='Real Confirmed')
plt.plot(corn_x, corn_y_predict, label='Predict Result')
plt.title('Italy Confirmed VS Dates')
plt.xlabel('Dates')
plt.ylabel('Amount')
plt.legend()
plt.show()

# germany

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

model.fit(ger_corn_x, corn_y_norm, epochs=25000, shuffle=False)
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

# France model

with open('data/france_history.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    rows = [row for row in reader]


fr_corn_y = []

for each_y in rows:
    fr_corn_y.append(int(each_y[0]))


dates = len(fr_corn_y)
fr_corn_x = list(range(1, dates + 1))

fr_corn_x = np.array(fr_corn_x)
fr_corn_y = np.array(fr_corn_y)

fr_dates_length = len(fr_corn_x)
fr_absorb = fr_corn_y[fr_dates_length-1]

corn_y_norm = fr_corn_y / fr_absorb

model.fit(fr_corn_x, corn_y_norm, epochs=25000, shuffle=False)
corn_y_predict = model.predict(fr_corn_x)
corn_y_predict = corn_y_predict * fr_absorb
fig_italy = plt.figure(figsize=(7, 5))
plt.scatter(fr_corn_x, fr_corn_y, label='Real Confirmed')
plt.plot(fr_corn_x, corn_y_predict, label='Predict Result')
plt.title('France Confirmed VS Dates')
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

# add uk latest data manually
uk_comfirmed_data.append(19522)

uk_date_length = len(uk_comfirmed_data)
uk_dates = list(range(1, uk_date_length + 1))

uk_comfirmed_data = np.array(uk_comfirmed_data)
uk_dates = np.array(uk_dates)

uk_absorb_amount = uk_comfirmed_data[uk_date_length-1]

uk_comfirmed_data_norm = uk_comfirmed_data / uk_absorb_amount

# fit model
model.fit(uk_dates, uk_comfirmed_data_norm, epochs=25000, shuffle=False)

uk_comfirmed_data_predict = model.predict(uk_dates)
uk_comfirmed_data_predict = uk_comfirmed_data_predict * uk_absorb_amount
fig2 = plt.figure(figsize=(7, 5))
plt.scatter(uk_dates, uk_comfirmed_data, label='Real Confirmed')
plt.plot(uk_dates, uk_comfirmed_data_predict, label='Predict Result')
plt.title('UK Confirmed VS Dates')
plt.xlabel('Dates')
plt.ylabel('Amount')
plt.legend()
plt.show()

uk_comfirmed_data_predict = np.array(list(range(1, uk_date_length+8)))
uk_comfirmed_predict_7_days = model.predict(uk_comfirmed_data_predict)
fig3 = plt.figure(figsize=(7, 5))
plt.scatter(uk_dates, uk_comfirmed_data, label='Real Confirmed')
plt.plot(uk_comfirmed_data_predict, uk_comfirmed_predict_7_days*uk_absorb_amount, label='Predict Result')
plt.title('UK Prediction Confirmed VS Dates')
plt.xlabel('Dates')
plt.ylabel('Amount')
plt.legend()
plt.savefig('uk_model_7_days.png')
plt.show()

# save prediction data
with open('uk_prediction_data/uk_prediction.json', 'w') as f:
    dict_uk_data = dict(zip(list(range(1, uk_date_length+8)), (uk_comfirmed_predict_7_days*uk_absorb_amount).tolist()))
    json.dump(dict_uk_data, f)
