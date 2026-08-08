
from fastapi import FastAPI
from app.monitoring.system_monitor import get_system_metrics

app = FastAPI(
    title="CloudOps Monitoring Platform",
    description="Cloud monitoring and auto-healing platform",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "CloudOps Monitoring Platform is running",
        "status": "healthy"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.get("/metrics")
def metrics():
    return get_system_metrics()
