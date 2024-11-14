import requests
import json

TEST_MODE = False # avoid wasting Api request limit
API_KEY = "754d70ba88fe085162116f42fe034878"

def get_lat_lon_values(city_name):
    try:
        if not TEST_MODE:
            url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit={1}&appid={API_KEY}"
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            #print(f"get_lat_lon_values: {data}")
        else:
            jsonstr = "[{'name': 'Wolsztyn', 'local_names': {'ru': 'Вольштын', 'uk': 'Вольштин', 'de': 'Wollstein', 'pl': 'Wolsztyn', 'lt': 'Volštynas'}, 'lat': 52.11725, 'lon': 16.1126622, 'country': 'PL', 'state': 'Greater Poland Voivodeship'}]"
            jsonstr = jsonstr.replace("'", '"')
            data = json.loads(jsonstr)

        return data[0]['lat'], data[0]['lon']


    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
        return None


def get_json_data(latitude, longitude):
    try:
        if not TEST_MODE:
            url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_KEY}"
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            #print(f"get_sunshine_percentage: {data}")
        else:
            jsonstr = "{'coord': {'lon': 16.1127, 'lat': 52.1173}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04d'}], 'base': 'stations', 'main': {'temp': 277.34, 'feels_like': 275.77, 'temp_min': 277.1, 'temp_max': 278.12, 'pressure': 1028, 'humidity': 95, 'sea_level': 1028, 'grnd_level': 1019}, 'visibility': 10000, 'wind': {'speed': 1.82, 'deg': 236, 'gust': 3.53}, 'clouds': {'all': 50}, 'dt': 1731497479, 'sys': {'type': 1, 'id': 1714, 'country': 'PL', 'sunrise': 1731478372, 'sunset': 1731510424}, 'timezone': 3600, 'id': 3081419, 'name': 'Wolsztyn', 'cod': 200}"
            jsonstr = jsonstr.replace("'", '"')
            data = json.loads(jsonstr)


        return data
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
        return None

def get_weather_for_city(city_name):
    v = get_lat_lon_values(city_name)
    return get_json_data(v[0], v[1])