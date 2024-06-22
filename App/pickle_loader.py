import pandas as pd
import pickle
import os



print(os.getcwd()) # /home/soheil/codes/House-Pred-CA/House-Pred-CA
df = pd.read_csv("data/lof/data-lof-2024-04-15.csv")




with open('App/pickles/2024-04-22/AvgPrice-2024-04-22.pkl', 'rb') as f:
    tree = pickle.load(f)

def calculate_average_neighbor_price(longitude, latitude, k=5):
    dist, ind = tree.query([[longitude, latitude]], k=k)
    neighbors = ind.flatten()
    neighbor_prices = df.iloc[neighbors]['price']
    avg_price = neighbor_prices.mean()
    return avg_price

with open('App/pickles/2024-04-22/cbr-ON-2024-04-22.pkl', 'rb') as f:
    X_train_columns = pickle.load(f).feature_names_
    

with open('App/pickles/2024-04-22/cbr-ON-2024-04-22.pkl', 'rb') as f:
    cbr_ON = pickle.load(f)

def eval_ON(X_test):
    print(X_train_columns)
    X_test = X_test.reindex(columns=X_train_columns)
    return cbr_ON.predict(X_test)[0]