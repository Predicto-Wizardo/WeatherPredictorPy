import requests
import time
import csv


openweather_url = "https://api.openweathermap.org/data/2.5/weather?lat=43.47&lon=-80.54&units=metric&appid=0b668fb873a34ff03efcfea09de00305"

response = requests.get(openweather_url)

# print(response.json())
#
# for elem in response.json():
#     print(elem)
#     print(response.json()[elem])

f = open('testinput.csv', 'w', newline='')
fieldnames = response.json()['main']
writer = csv.DictWriter(f, fieldnames=fieldnames)

t = 10
writer.writeheader()

for i in range(6):
    response = requests.get(openweather_url)
    row = response.json()['main']

    writer.writerow(row)
    time.sleep(t)