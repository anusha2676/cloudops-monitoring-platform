def perform_auto_healing(alert):
    """
    Perform a controlled recovery action
    based on the alert severity.
    """

    severity = alert.get("severity")
    alert_type = alert.get("type")

    if severity != "CRITICAL":
        return {
            "action": "none",
            "result": "No healing required"
        }

    if alert_type == "CPU":
        action = "CPU usage is critical. Recovery action recommended."

    elif alert_type == "MEMORY":
        action = "Memory usage is critical. Recovery action recommended."

    elif alert_type == "DISK":
        action = "Disk usage is critical. Recovery action recommended."

    else:
        action = "Unknown critical condition detected."

    return {
        "action": action,
        "result": "Recovery action recorded"
    }
