import psutil


def check_system_health():
    """
    Check the overall health of the system
    based on CPU, memory, and disk usage.
    """

    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent

    if cpu >= 90 or memory >= 90 or disk >= 95:
        status = "critical"

    elif cpu >= 80 or memory >= 80 or disk >= 85:
        status = "warning"

    else:
        status = "healthy"

    return {
        "status": status,
        "cpu_usage": cpu,
        "memory_usage": memory,
        "disk_usage": disk
    }
