import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Load data
df = pd.read_csv("data/mess_data.csv")

# Create label: 1 = High Waste, 0 = Normal
df["label"] = df["waste_kg"].apply(lambda x: 1 if x > 30 else 0)

# Features and target
X = df[["meals_served", "waste_kg"]]
y = df["label"]

# Train model
model = DecisionTreeClassifier()
model.fit(X, y)

# Predict
prediction = model.predict([[200, 40]])

if prediction[0] == 1:
    print("⚠️ High Waste Detected")
else:
    print("✅ Waste is Normal")