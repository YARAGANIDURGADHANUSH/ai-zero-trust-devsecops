import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.metrics import classification_report


def load_data():
    data = pd.read_csv("ai_security/pipeline_metrics.csv")
    return data


def train_model(data):
    model = IsolationForest(
        n_estimators=100,
        contamination=0.1,
        random_state=42
    )
    model.fit(data)
    return model


def evaluate_model(model, data):
    predictions = model.predict(data)

    # Convert anomaly labels
    predictions = [1 if p == -1 else 0 for p in predictions]

    results = data.copy()
    results["anomaly"] = predictions

    print("\nEvaluation Results:\n")
    print(results)

    return results


def main():
    print("DevSecOps AI Security Evaluation\n")

    data = load_data()

    model = train_model(data)

    evaluate_model(model, data)


if __name__ == "__main__":
    main()
