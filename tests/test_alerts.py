from app.alerts.alert_manager import generate_alerts
from app.healing.auto_healer import perform_auto_healing


def test_cpu_warning_alert():
    metrics = {
        "cpu_usage": 85,
        "memory_usage": 50,
        "disk_usage": 50
    }

    alerts = generate_alerts(metrics)

    assert len(alerts) == 1
    assert alerts[0]["type"] == "CPU"
    assert alerts[0]["severity"] == "WARNING"


def test_cpu_critical_alert():
    metrics = {
        "cpu_usage": 95,
        "memory_usage": 50,
        "disk_usage": 50
    }

    alerts = generate_alerts(metrics)

    assert len(alerts) == 1
    assert alerts[0]["type"] == "CPU"
    assert alerts[0]["severity"] == "CRITICAL"


def test_memory_critical_alert():
    metrics = {
        "cpu_usage": 50,
        "memory_usage": 95,
        "disk_usage": 50
    }

    alerts = generate_alerts(metrics)

    assert len(alerts) == 1
    assert alerts[0]["type"] == "MEMORY"
    assert alerts[0]["severity"] == "CRITICAL"


def test_disk_critical_alert():
    metrics = {
        "cpu_usage": 50,
        "memory_usage": 50,
        "disk_usage": 96
    }

    alerts = generate_alerts(metrics)

    assert len(alerts) == 1
    assert alerts[0]["type"] == "DISK"
    assert alerts[0]["severity"] == "CRITICAL"


def test_auto_healing_for_critical_alert():
    alert = {
        "type": "CPU",
        "severity": "CRITICAL",
        "message": "CPU usage is critically high"
    }

    result = perform_auto_healing(alert)

    assert result["action"] != "none"
    assert result["result"] == "Recovery action recorded"


def test_no_healing_for_warning_alert():
    alert = {
        "type": "CPU",
        "severity": "WARNING",
        "message": "CPU usage is high"
    }

    result = perform_auto_healing(alert)

    assert result["action"] == "none"
    assert result["result"] == "No healing required"
