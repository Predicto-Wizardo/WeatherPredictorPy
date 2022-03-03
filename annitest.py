import requests

response = requests.get("https://api.openweathermap.org/data/2.5/weather?lat=35&lon=139&appid= {0b668fb873a34ff03efcfea09de00305}")

print(response)