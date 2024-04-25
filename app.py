import requests
# from merge_encode_fillnna import calculate_average_neighbor_price
from BallTree import calculate_average_neighbor_price





lng = -79.378075
lat = 43.644229

url_dem =  f'https://api.locallogic.co/v3/demographics?lng={lng}&lat={lat}&lang=en'
url_loc = f'https://api.locallogic.co/v3/scores?lng={lng}&lat={lat}'


# querystring = {"lng":"-79.378075","lat":"43.644229","lang":"en"}

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

response_dem = requests.request("GET", url_dem, headers=headers,)
json_dem = response_dem.json()
data_dem = json_dem["data"]["attributes"]

response_loc = requests.request("GET", url_loc, headers=headers,)
json_loc = response_loc.json()
data_loc = json_loc["data"]["location"]





avg_price_5 = calculate_average_neighbor_price(lng, lat, k=5)
print(avg_price_5)

household_income = data_dem["income"]["variables"][0]["value"]
individual_income = data_dem["income"]["variables"][0]["value"]
commute_transit = data_dem["commute_mode"]["variables"][0]["value"]
commute_foot = data_dem["commute_mode"]["variables"][1]["value"]
commute_bicycle = data_dem["commute_mode"]["variables"][2]["value"]
commute_drive = data_dem["commute_mode"]["variables"][3]["value"]
single_family = data_dem["household_composition"]["variables"][0]["value"]
multi_family = data_dem["household_composition"]["variables"][1]["value"]
single_person = data_dem["household_composition"]["variables"][2]["value"]
multi_person = data_dem["household_composition"]["variables"][3]["value"]
total_individuals = data_dem["population_total"]["variables"][0]["value"]
age_0_to_4 = data_dem["population_age"]["variables"][0]["value"]
age_5_to_9 = data_dem["population_age"]["variables"][1]["value"]
age_10_to_14 = data_dem["population_age"]["variables"][2]["value"]
age_15_to_19 = data_dem["population_age"]["variables"][3]["value"]
age_20_to_34 = data_dem["population_age"]["variables"][4]["value"]
age_35_to_49 = data_dem["population_age"]["variables"][5]["value"]
age_50_to_64 = data_dem["population_age"]["variables"][6]["value"]
age_65_to_79 = data_dem["population_age"]["variables"][7]["value"]
age_80_plus = data_dem["population_age"]["variables"][8]["value"]
owners = data_dem["housing_tenancy"]["variables"][0]["value"]
renters = data_dem["housing_tenancy"]["variables"][1]["value"]
lang_en_only = data_dem["official_language_knowledge"]["variables"][0]["value"]
lang_fr_only = data_dem["official_language_knowledge"]["variables"][1]["value"]
lang_en_and_fr = data_dem["official_language_knowledge"]["variables"][2]["value"]
lang_other = data_dem["official_language_knowledge"]["variables"][3]["value"]
edu_no_high_school = data_dem["education_level"]["variables"][0]["value"]
edu_high_school = data_dem["education_level"]["variables"][1]["value"]
edu_trade_certificate = data_dem["education_level"]["variables"][2]["value"]
edu_college_certificate = data_dem["education_level"]["variables"][3]["value"]
edu_university_certificate = data_dem["education_level"]["variables"][4]["value"]
edu_bachelor_degree = data_dem["education_level"]["variables"][5]["value"]
edu_post_graduate_degree = data_dem["education_level"]["variables"][6]["value"]
household_children = data_dem["household_children"]["variables"][0]["value"]
area_single_detached = data_dem["housing_type"]["variables"][0]["value"]
area_semi_detached = data_dem["housing_type"]["variables"][1]["value"]
area_duplex = data_dem["housing_type"]["variables"][2]["value"]
area_row_houses = data_dem["housing_type"]["variables"][3]["value"]
area_apt_1_to_4_floors = data_dem["housing_type"]["variables"][4]["value"]
area_apt_5_plus_floors = data_dem["housing_type"]["variables"][5]["value"]

loc_high_schools = data_loc["high_schools"]["value"] if "high_schools" in data_loc else "0.0"
loc_primary_schools = data_loc["primary_schools"]["value"] if "primary_schools" in data_loc else "0.0"
loc_transit_friendly = data_loc["transit_friendly"]["value"] if "transit_friendly" in data_loc else "0.0"
loc_groceries = data_loc["groceries"]["value"] if "groceries" in data_loc else "0.0"
loc_wellness = data_loc["wellness"]["value"] if "wellness" in data_loc else "0.0"
loc_restaurants = data_loc["restaurants"]["value"] if "restaurants" in data_loc else "0.0"
loc_pedestrian_friendly = data_loc["pedestrian_friendly"]["value"] if "pedestrian_friendly" in data_loc else "0.0"
loc_greenery = data_loc["greenery"]["value"] if "greenery" in data_loc else "0.0"
loc_cycling_friendly = data_loc["cycling_friendly"]["value"] if "cycling_friendly" in data_loc else "0.0"
loc_car_friendly = data_loc["car_friendly"]["value"] if "car_friendly" in data_loc else "0.0"
loc_vibrant = data_loc["vibrant"]["value"] if "vibrant" in data_loc else "0.0"
loc_shopping = data_loc["shopping"]["value"] if "shopping" in data_loc else "0.0"
loc_daycares = data_loc["daycares"]["value"] if "daycares" in data_loc else "0.0"
loc_nightlife = data_loc["nightlife"]["value"] if "nightlife" in data_loc else "0.0"
loc_cafes = data_loc["cafes"]["value"] if "cafes" in data_loc else "0.0"
loc_quiet = data_loc["quiet"]["value"] if "quiet" in data_loc else "0.0"
loc_parks = data_loc["parks"]["value"] if "parks" in data_loc else "0.0"


print(avg_price_5, household_income, loc_high_schools)

