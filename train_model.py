import pandas as pd
from sklearn.linear_model import LinearRegression

# Load data
df = pd.read_csv("data/mess_data.csv")

# Features and target
X = df[["attendance"]]
y = df["meals_served"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Predict
prediction = model.predict([[200]])

print("Predicted meals needed:", prediction[0])