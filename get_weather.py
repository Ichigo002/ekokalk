import requests
import json

TEST_MODE = True
API_KEY = "754d70ba88fe085162116f42fe034878"


def get_sunshine_percentage(latitude, longitude):
    try:
        if TEST_MODE:
            url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_KEY}"
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
        else:
            jsonstr = "{'coord': {'lon': -122.4194, 'lat': 37.7749}, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03n'}], 'base': 'stations', 'main': {'temp': 283.01, 'feels_like': 281.17, 'temp_min': 280.83, 'temp_max': 284.2, 'pressure': 1020, 'humidity': 86, 'sea_level': 1020, 'grnd_level': 1016}, 'visibility': 10000, 'wind': {'speed': 3.6, 'deg': 130}, 'clouds': {'all': 40}, 'dt': 1731496393, 'sys': {'type': 2, 'id': 2003880, 'country': 'US', 'sunrise': 1731509311, 'sunset': 1731545988}, 'timezone': -28800, 'id': 5391959, 'name': 'San Francisco', 'cod': 200}"
            data = json.loads(jsonstr)


        cloud_coverage = data['clouds']['all']

        sunshine_percentage = 100 - cloud_coverage

        return sunshine_percentage
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
        return None

# Get and print sunshine percentage
sunshine_percentage_today = get_sunshine_percentage()
print(sunshine_percentage_today)
