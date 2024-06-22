import requests
import pandas as pd
from pickle_loader import calculate_average_neighbor_price, eval_ON
import os


print(os.getcwd()) # /home/soheil/codes/House-Pred-CA/House-Pred-CA

# lng = -79.7953955
# lat = 43.2172796

# bathrooms_total = 2
# bedrooms = 2
# bedrooms_extra = 0
# stories_total = 1
# size_interior = 1000
# parkings = 1

# building_type_Apartment = 1
# building_type_House = 0
# building_type_Row_Townhouse = 0
# building_type_Semi_Detached = 0

# ownership_type_group_ids_0 = 0
# ownership_type_group_ids_1 = 0
# ownership_type_group_ids_2 = 1



# url_dem =  f'https://api.locallogic.co/v3/demographics?lng={lng}&lat={lat}&lang=en'
# url_loc = f'https://api.locallogic.co/v3/scores?lng={lng}&lat={lat}'


# # querystring = {"lng":"-79.378075","lat":"43.644229","lang":"en"}

# headers = {
#     "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0",
#     "Accept": "application/json",
#     "Accept-Language": "en-CA,en-US;q=0.7,en;q=0.3",
#     # "Accept-Encoding": "gzip, deflate, br",
#     "Referer": "https://locallogic.co/",
#     "Authorization": "V3 Ei9J0EgWQDjhJ1Kp1jcmDo7Gn5H6lGZD.e6c5852b-20af-47dd-a198-0792b3d901b0",
#     "Origin": "https://locallogic.co",
#     "DNT": "1",
#     "Sec-GPC": "1",
#     "Connection": "keep-alive",
#     "Sec-Fetch-Dest": "empty",
#     "Sec-Fetch-Mode": "cors",
#     "Sec-Fetch-Site": "same-site",
#     "TE": "trailers"
# }

# response_dem = requests.request("GET", url_dem, headers=headers,)
# json_dem = response_dem.json()
# data_dem = json_dem["data"]["attributes"]

# response_loc = requests.request("GET", url_loc, headers=headers,)
# json_loc = response_loc.json()
# data_loc = json_loc["data"]["location"]





# avg_price_5 = calculate_average_neighbor_price(lng, lat, k=5)
# print(avg_price_5)

# household_income = data_dem["income"]["variables"][0]["value"]
# individual_income = data_dem["income"]["variables"][0]["value"]
# commute_transit = data_dem["commute_mode"]["variables"][0]["value"]
# commute_foot = data_dem["commute_mode"]["variables"][1]["value"]
# commute_bicycle = data_dem["commute_mode"]["variables"][2]["value"]
# commute_drive = data_dem["commute_mode"]["variables"][3]["value"]
# single_family = data_dem["household_composition"]["variables"][0]["value"]
# multi_family = data_dem["household_composition"]["variables"][1]["value"]
# single_person = data_dem["household_composition"]["variables"][2]["value"]
# multi_person = data_dem["household_composition"]["variables"][3]["value"]
# total_individuals = data_dem["population_total"]["variables"][0]["value"]
# age_0_to_4 = data_dem["population_age"]["variables"][0]["value"]
# age_5_to_9 = data_dem["population_age"]["variables"][1]["value"]
# age_10_to_14 = data_dem["population_age"]["variables"][2]["value"]
# age_15_to_19 = data_dem["population_age"]["variables"][3]["value"]
# age_20_to_34 = data_dem["population_age"]["variables"][4]["value"]
# age_35_to_49 = data_dem["population_age"]["variables"][5]["value"]
# age_50_to_64 = data_dem["population_age"]["variables"][6]["value"]
# age_65_to_79 = data_dem["population_age"]["variables"][7]["value"]
# age_80_plus = data_dem["population_age"]["variables"][8]["value"]
# owners = data_dem["housing_tenancy"]["variables"][0]["value"]
# renters = data_dem["housing_tenancy"]["variables"][1]["value"]
# lang_en_only = data_dem["official_language_knowledge"]["variables"][0]["value"]
# lang_fr_only = data_dem["official_language_knowledge"]["variables"][1]["value"]
# lang_en_and_fr = data_dem["official_language_knowledge"]["variables"][2]["value"]
# lang_other = data_dem["official_language_knowledge"]["variables"][3]["value"]
# edu_no_high_school = data_dem["education_level"]["variables"][0]["value"]
# edu_high_school = data_dem["education_level"]["variables"][1]["value"]
# edu_trade_certificate = data_dem["education_level"]["variables"][2]["value"]
# edu_college_certificate = data_dem["education_level"]["variables"][3]["value"]
# edu_university_certificate = data_dem["education_level"]["variables"][4]["value"]
# edu_bachelor_degree = data_dem["education_level"]["variables"][5]["value"]
# edu_post_graduate_degree = data_dem["education_level"]["variables"][6]["value"]
# household_children = data_dem["household_children"]["variables"][0]["value"]
# area_single_detached = data_dem["housing_type"]["variables"][0]["value"]
# area_semi_detached = data_dem["housing_type"]["variables"][1]["value"]
# area_duplex = data_dem["housing_type"]["variables"][2]["value"]
# area_row_houses = data_dem["housing_type"]["variables"][3]["value"]
# area_apt_1_to_4_floors = data_dem["housing_type"]["variables"][4]["value"]
# area_apt_5_plus_floors = data_dem["housing_type"]["variables"][5]["value"]

