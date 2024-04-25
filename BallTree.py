import pandas as pd
import pickle

df = pd.read_csv("data/lof/data-lof-2024-04-15.csv")
with open('balltree.pkl', 'rb') as f:
    tree = pickle.load(f)

def calculate_average_neighbor_price(longitude, latitude, k=5):
    dist, ind = tree.query([[longitude, latitude]], k=k)
    neighbors = ind.flatten()
    neighbor_prices = df.iloc[neighbors]['price']
    avg_price = neighbor_prices.mean()
    return avg_price

