from app.models import Metric


def save_metrics(db, metrics):
    network = metrics.get("network", {})

    metric = Metric(
        cpu_usage=metrics.get("cpu_usage", 0),
        memory_usage=metrics.get("memory_usage", 0),
        disk_usage=metrics.get("disk_usage", 0),
        bytes_sent=network.get("bytes_sent", 0),
        bytes_received=network.get("bytes_received", 0)
    )

    db.add(metric)
    db.commit()
    db.refresh(metric)

    return metric
