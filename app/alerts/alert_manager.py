def generate_alerts(metrics):
    """
    Generate alerts based on CPU, memory,
    and disk usage thresholds.
    """

    alerts = []

    cpu = metrics.get("cpu_usage", 0)
    memory = metrics.get("memory_usage", 0)
    disk = metrics.get("disk_usage", 0)

    # CPU alerts
    if cpu >= 90:
        alerts.append({
            "type": "CPU",
            "severity": "CRITICAL",
            "message": f"CPU usage is critically high: {cpu}%"
        })
    elif cpu >= 80:
        alerts.append({
            "type": "CPU",
            "severity": "WARNING",
            "message": f"CPU usage is high: {cpu}%"
        })

    # Memory alerts
    if memory >= 90:
        alerts.append({
            "type": "MEMORY",
            "severity": "CRITICAL",
            "message": f"Memory usage is critically high: {memory}%"
        })
    elif memory >= 80:
        alerts.append({
            "type": "MEMORY",
            "severity": "WARNING",
            "message": f"Memory usage is high: {memory}%"
        })

    # Disk alerts
    if disk >= 95:
        alerts.append({
            "type": "DISK",
            "severity": "CRITICAL",
            "message": f"Disk usage is critically high: {disk}%"
        })
    elif disk >= 85:
        alerts.append({
            "type": "DISK",
            "severity": "WARNING",
            "message": f"Disk usage is high: {disk}%"
        })

    return alerts
