import requests
import json
from math import floor

# data from verkehrsmittel-personenverkehr_2019-uba.png
avg_greenhouse_car_gPkm = 143
avg_greenhouse_train_far_gPkm = 29
avg_greenhouse_train_near_gPkm = 55
avg_greenhouse_bus_far_gPkm = 29
avg_greenhouse_bus_near_gPkm = 80
avg_greenhouse_tram_gPkm = 55
# according to european cyclists foundation
avg_greenhouse_bike_gPkm = 22


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


# execute regularly for rush hour tines (8am, 1pm, 6pm)
def bonus_credit_factor(lat: float, long: float) -> float:
    """calculate factor for bonus credits if air quality is bad, the higher aqi the worse the air quality is
    :params lat: provided latitude
    :params long: provided longitude
    :return: factor for additional credits
    :rtype: float
    """
    current_aqi = get_air_quality(lat, long)

    credit_factor = 1

    if current_aqi > 70:
        credit_factor = 1.01

    elif current_aqi > 90:
        credit_factor = 1.025

    elif current_aqi > 120:
        credit_factor = 1.075

    elif current_aqi > 150:
        credit_factor = 1.15

    return credit_factor


def calc_credits(travel_type: str, distance: float, lat: float, long: float) -> tuple:
    """calculate credits earned depending on travel distance and travel type
    :params travel_type: shows which means of transportation/travel was used
    :params distance: travel distance in km
    :params lat: provided latitude
    :params long: provided longitude
    :return: earned credits, bonus credits and greenhouse gas savings
    :rtype: tuple
    """
    cred_factor = bonus_credit_factor(lat, long)

    # difference between car and means of travel in terms of emission
    if travel_type == "car":
        savings = 0
    elif travel_type == "train-far":
        savings = avg_greenhouse_car_gPkm - avg_greenhouse_train_far_gPkm
    elif travel_type == "train-near":
        savings = avg_greenhouse_car_gPkm - avg_greenhouse_train_near_gPkm
    elif travel_type == "bus-far":
        savings = avg_greenhouse_car_gPkm - avg_greenhouse_bus_far_gPkm
    elif travel_type == "bus-near":
        savings = avg_greenhouse_car_gPkm - avg_greenhouse_bus_near_gPkm
    elif travel_type == "tram":
        savings = avg_greenhouse_car_gPkm - avg_greenhouse_tram_gPkm
    elif travel_type == "bike":
        savings = avg_greenhouse_car_gPkm - avg_greenhouse_bike_gPkm
    elif travel_type == "pedestrian":
        savings = 143
    else:
        print("Invalid travel_type. This travel_type will not grant you credits.")

    # calculate saved emissions and credits
    savings = savings * distance
    credits = savings / 10

    # calculate potential bonus credits dependant on air quality
    bonus_credits = credits * cred_factor - credits
    bonus_credits = floor(bonus_credits)

    credits = floor(credits)

    return credits, bonus_credits, savings
