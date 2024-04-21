import pandas as pd
import numpy as np
from time import sleep
from random import randint
import requests
import csv


df_house = pd.read_csv("data/lof/data-lof-2024-04-15.csv")
df_dem = pd.read_csv("data/LocalLogic/Demographics/demographics-2024-04-15.csv")

outstanding_ids = list(set(df_house["id"]) - set(df_dem["id"]))

coords = df_house[df_house['id'].isin(outstanding_ids)][["id", "lng", "lat"]].to_numpy()



def write_to_csv(id, data):

    household_income = data["income"]["variables"][0]["value"]
    individual_income = data["income"]["variables"][0]["value"]

    commute_transit = data["commute_mode"]["variables"][0]["value"]
    commute_foot = data["commute_mode"]["variables"][1]["value"]
    commute_bicycle = data["commute_mode"]["variables"][2]["value"]
    commute_drive = data["commute_mode"]["variables"][3]["value"]

    single_family = data["household_composition"]["variables"][0]["value"]
    multi_family = data["household_composition"]["variables"][1]["value"]
    single_person = data["household_composition"]["variables"][2]["value"]
    multi_person = data["household_composition"]["variables"][3]["value"]

    total_individuals = data["population_total"]["variables"][0]["value"]

    age_0_to_4 = data["population_age"]["variables"][0]["value"]
    age_5_to_9 = data["population_age"]["variables"][1]["value"]
    age_10_to_14 = data["population_age"]["variables"][2]["value"]
    age_15_to_19 = data["population_age"]["variables"][3]["value"]
    age_20_to_34 = data["population_age"]["variables"][4]["value"]
    age_35_to_49 = data["population_age"]["variables"][5]["value"]
    age_50_to_64 = data["population_age"]["variables"][6]["value"]
    age_65_to_79 = data["population_age"]["variables"][7]["value"]
    age_80_plus = data["population_age"]["variables"][8]["value"]

    owners = data["housing_tenancy"]["variables"][0]["value"]
    renters = data["housing_tenancy"]["variables"][1]["value"]

    lang_en_only = data["official_language_knowledge"]["variables"][0]["value"]
    lang_fr_only = data["official_language_knowledge"]["variables"][1]["value"]
    lang_en_and_fr = data["official_language_knowledge"]["variables"][2]["value"]
    lang_other = data["official_language_knowledge"]["variables"][3]["value"]

    edu_no_high_school = data["education_level"]["variables"][0]["value"]
    edu_high_school = data["education_level"]["variables"][1]["value"]
    edu_trade_certificate = data["education_level"]["variables"][2]["value"]
    edu_college_certificate = data["education_level"]["variables"][3]["value"]
    edu_university_certificate = data["education_level"]["variables"][4]["value"]
    edu_bachelor_degree = data["education_level"]["variables"][5]["value"]
    edu_post_graduate_degree = data["education_level"]["variables"][6]["value"]

    household_children = data["household_children"]["variables"][0]["value"]

    area_single_detached = data["housing_type"]["variables"][0]["value"]
    area_semi_detached = data["housing_type"]["variables"][1]["value"]
    area_duplex = data["housing_type"]["variables"][2]["value"]
    area_row_houses = data["housing_type"]["variables"][3]["value"]
    area_apt_1_to_4_floors = data["housing_type"]["variables"][4]["value"]
    area_apt_5_plus_floors = data["housing_type"]["variables"][5]["value"]

    with open (r"data/LocalLogic/Demographics/demographics-2024-04-15.csv", 'a') as f:
        writer_obj = csv.writer(f)
        writer_obj.writerow([int(id), household_income, individual_income, commute_transit, commute_foot, commute_bicycle,
                            commute_drive, single_family, multi_family, single_person, multi_person, total_individuals,
                            age_0_to_4, age_5_to_9, age_10_to_14, age_15_to_19, age_20_to_34, age_35_to_49,
                            age_50_to_64, age_65_to_79, age_80_plus, owners, renters, lang_en_only, lang_fr_only,
                            lang_en_and_fr, lang_other, edu_no_high_school, edu_high_school, edu_trade_certificate,
                            edu_college_certificate, edu_university_certificate, edu_bachelor_degree, 
                            edu_post_graduate_degree, household_children, area_single_detached, area_semi_detached,
                            area_duplex, area_row_houses, area_apt_1_to_4_floors, area_apt_5_plus_floors])



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
        url_demographics =  f'https://api.locallogic.co/v3/demographics?lng={lng}&lat={lat}&lang=en'
        response = requests.request("GET", url_demographics, headers=headers,)

        res_json = response.json()
        if "data" in res_json:
            data = res_json["data"]["attributes"]
            write_to_csv(id, data)
        else:
            print("nothing found")
            with open (r"data/LocalLogic/Demographics/demographics-2024-04-15.csv", 'a') as f:
                writer_obj = csv.writer(f)
                writer_obj.writerow([int(id), ""])
   
    except Exception as exception:
        print("An exception occurred")
        print(exception)
        with open (r"data/LocalLogic/Demographics/demographics-2024-04-15.csv", 'a') as f:
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
