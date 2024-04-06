import pandas as pd
from sklearn.impute import KNNImputer

df = pd.read_csv("data/lof/data-lof-2024-04-01.csv")
df_dem = pd.read_csv("data/LocalLogic/Demographics/demographics-2024-04-01.csv")
df_loc = pd.read_csv("data/LocalLogic/Locations/locations-2024-04-01.csv")

df = pd.merge(df, df_dem, on="id")
df = pd.merge(df, df_loc, on="id")

df = df.drop(["id", "id_mls", "agency_name", "agency_type", "property_type", "ownership_type", "land_size", "page_url", "timestamp", "postal_code"], axis=1)

df["ownership_type_group_ids"] = df["ownership_type_group_ids"].astype("object")

df_enc = pd.get_dummies(df)

imputer = KNNImputer(n_neighbors=5)
columns = df_enc.columns
df_enc = imputer.fit_transform(df_enc)
df_enc = pd.DataFrame(df_enc, columns=columns)

df_enc.to_csv("data/enc/data-enc-2024-04-01.csv", index=False)