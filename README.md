# AI-Enhanced Zero Trust DevSecOps Demo

This repository demonstrates a lightweight DevSecOps workflow that combines a Flask-based application, AI-driven anomaly detection, containerization, Kubernetes deployment manifests, monitoring configuration, and automated security scanning in CI.

## What this project does

The project provides a simple secure application service and an accompanying AI security module that analyzes pipeline-related metrics to identify unusual behavior. It is intended as a practical example of how DevSecOps principles can be applied in a small, containerized environment.

## Key features

- Flask web service with health and security endpoints
- AI-based anomaly detection using an Isolation Forest model
- Example pipeline metrics dataset for model training and evaluation
- Docker image for running the service in a container
- Kubernetes deployment and service manifests
- Prometheus and Grafana monitoring assets
- GitHub Actions workflow with Python validation and Trivy security scans

## Project structure

```text
.
├── .github/workflows/pipeline.yml
├── ai_security/
│   ├── anomaly_detection.py
│   ├── evaluate_model.py
│   ├── pipeline_metrics.csv
│   └── __pycache__/
├── app/
│   ├── app.py
│   └── requirements.txt
├── docker/
│   └── Dockerfile
├── experiments/
│   └── results.csv
├── kubernetes/
│   ├── deployment.yaml
│   └── service.yaml
├── monitoring/
│   ├── grafana-dashboard.json
│   └── prometheus.yml
└── README.md
```

## Application behavior

The Flask app in [app/app.py](app/app.py) exposes the following endpoints:

- `/` returns a JSON response with a status message and timestamp
- `/health` returns a simple health check response
- `/security` returns a JSON payload describing the Zero Trust and DevSecOps model

The service runs on port 5000 by default.

## AI security module

The scripts in [ai_security/anomaly_detection.py](ai_security/anomaly_detection.py) and [ai_security/evaluate_model.py](ai_security/evaluate_model.py) use scikit-learn’s Isolation Forest implementation to detect anomalies in the sample dataset in [ai_security/pipeline_metrics.csv](ai_security/pipeline_metrics.csv).

The example dataset includes metrics such as:

- deploy frequency
- CPU usage
- network requests

## Local setup

### Prerequisites

- Python 3.10+
- pip
- Docker (optional, for containerized run)
- kubectl (optional, for Kubernetes deployment)

### Install dependencies

```bash
pip install -r app/requirements.txt
```

### Run the Flask application

```bash
python app/app.py
```

Then open http://localhost:5000/ in your browser or use curl:

```bash
curl http://localhost:5000/health
```

### Run the anomaly detection script

```bash
python ai_security/anomaly_detection.py
```

### Evaluate the model

```bash
python ai_security/evaluate_model.py
```

## Docker usage

Build the image:

```bash
docker build -t devsecops-app -f docker/Dockerfile .
```

Run the container:

```bash
docker run -p 5000:5000 devsecops-app
```

## Kubernetes deployment

The Kubernetes manifests in [kubernetes/deployment.yaml](kubernetes/deployment.yaml) and [kubernetes/service.yaml](kubernetes/service.yaml) define a deployment with two replicas and a NodePort service exposing the application.

Apply them with:

```bash
kubectl apply -f kubernetes/deployment.yaml
kubectl apply -f kubernetes/service.yaml
```

## Monitoring

The repository includes monitoring configuration for Prometheus and a basic Grafana dashboard:

- [monitoring/prometheus.yml](monitoring/prometheus.yml) scrapes the app on port 5000
- [monitoring/grafana-dashboard.json](monitoring/grafana-dashboard.json) provides a starter dashboard definition

## CI/CD workflow

The GitHub Actions workflow in [.github/workflows/pipeline.yml](.github/workflows/pipeline.yml) runs on pushes to the main branch and performs:

- dependency installation
- Python syntax validation using py_compile
- Docker image build
- filesystem and image vulnerability scanning with Trivy

## Notes

This repository is a compact demonstration project rather than a production-grade platform. It is designed to show how security checks, monitoring, and AI-based anomaly detection can be wired into a simple CI/CD flow.
