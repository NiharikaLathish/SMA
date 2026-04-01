import pandas as pd
import numpy as np

days = 100

data = {
    "day": np.arange(days),
    "attendance": np.random.randint(100, 300, days),
    "meals_served": np.random.randint(90, 280, days),
    "waste_kg": np.random.uniform(5, 50, days)
}

df = pd.DataFrame(data)

import os
os.makedirs("data", exist_ok=True)

df.to_csv("data/mess_data.csv", index=False)

print("✅ Data generated and saved to data/mess_data.csv")