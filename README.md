# Weather App

This is a simple Python script that fetches and displays the current weather for a given city using the OpenWeatherMap API.

## Prerequisites
- Python 3.x
- `requests` library installed

## Installation
1. Clone or download the script.
2. Install the required dependencies using:
   ```bash
   pip install requests
   ```

## Usage
1. Replace `API_KEY` with your own API key from [OpenWeatherMap](https://home.openweathermap.org/api_keys).
2. Run the script:
   ```bash
   python weather.py
   ```
3. Enter the city name when prompted.
4. The script will display the current weather description and temperature in Celsius.

## Code Overview
```python
import requests

API_KEY = "your_api_key_here"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data["main"]["temp"] - 273.15, 2)
    print("Weather:", weather)
    print("Temperature:", temperature, "Celsius")
else:
    print("Failed to fetch data")
```

## Troubleshooting
- Ensure you have an active internet connection.
- Verify that the API key is correct and has not expired.
- Check that the city name is correctly spelled.
- If you encounter rate limits, wait a few minutes before making another request.

## License
This project is open-source and available under the MIT License.

## Author
Developed by Timmoh Itibi

