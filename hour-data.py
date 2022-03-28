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

t = 3600 # set x amount of seconds to wait
writer.writeheader()

for i in range(168):
    response = requests.get(openweather_url) # gets current weather data with a lot of extra info
    row = response.json()['main'] # gets the main weather data
    writer.writerow(row) # writes to csv
    time.sleep(t) # delay timer

f.close()