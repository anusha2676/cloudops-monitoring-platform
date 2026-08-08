from app.database import Base, engine, SessionLocal
from app.services.metric_service import save_metrics
from app.services.alert_service import save_alerts


def setup_database():
    Base.metadata.create_all(bind=engine)


def test_save_metrics():
    setup_database()

    db = SessionLocal()

    metrics = {
        "cpu_usage": 45,
        "memory_usage": 50,
        "disk_usage": 60,
        "network": {
            "bytes_sent": 1000,
            "bytes_received": 2000
        }
    }

    metric = save_metrics(db, metrics)

    assert metric.id is not None
    assert metric.cpu_usage == 45
    assert metric.memory_usage == 50
    assert metric.disk_usage == 60

    db.close()


def test_save_alerts():
    setup_database()

    db = SessionLocal()

    alerts = [
        {
            "type": "CPU",
            "severity": "CRITICAL",
            "message": "CPU usage is critically high"
        }
    ]

    saved_alerts = save_alerts(db, alerts)

    assert len(saved_alerts) == 1
    assert saved_alerts[0].id is not None
    assert saved_alerts[0].alert_type == "CPU"
    assert saved_alerts[0].severity == "CRITICAL"

    db.close()
