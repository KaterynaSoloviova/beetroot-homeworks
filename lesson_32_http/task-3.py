# Task 3
# The Weather app
# Write a console application which takes as an input a city name and returns current weather in the format of your
# choice. For the current task, you can choose any weather API or website or use https://openweathermap.org
import requests

city = input('Enter city name: ')
key = "bdd2c72c9ab84951b3e20e5c7c2fd852"
url = f"https://api.weatherbit.io/v2.0/current?key={key}&city={city}"

response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    city = data["data"][0]["city_name"]
    temperature = data["data"][0]["temp"]
    precipitates = data["data"][0]["precip"]
    description = data["data"][0]["weather"]["description"]

    print(f"City: {city}")
    print(f"Description: {description}")
    print(f"Temperature: {temperature} ºC")
    print(f"Precipitates: {precipitates} mm")

else:
    print("Invalid City Name")
