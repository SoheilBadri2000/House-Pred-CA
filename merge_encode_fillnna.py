import pandas as pd
from sklearn.impute import KNNImputer
from sklearn.neighbors import BallTree

df = pd.read_csv("data/lof/data-lof-2024-05-13.csv")
df_dem = pd.read_csv("data/LocalLogic/Demographics/demographics-2024-05-13.csv")
df_loc = pd.read_csv("data/LocalLogic/Locations/locations-2024-05-13.csv")


df_geo_price = df[["lng", "lat", "price"]]
# Function to calculate average price of 5 nearest neighbors
def calculate_avg_price_5(row, tree, df, k=5):
    # Ensure k is within valid range
    k = min(k, len(df) - 1)  # Ensure k is not greater than number of samples - 1
    # Find the indices of the k nearest neighbors
    dist, ind = tree.query([row[['lng', 'lat']].values], k=k+1)
    # Exclude the sample itself (first nearest neighbor)
    neighbors = ind.flatten()[1:]
    # Get prices of the neighboring houses
    neighbor_prices = df.iloc[neighbors]['price']
    # Calculate average price
    avg_price = neighbor_prices.mean()
    return avg_price

# Create a BallTree for nearest neighbor search based on lng and lat
tree = BallTree(df_geo_price[['lng', 'lat']].values, leaf_size=15)
# Apply the function row-wise to calculate average price of neighbors
avg_price_5 = df_geo_price.apply(lambda row: calculate_avg_price_5(row, tree, df_geo_price), axis=1)
df.insert(2, "avg_price_5", avg_price_5)



# USE THE FOLLOWING FUNCTION FOR TEST DATA
def calculate_average_neighbor_price(lng, lat, df=df, k=5):
    """
    Calculate the average price of the k nearest neighboring houses based on lng and lat.

    Parameters:
    - df (DataFrame): The original dataframe containing 'lng', 'lat', and 'price' columns.
    - lng (float): Longitude of the target location.
    - lat (float): Latitude of the target location.
    - k (int): Number of nearest neighbors to consider (default is 5).

    Returns:
    - float: Average price of the k nearest neighboring houses.
    """
    # Create a BallTree for nearest neighbor search based on lng and lat
    tree = BallTree(df[['lng', 'lat']].values, leaf_size=15)
    print("tree made")

    # Find the indices of the k nearest neighbors (including the sample itself)
    dist, ind = tree.query([[lng, lat]], k=k)
    print("ind made")

    # Extract indices of the neighbors
    neighbors = ind.flatten()

    # Get prices of the neighboring houses
    neighbor_prices = df.iloc[neighbors]['price']
    print(neighbor_prices)

    # Calculate average price of neighboring houses
    avg_price = neighbor_prices.mean()

    return avg_price

# # SAMPLE USE
# target_longitude = -118.41
# target_latitude = 34.05
# average_neighbor_price = calculate_average_neighbor_price(real_estate_df, target_longitude, target_latitude, k=5)
# print(f"Average price of 5 neighboring houses at ({target_longitude}, {target_latitude}): ${average_neighbor_price:.2f}")





if __name__ == "__main__":

    df = pd.merge(df, df_dem, on="id")
    df = pd.merge(df, df_loc, on="id")

    df = df.drop(["id", "id_mls", "agency_name", "agency_type", "property_type", "ownership_type", "land_size", "page_url", "timestamp", "postal_code"], axis=1)

    df["ownership_type_group_ids"] = df["ownership_type_group_ids"].astype("int")
    df["ownership_type_group_ids"] = df["ownership_type_group_ids"].astype("object")

    df_enc = pd.get_dummies(df)

    imputer = KNNImputer(n_neighbors=5)
    columns = df_enc.columns
    df_enc = imputer.fit_transform(df_enc)
    df_enc = pd.DataFrame(df_enc, columns=columns)


    df_enc.to_csv("data/enc/data-enc-2024-05-13.csv", index=False)