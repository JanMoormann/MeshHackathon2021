import requests
import json


def get_air_quality(lat: float, long: float) -> int:
    """get current air quality for provided latitude and longitude
    :params lat: provided latitude
    :params long: provided longitude
    :return: current air quality
    :rtype: int
    """
    api_key = "60387d28b5cb44a8b87d28b5cbb4a8c7"
    url = f"https://api.weather.com/v3/wx/globalAirQuality?geocode={lat},{long}&language=de-DE&scale=EPA&format=json&apiKey={api_key}"
    response = requests.get(url)
    json_response = json.loads(response.text)
    air_quality = json_response["globalairquality"]["airQualityIndex"]

    return air_quality


def get_price_factor(lat: float, long: float) -> float:
    """determine discount depending on air quality
    :params lat: provided latitude
    :params long: provided longitude
    :return: factor to multiply with ticket price
    :rtype: float
    """
    current_aqi = get_air_quality(lat, long)

    price_factor = 1

    if current_aqi > 70:
        price_factor = 0.99

    elif current_aqi > 90:
        price_factor = 0.975

    elif current_aqi > 120:
        price_factor = 0.925

    elif current_aqi > 150:
        price_factor = 0.85

    return price_factor


# example for Stuttgart
ticket_price = 2
price_factor_adjustment = get_price_factor(48.7758, 9.1829)
actual_price = ticket_price * price_factor_adjustment

print(actual_price)