# loc_high_schools = data_loc["high_schools"]["value"] if "high_schools" in data_loc else "0.0"
# loc_primary_schools = data_loc["primary_schools"]["value"] if "primary_schools" in data_loc else "0.0"
# loc_transit_friendly = data_loc["transit_friendly"]["value"] if "transit_friendly" in data_loc else "0.0"
# loc_groceries = data_loc["groceries"]["value"] if "groceries" in data_loc else "0.0"
# loc_wellness = data_loc["wellness"]["value"] if "wellness" in data_loc else "0.0"
# loc_restaurants = data_loc["restaurants"]["value"] if "restaurants" in data_loc else "0.0"
# loc_pedestrian_friendly = data_loc["pedestrian_friendly"]["value"] if "pedestrian_friendly" in data_loc else "0.0"
# loc_greenery = data_loc["greenery"]["value"] if "greenery" in data_loc else "0.0"
# loc_cycling_friendly = data_loc["cycling_friendly"]["value"] if "cycling_friendly" in data_loc else "0.0"
# loc_car_friendly = data_loc["car_friendly"]["value"] if "car_friendly" in data_loc else "0.0"
# loc_vibrant = data_loc["vibrant"]["value"] if "vibrant" in data_loc else "0.0"
# loc_shopping = data_loc["shopping"]["value"] if "shopping" in data_loc else "0.0"
# loc_daycares = data_loc["daycares"]["value"] if "daycares" in data_loc else "0.0"
# loc_nightlife = data_loc["nightlife"]["value"] if "nightlife" in data_loc else "0.0"
# loc_cafes = data_loc["cafes"]["value"] if "cafes" in data_loc else "0.0"
# loc_quiet = data_loc["quiet"]["value"] if "quiet" in data_loc else "0.0"
# loc_parks = data_loc["parks"]["value"] if "parks" in data_loc else "0.0"



# X_test = pd.DataFrame(
#     [[avg_price_5, bathrooms_total, bedrooms_extra, bedrooms,
#     stories_total, size_interior, lng, lat, parkings,
#     household_income, individual_income, commute_transit,
#     commute_foot, commute_bicycle, commute_drive, single_family,
#     multi_family, single_person, multi_person, total_individuals,
#     age_0_to_4, age_5_to_9, age_10_to_14, age_15_to_19,
#     age_20_to_34, age_35_to_49, age_50_to_64, age_65_to_79,
#     age_80_plus, owners, renters, lang_en_only, lang_fr_only,
#     lang_en_and_fr, lang_other, edu_no_high_school, edu_high_school,
#     edu_trade_certificate, edu_college_certificate,
#     edu_university_certificate, edu_bachelor_degree,
#     edu_post_graduate_degree, household_children,
#     area_single_detached, area_semi_detached, area_duplex,
#     area_row_houses, area_apt_1_to_4_floors, area_apt_5_plus_floors,
#     loc_high_schools, loc_primary_schools, loc_transit_friendly,
#     loc_groceries, loc_wellness, loc_restaurants,
#     loc_pedestrian_friendly, loc_greenery, loc_cycling_friendly,
#     loc_car_friendly, loc_vibrant, loc_shopping, loc_daycares,
#     loc_nightlife, loc_cafes, loc_quiet, loc_parks,
#     building_type_Apartment, building_type_House,
#     building_type_Row_Townhouse, building_type_Semi_Detached,
#     ownership_type_group_ids_0, ownership_type_group_ids_1,
#     ownership_type_group_ids_2]],

