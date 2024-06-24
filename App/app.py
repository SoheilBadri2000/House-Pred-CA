import requests
import pandas as pd
from pickle_loader import calculate_average_neighbor_price, eval_price
import os


print(os.getcwd()) # /home/soheil/codes/House-Pred-CA/House-Pred-CA


def process_ON(X_json):
    X_test = pd.json_normalize(X_json)
    
    # PREPROCESS THE PROVINCE
    province = (X_test["province"][0]).lower()
    X_test.drop("province", axis=1)

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
        X_test["ownership_type_group_ids_0"] = 1 # Adjust the features
        X_test["ownership_type_group_ids_1"] = 0
        X_test["ownership_type_group_ids_2"] = 0

    X_test = X_test.drop(["Bedrooms", "Partial Bedrooms", "Bathrooms", "Storeys",
                          "Interior Size", "Building Type", "Ownership Type"], axis=1)
    
    return eval_price(province, X_test)
