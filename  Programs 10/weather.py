import requests

key = 'cbbd31b75c80115f1149c37d90ff3cdd'

User_city = input("Enter your city: ")

weather_data = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={User_city}&appid={key}')

if weather_data.status_code == 200:
    weather = weather_data.json()['weather'][0]['main']
    temp = weather_data.json()['main']['temp']
    celsius = round(temp - 273)

    print(f"The weather in {User_city} is: {weather}")
    print(f"The temperature in {User_city} is: {celsius}")

else:
    print("City not found")
