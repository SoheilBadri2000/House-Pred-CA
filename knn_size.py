import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer

df = pd.read_csv("data/aug/data-aug-2024-05-27.csv")
# df = pd.read_csv("data/data_cleaned_ph2.csv")
# df = pd.read_csv("data/data_cleaned_ph1_4.csv")

df["size_interior"] = df["size_interior"].abs()


df_knn = df[['bathrooms_total', 'bedrooms_extra', 'bedrooms',
            'stories_total', 'size_interior', 'building_type',
            'property_type', 'lng', 'lat',
            'ownership_type_group_ids', 'parkings',
            'province', 'price']]

# df_knn = df[df["province"]=="Ontario"].drop(["agency_name", "agency_type", "property_type", "ownership_type", "land_size", "page_url", "timestamp", "postal_code"], axis=1)

# For some reason, some houses have negative size

# set houses with size of 0 or 1 to NaN
df_knn["size_interior"] = df_knn["size_interior"].replace([0,1], np.NaN)

df_knn = pd.get_dummies(df_knn)
columns = df_knn.columns

# print(df_knn.columns)
imputer = KNNImputer(n_neighbors=5)
df_knn = imputer.fit_transform(df_knn)
df_knn = pd.DataFrame(df_knn, columns=columns)

print(df_knn[df_knn["province_Ontario"] == 1].corr(numeric_only=True)["price"].sort_values(ascending=False))

df["size_interior"] = df_knn["size_interior"]
df.to_csv("data/knn/data-knn-2024-05-27.csv", index=False)

