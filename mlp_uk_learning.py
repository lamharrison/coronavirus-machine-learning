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

uk_comfirmed_data_norm = uk_comfirmed_data / 14658

# fit model
model.fit(uk_dates, uk_comfirmed_data_norm, epochs=5000, shuffle=False)

uk_comfirmed_data_predict = model.predict(uk_dates)
uk_comfirmed_data_predict = uk_comfirmed_data_predict * 14658
fig2 = plt.figure(figsize=(7, 5))
plt.scatter(uk_dates, uk_comfirmed_data, label='Real Confirmed')
plt.plot(uk_dates, uk_comfirmed_data_predict, label='Predict Result')
plt.title('UK Confirmed VS Dates')
plt.xlabel('Dates')
plt.ylabel('Amount')
plt.legend()
plt.show()