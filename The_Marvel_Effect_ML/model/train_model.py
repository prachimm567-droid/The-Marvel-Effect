from pathlib import Path
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

BASE = Path(__file__).resolve().parents[1]
FEATURES = [
    "empathy","leadership","loyalty","risk_taking","strategic_thinking",
    "independence","impulsiveness","moral_reasoning","humor","self_sacrifice"
]

data = pd.read_csv(BASE / "data" / "characters.csv")
scaler = StandardScaler()
X = scaler.fit_transform(data[FEATURES])

model = KNeighborsClassifier(n_neighbors=1)
model.fit(X, data["character"])

print("Dataset loaded successfully!")
print(data)
print("\nKNN model trained successfully!")
