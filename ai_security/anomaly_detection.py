import numpy as np
from sklearn.ensemble import IsolationForest

# Example pipeline activity dataset
# columns: [deploy_frequency, cpu_usage, network_requests]
data = np.array([
    [10, 40, 200],
    [12, 42, 210],
    [9, 39, 198],
    [11, 41, 205],
    [50, 90, 800]   # suspicious activity example
])

# Train anomaly detection model
model = IsolationForest(contamination=0.1)

model.fit(data)

# Detect anomalies
predictions = model.predict(data)

for i, p in enumerate(predictions):
    if p == -1:
        print(f"⚠ Anomaly detected in record {i}")
    else:
        print(f"Normal activity {i}")
