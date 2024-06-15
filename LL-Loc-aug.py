import pandas as pd
import numpy as np
from time import sleep
from random import randint
import requests
import csv


df_house = pd.read_csv("data/lof/data-lof-2024-06-10.csv")
df_loc = pd.read_csv("data/LocalLogic/Locations/locations-2024-06-10.csv")

outstanding_ids = list(set(df_house["id"]) - set(df_loc["id"]))

coords = df_house[df_house['id'].isin(outstanding_ids)][["id", "lng", "lat"]].to_numpy()


def write_to_csv(id, data):

    loc_high_schools = data["high_schools"]["value"] if "high_schools" in data else "0.0"
    loc_primary_schools = data["primary_schools"]["value"] if "primary_schools" in data else "0.0"
    loc_transit_friendly = data["transit_friendly"]["value"] if "transit_friendly" in data else "0.0"
    loc_groceries = data["groceries"]["value"] if "groceries" in data else "0.0"
    loc_wellness = data["wellness"]["value"] if "wellness" in data else "0.0"
    loc_restaurants = data["restaurants"]["value"] if "restaurants" in data else "0.0"
    loc_pedestrian_friendly = data["pedestrian_friendly"]["value"] if "pedestrian_friendly" in data else "0.0"
    loc_greenery = data["greenery"]["value"] if "greenery" in data else "0.0"
    loc_cycling_friendly = data["cycling_friendly"]["value"] if "cycling_friendly" in data else "0.0"
    loc_car_friendly = data["car_friendly"]["value"] if "car_friendly" in data else "0.0"
    loc_vibrant = data["vibrant"]["value"] if "vibrant" in data else "0.0"
    loc_shopping = data["shopping"]["value"] if "shopping" in data else "0.0"
    loc_daycares = data["daycares"]["value"] if "daycares" in data else "0.0"
    loc_nightlife = data["nightlife"]["value"] if "nightlife" in data else "0.0"
    loc_cafes = data["cafes"]["value"] if "cafes" in data else "0.0"
    loc_quiet = data["quiet"]["value"] if "quiet" in data else "0.0"
    loc_parks = data["parks"]["value"] if "parks" in data else "0.0"

    with open (r"data/LocalLogic/Locations/locations-2024-06-10.csv", 'a') as f:
        writer_obj = csv.writer(f)
        writer_obj.writerow([int(id), loc_high_schools, loc_primary_schools, loc_transit_friendly, loc_groceries,
                             loc_wellness, loc_restaurants, loc_pedestrian_friendly, loc_greenery, loc_cycling_friendly,
                             loc_car_friendly, loc_vibrant, loc_shopping, loc_daycares, loc_nightlife, loc_cafes,
                             loc_quiet, loc_parks])



headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0",
    "Accept": "application/json",
    "Accept-Language": "en-CA,en-US;q=0.7,en;q=0.3",
    # "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://locallogic.co/",
    "Authorization": "V3 Ei9J0EgWQDjhJ1Kp1jcmDo7Gn5H6lGZD.e6c5852b-20af-47dd-a198-0792b3d901b0",
    "Origin": "https://locallogic.co",
    "DNT": "1",
    "Sec-GPC": "1",
    "Connection": "keep-alive",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    "TE": "trailers"
}

for id, lng, lat in coords:

    print(f"\nlng: {lng}, lat: {lat}")

    try:
        url_location_scores = f'https://api.locallogic.co/v3/scores?lng={lng}&lat={lat}'
        response = requests.request("GET", url_location_scores, headers=headers,)

        res_json = response.json()
        if "data" in res_json:
            data = res_json["data"]["location"]
            write_to_csv(id, data)
        else:
            print("nothing found")
            with open (r"data/LocalLogic/Locations/locations-2024-06-10.csv", 'a') as f:
                writer_obj = csv.writer(f)
                writer_obj.writerow([int(id), ""])
   
    except Exception as exception:
        print("An exception occurred")
        print(exception)
        with open (r"data/LocalLogic/Locations/locations-2024-06-10.csv", 'a') as f:
            writer_obj = csv.writer(f)
            writer_obj.writerow([int(id), ""])
        # rand = randint(150, 300)
        # print(f"Safety sleep for {rand} secs...")
        # sleep(rand)
        # url_demographics =  f'https://api.locallogic.co/v3/demographics?lng={lng}&lat={lat}&lang=en'
        # response = requests.request("GET", url_demographics, headers=headers,)

        # res_json = response.json()
        # data = res_json["data"]
        # write_to_csv(data)


      # print(json.dumps(res_json, indent=4))

      # with open("locals.json", "w") as f:
      #     json.dump(res_json, f, indent=4)
