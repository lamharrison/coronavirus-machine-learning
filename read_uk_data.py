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
comfirmed_data = []

for each in each_data:
    comfirmed_data.append(each['confirmed'])

date_length = len(comfirmed_data)

print('Confirmed numbers:')
print(comfirmed_data)
print('Dates:')
print(date_length)

