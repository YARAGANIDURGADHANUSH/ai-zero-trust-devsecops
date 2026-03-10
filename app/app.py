from flask import Flask, jsonify
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "AI-Enhanced Zero Trust DevSecOps Pipeline",
        "status": "running",
        "timestamp": datetime.datetime.now().isoformat()
    })

@app.route("/health")
def health():
    return jsonify({
        "service": "secure-devsecops-app",
        "status": "healthy"
    })

@app.route("/security")
def security_info():
    return jsonify({
        "security_model": "Zero Trust",
        "pipeline": "DevSecOps",
        "monitoring": "Enabled"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
