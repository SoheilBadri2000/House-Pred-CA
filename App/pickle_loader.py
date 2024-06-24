import pandas as pd
import pickle
import os



print(os.getcwd()) # /home/soheil/codes/House-Pred-CA/House-Pred-CA
df = pd.read_pickle("App/pickles/2024-06-17/Price-2024-06-17.pkl")

with open('App/pickles/2024-06-17/AvgPrice-2024-06-17.pkl', 'rb') as f:
    tree = pickle.load(f)

province_dict = {
    'ontario': 'ON',
    'quebec': 'QC',
    'british columbia': 'BC',
    'alberta': 'AB',
    'manitoba': 'MB',
    'saskatchewan': 'SK',
    'nova scotia': 'NS',
    'new brunswick': 'NB',
    'newfoundland and labrador': 'NL',
    'prince edward island': 'PE',
    'yukon': 'YT',
    'northwest territories': 'NT',
    'nunavut': 'NT' # NU
}

models = {}

# Make a dictionary with provinces as keys and loaded pickles as values
for province,acronym in province_dict.items():
    file_path = f'App/pickles/2024-06-17/cbr-{acronym}-2024-06-17.pkl'
    with open(file_path, 'rb') as f:
        models[province] = pickle.load(f)



def calculate_average_neighbor_price(longitude, latitude, k=5):
    dist, ind = tree.query([[longitude, latitude]], k=k)
    neighbors = ind.flatten()
    neighbor_prices = df.iloc[neighbors]['price']
    avg_price = neighbor_prices.mean()
    return avg_price

# Get feature names from one of the pkl files
with open('App/pickles/2024-06-17/cbr-ON-2024-06-17.pkl', 'rb') as f:
    X_train_columns = pickle.load(f).feature_names_
    

# with open('App/pickles/2024-06-17/cbr-ON-2024-06-17.pkl', 'rb') as f:
#     cbr_ON = pickle.load(f)

# Predict based on province
def eval_price(province, X_test):
    return models[province].predict(X_test.reindex(columns=X_train_columns))[0]