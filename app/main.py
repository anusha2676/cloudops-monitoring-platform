from fastapi import FastAPI
from app.monitoring.system_monitor import get_system_metrics
from app.monitoring.health_checker import check_system_health
from app.alerts.alert_manager import generate_alerts

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
    return check_system_health()


@app.get("/metrics")
def metrics():
    return get_system_metrics()


@app.get("/alerts")
def alerts():
    metrics_data = get_system_metrics()
    alerts_data = generate_alerts(metrics_data)

    return {
        "alerts": alerts_data,
        "count": len(alerts_data)
    }
