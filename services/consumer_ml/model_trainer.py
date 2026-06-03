import pickle
import numpy as np
from sklearn.ensemble import IsolationForest

# Train a dummy Unsupervised Isolation Forest for real-time risk flagging
X_train = np.array([
    # [Quantity, Amount, Is_Status_51]
    [2, 1200, 0], [1, 600, 0], [3, 4500, 0], [5, 5000, 0],
    [100, 45000, 1], [85, 38000, 1], [1, 48000, 1] # Outliers
])

model = IsolationForest(contamination=0.1, random_state=42)
model.fit(X_train)

with open("iso_forest.pkl", "wb") as f:
    pickle.dump(model, f)
print("Scikit-Learn IsolationForest Model serialized and ready.")