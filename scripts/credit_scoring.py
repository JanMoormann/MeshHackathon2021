from math import floor

# data from verkehrsmittel-personenverkehr_2019-uba.png
avg_greenhouse_car_gPkm = 143
avg_greenhouse_train_far_gPkm = 29
avg_greenhouse_train_near_gPkm = 55
avg_greenhouse_bus_far_gPkm = 29
avg_greenhouse_bus_near_gPkm = 80
avg_greenhouse_tram_gPkm = 55


def calc_credits(travel_type: str, distance: float) -> int:
    """calculate credits earned depending on travel distance and travel type
    :params travel_type: shows which means of transportation/travel was used
    :params distance: travel distance in km
    :return: earned credits based on how "clean" you traveled
    :rtype: int
    """
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
        savings = 143
    elif travel_type == "pedestrian":
        savings = 143
    else:
        print("Invalid travel_type. This travel_type will not grant you credits.")

    credits = savings * distance / 10
    credits = floor(credits)

    return credits
