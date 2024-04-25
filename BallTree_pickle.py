import pandas as pd
from sklearn.neighbors import BallTree
import pickle

df = pd.read_csv("data/lof/data-lof-2024-04-15.csv")

def create_ball_tree(df):
    """
    Create and return a BallTree for nearest neighbor search based on longitude and latitude.

    Parameters:
    - df (DataFrame): The dataframe containing 'longitude' and 'latitude' columns.

    Returns:
    - BallTree: The BallTree object for nearest neighbor search.
    """
    tree = BallTree(df[['lng', 'lat']].values, leaf_size=15)
    return tree



# Create and pickle the BallTree
tree = create_ball_tree(df)
with open('balltree.pkl', 'wb') as f:
    pickle.dump(tree, f)
