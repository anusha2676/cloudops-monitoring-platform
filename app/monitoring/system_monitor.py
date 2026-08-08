import psutil


def get_cpu_usage():
    return psutil.cpu_percent(interval=1)


def get_memory_usage():
    memory = psutil.virtual_memory()
    return memory.percent


def get_disk_usage():
    disk = psutil.disk_usage("/")
    return disk.percent


def get_network_usage():
    network = psutil.net_io_counters()

    return {
        "bytes_sent": network.bytes_sent,
        "bytes_received": network.bytes_recv
    }


def get_system_metrics():
    return {
        "cpu_usage": get_cpu_usage(),
        "memory_usage": get_memory_usage(),
        "disk_usage": get_disk_usage(),
        "network": get_network_usage()
    }
