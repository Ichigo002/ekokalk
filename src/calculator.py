import datetime
from .get_weather import get_weather_for_city

def estimate_solar_power(city_name, actual_daily_kwh):
    """
    Estimate the solar power production based on panel area, panel efficiency, and weather data.
    
    :param weather_data: Weather data dictionary containing cloud cover percentage.
    :return: Estimated energy production in kWh.
    """

    weather_data = get_weather_for_city(city_name=city_name)
    
    sunrise_time = datetime.datetime.fromtimestamp(weather_data['sys']['sunrise'])
    sunset_time = datetime.datetime.fromtimestamp(weather_data['sys']['sunset'])

    
    full_sun_irradiance = 1000  # W/m² (solar irradiance under full sun)
    full_sunlight_hours = (sunset_time - sunrise_time).total_seconds() / 3600  # in hours
    
    cloud_cover = weather_data['clouds']['all']
    
    effective_sunlight_intensity = full_sun_irradiance * (1 - (cloud_cover / 100))
    
    energy_per_hour_under_full_sun = actual_daily_kwh / full_sunlight_hours

    energy_produced_kwh = energy_per_hour_under_full_sun * (effective_sunlight_intensity / full_sun_irradiance)
    
    
    return energy_produced_kwh
