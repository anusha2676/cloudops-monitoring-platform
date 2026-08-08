from app.models import Alert


def save_alerts(db, alerts):
    saved_alerts = []

    for alert_data in alerts:
        alert = Alert(
            alert_type=alert_data.get("type"),
            severity=alert_data.get("severity"),
            message=alert_data.get("message"),
            status="active"
        )

        db.add(alert)
        saved_alerts.append(alert)

    db.commit()

    for alert in saved_alerts:
        db.refresh(alert)

    return saved_alerts
