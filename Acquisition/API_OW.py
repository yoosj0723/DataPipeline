import requests
import json

# requests.get() == urllib.urlopen()

key = ""

cities = ["Seoul,KR", "Tokyo,JP"]
api = "https://api.openweathermap.org/data/2.5/weather?q={name}&appid={key}"

for name in cities:
    url = api.format(name = name, key=key)
    res = requests.get(url)
    data = json.loads(res.text)

    print(data)
    print('CITY =', data['name'])
    print("Weather =", data['weather'][0]['description'])
    print("MIN Temp =", data['main']['temp_min'])
    print("MAX Temp =", data['main']['temp_max'])
    print("Humidity =", data['main']['humidity'])
    print("Pressure =", data['main']['pressure'])