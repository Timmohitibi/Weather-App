import requests

API_KEY = "f493235022f117443717201d55ff1d93"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
  data = response.json()
  weather = data['weather'][0]['description']
  
  temperature = round(data["main"]["temp"] - 273.15, 2)

  print("weather",weather)
  print("temperature:", temperature, "celsius")

else:
    print("Failed to fetch data")