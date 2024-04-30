import pandas as pd
from sklearn.neighbors import BallTree
import pickle
from catboost import CatBoostRegressor

df = pd.read_csv("data/lof/data-lof-2024-04-22.csv")
df_enc = pd.read_csv("data/enc/data-enc-2024-04-22.csv")

df_ON = df_enc[df_enc["province_Ontario"] == True]
df_QC = df_enc[df_enc["province_Quebec"] == True]
df_BC = df_enc[df_enc["province_British Columbia"] == True]
df_AB = df_enc[df_enc["province_Alberta"] == True]
df_SK = df_enc[df_enc["province_Saskatchewan"] == True]
df_MB = df_enc[df_enc["province_Manitoba"] == True]
# East
df_ES = df_enc[(df_enc["province_Nova Scotia"] == True) |
               (df_enc["province_New Brunswick"] == True) |
               (df_enc["province_Newfoundland & Labrador"] == True) |
               (df_enc["province_Prince Edward Island"] == True)]
# North
df_NO = df_enc[(df_enc["province_Yukon"] == True) |
               (df_enc["province_Northwest Territories"] == True)]

df_ON = df_ON.drop(["province_Ontario", "province_Quebec", "province_British Columbia", "province_Alberta", "province_Saskatchewan",
                    "province_Manitoba", "province_Nova Scotia", "province_New Brunswick", "province_Newfoundland & Labrador",
                    "province_Prince Edward Island", "province_Yukon", "province_Northwest Territories"], axis=1)
df_QC = df_QC.drop(["province_Ontario", "province_Quebec", "province_British Columbia", "province_Alberta", "province_Saskatchewan",
                    "province_Manitoba", "province_Nova Scotia", "province_New Brunswick", "province_Newfoundland & Labrador",
                    "province_Prince Edward Island", "province_Yukon", "province_Northwest Territories"], axis=1)
df_BC = df_BC.drop(["province_Ontario", "province_Quebec", "province_British Columbia", "province_Alberta", "province_Saskatchewan",
                    "province_Manitoba", "province_Nova Scotia", "province_New Brunswick", "province_Newfoundland & Labrador",
                    "province_Prince Edward Island", "province_Yukon", "province_Northwest Territories"], axis=1)
df_AB = df_AB.drop(["province_Ontario", "province_Quebec", "province_British Columbia", "province_Alberta", "province_Saskatchewan",
                    "province_Manitoba", "province_Nova Scotia", "province_New Brunswick", "province_Newfoundland & Labrador",
                    "province_Prince Edward Island", "province_Yukon", "province_Northwest Territories"], axis=1)
df_SK = df_SK.drop(["province_Ontario", "province_Quebec", "province_British Columbia", "province_Alberta", "province_Saskatchewan",
                    "province_Manitoba", "province_Nova Scotia", "province_New Brunswick", "province_Newfoundland & Labrador",
                    "province_Prince Edward Island", "province_Yukon", "province_Northwest Territories"], axis=1)
df_MB = df_MB.drop(["province_Ontario", "province_Quebec", "province_British Columbia", "province_Alberta", "province_Saskatchewan",
                    "province_Manitoba", "province_Nova Scotia", "province_New Brunswick", "province_Newfoundland & Labrador",
                    "province_Prince Edward Island", "province_Yukon", "province_Northwest Territories"], axis=1)
df_ES = df_ES.drop(["province_Ontario", "province_Quebec", "province_British Columbia", "province_Alberta",
                    "province_Saskatchewan","province_Manitoba", "province_Yukon", "province_Northwest Territories"], axis=1)
df_NO = df_NO.drop(["province_Ontario", "province_Quebec", "province_British Columbia", "province_Alberta",
                    "province_Saskatchewan", "province_Manitoba", "province_Nova Scotia", "province_New Brunswick",
                    "province_Newfoundland & Labrador", "province_Prince Edward Island"], axis=1)



def create_ball_tree(df):
    tree = BallTree(df[['lng', 'lat']].values, leaf_size=15)
    return tree

# Create and pickle the BallTree
tree = create_ball_tree(df)
with open('pickles/2024-04-22/AvgPrice-2024-04-22.pkl', 'wb') as f:
    pickle.dump(tree, f)



X = df_ON.drop("price", axis=1)
y = df_ON["price"].values.flatten()
cbr = CatBoostRegressor(silent=True)
cbr.fit(X, y)

with open('pickles/2024-04-22/cbr-ON-2024-04-22.pkl', 'wb') as f:
    pickle.dump(cbr, f)