#     columns= ['avg_price_5', 'bathrooms_total', 'bedrooms_extra', 'bedrooms',
#        'stories_total', 'size_interior', 'lng', 'lat', 'parkings',
#        'household_income', 'individual_income', 'commute_transit',
#        'commute_foot', 'commute_bicycle', 'commute_drive', 'single_family',
#        'multi_family', 'single_person', 'multi_person', 'total_individuals',
#        'age_0_to_4', 'age_5_to_9', 'age_10_to_14', 'age_15_to_19',
#        'age_20_to_34', 'age_35_to_49', 'age_50_to_64', 'age_65_to_79',
#        'age_80_plus', 'owners', 'renters', 'lang_en_only', 'lang_fr_only',
#        'lang_en_and_fr', 'lang_other', 'edu_no_high_school', 'edu_high_school',
#        'edu_trade_certificate', 'edu_college_certificate',
#        'edu_university_certificate', 'edu_bachelor_degree',
#        'edu_post_graduate_degree', 'household_children',
#        'area_single_detached', 'area_semi_detached', 'area_duplex',
#        'area_row_houses', 'area_apt_1_to_4_floors', 'area_apt_5_plus_floors',
#        'loc_high_schools', 'loc_primary_schools', 'loc_transit_friendly',
#        'loc_groceries', 'loc_wellness', 'loc_restaurants',
#        'loc_pedestrian_friendly', 'loc_greenery', 'loc_cycling_friendly',
#        'loc_car_friendly', 'loc_vibrant', 'loc_shopping', 'loc_daycares',
#        'loc_nightlife', 'loc_cafes', 'loc_quiet', 'loc_parks',
#        'building_type_Apartment', 'building_type_House',
#        'building_type_Row / Townhouse', 'building_type_Semi-Detached',
#        'ownership_type_group_ids_0.0', 'ownership_type_group_ids_1.0',
#        'ownership_type_group_ids_2.0']
# )

# buildingTypes = [
#   "House",
#   "Apartment",
#   "Row/Townhouse",
#   "Semi-Detached",
# ]

# ownershipTypes = [
#   "Freehold",
#   "Strata/Condo",
#   "Other",
# ]

def process_ON(X_json):
    X_test = pd.json_normalize(X_json)
    
    # PREPROCESS THE PROVINCE

    X_test["avg_price_5"] = calculate_average_neighbor_price(X_json["lng"], X_json["lat"], k=5)

    X_test["bedrooms"] = X_test["Bedrooms"]
    X_test["bedrooms_extra"] = X_test["Partial Bedrooms"]
    X_test["bathrooms_total"] = X_test["Bathrooms"]
    X_test["stories_total"] = X_test["Storeys"]
    X_test["size_interior"] = X_test["Interior Size"]
    
    if X_test["Building Type"][0] == "House":
        X_test["building_type_House"] = 1
        X_test["building_type_Apartment"] = 0
        X_test["building_type_Row_Townhouse"] = 0
        X_test["building_type_Semi_Detached"] = 0
    elif X_test["Building Type"][0] == "Apartment":
        X_test["building_type_House"] = 0
        X_test["building_type_Apartment"] = 1
        X_test["building_type_Row_Townhouse"] = 0
        X_test["building_type_Semi_Detached"] = 0
    elif X_test["Building Type"][0] == "Row/Townhouse":
        X_test["building_type_House"] = 0
        X_test["building_type_Apartment"] = 0
        X_test["building_type_Row_Townhouse"] = 1
        X_test["building_type_Semi_Detached"] = 0
    elif X_test["Building Type"][0] == "Semi-Detached":
        X_test["building_type_House"] = 0
        X_test["building_type_Apartment"] = 0
        X_test["building_type_Row_Townhouse"] = 0
        X_test["building_type_Semi_Detached"] = 1

    if X_test["Ownership Type"][0] == "Freehold":
        X_test["ownership_type_group_ids_0"] = 0
        X_test["ownership_type_group_ids_1"] = 1
        X_test["ownership_type_group_ids_2"] = 0
    elif X_test["Ownership Type"][0] == "Strata/Condo":
        X_test["ownership_type_group_ids_0"] = 0
        X_test["ownership_type_group_ids_1"] = 0
        X_test["ownership_type_group_ids_2"] = 1
    elif X_test["Ownership Type"][0] == "Other":
        X_test["ownership_type_group_ids_0.0"] = 1 # Adjust the features
        X_test["ownership_type_group_ids_1.0"] = 0
        X_test["ownership_type_group_ids_2.0"] = 0

    X_test = X_test.drop(["Bedrooms", "Partial Bedrooms", "Bathrooms", "Storeys",
                          "Interior Size", "Building Type", "Ownership Type"], axis=1)
    
    return eval_ON(X_test)
