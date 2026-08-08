from app.monitoring.system_monitor import (
    get_cpu_usage,
    get_memory_usage,
    get_disk_usage,
    get_network_usage,
    get_system_metrics
)


def test_cpu_usage():
    cpu = get_cpu_usage()

    assert isinstance(cpu, (int, float))
    assert 0 <= cpu <= 100


def test_memory_usage():
    memory = get_memory_usage()

    assert isinstance(memory, (int, float))
    assert 0 <= memory <= 100


def test_disk_usage():
    disk = get_disk_usage()

    assert isinstance(disk, (int, float))
    assert 0 <= disk <= 100


def test_network_usage():
    network = get_network_usage()

    assert isinstance(network, dict)
    assert "bytes_sent" in network
    assert "bytes_received" in network


def test_system_metrics():
    metrics = get_system_metrics()

    assert "cpu_usage" in metrics
    assert "memory_usage" in metrics
    assert "disk_usage" in metrics
    assert "network" in metrics
