import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression

df = pd.read_csv("house_p.csv")
x = df[["Area", "Bedrooms", "Age"]]
y = df["Price"]

model = LinearRegression()
model.fit(x, y)

with open("house_price_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved successfully.")