from fastapi import FastAPI, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request

from sqlalchemy.orm import Session

from app.monitoring.system_monitor import get_system_metrics
from app.monitoring.health_checker import check_system_health
from app.alerts.alert_manager import generate_alerts
from app.healing.auto_healer import perform_auto_healing

from app.database import engine, Base, get_db
from app import models

from app.services.metric_service import save_metrics
from app.services.alert_service import save_alerts


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="CloudOps Monitoring Platform",
    description="Cloud monitoring and auto-healing platform",
    version="1.0.0"
)


templates = Jinja2Templates(
    directory="app/dashboard/templates"
)


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


@app.get("/health")
def health_check():
    return check_system_health()


@app.get("/metrics")
def metrics(db: Session = Depends(get_db)):
    metrics_data = get_system_metrics()

    save_metrics(db, metrics_data)

    return metrics_data


@app.get("/alerts")
def alerts(db: Session = Depends(get_db)):
    metrics_data = get_system_metrics()

    alerts_data = generate_alerts(metrics_data)

    save_alerts(db, alerts_data)

    healing_results = []

    for alert in alerts_data:
        result = perform_auto_healing(alert)

        healing_results.append({
            "alert": alert,
            "healing": result
        })

    return {
        "alerts": alerts_data,
        "count": len(alerts_data),
        "healing_results": healing_results
    }
