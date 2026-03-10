import pandas as pd
from sklearn.ensemble import IsolationForest

def load_data():
    """
    Load pipeline metrics dataset
    """
    try:
        data = pd.read_csv("ai_security/pipeline_metrics.csv")
        print("Dataset loaded successfully")
        print(data.head())
        return data
    except Exception as e:
        print("Error loading dataset:", e)
        return None


def train_model(data):
    """
    Train Isolation Forest model
    """
    model = IsolationForest(
        n_estimators=100,
        contamination=0.1,
        random_state=42
    )

    model.fit(data)
    return model


def detect_anomalies(model, data):
    """
    Predict anomalies in the dataset
    """
    predictions = model.predict(data)

    results = data.copy()
    results["anomaly"] = predictions

    print("\nDetection Results:")
    for index, row in results.iterrows():
        if row["anomaly"] == -1:
            print(f"⚠ Anomaly detected at record {index}: {row.values}")
        else:
            print(f"Normal activity at record {index}")

    return results


def main():
    print("AI Security Module - Pipeline Anomaly Detection")

    data = load_data()

    if data is None:
        return

    model = train_model(data)

    detect_anomalies(model, data)


if __name__ == "__main__":
    main()
