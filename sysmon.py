"""
FinSight Observer - System Metrics Exporter




This agent collects host-level system metrics and exposes them
via an HTTP endpoint compatible with Prometheus.

Metrics exposed:
- CPU usage (%)
- Memory usage (%)
- Disk usage (%)
- Network I/O (bytes sent + received)


Author: Fahd Sliman
"""

import time
import psutil
import logging
from prometheus_client import start_http_server, Gauge

# ---------------------------------------------------------
# Configurations
# ---------------------------------------------------------

METRICS_PORT = 9090        # Port Prometheus will scrape
COLLECTION_INTERVAL = 1    # Seconds between metric updates

# ---------------------------------------------------------
# Logging setup (helps debugging and production visibility)
# ---------------------------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [FinSight Observer] %(levelname)s: %(message)s"
)

# ---------------------------------------------------------
# Prometheus metric definitions (Gauge = value goes up/down)
# ---------------------------------------------------------

cpu_usage = Gauge(
    "finsight_cpu_usage_percent",
    "CPU usage percentage"
)

memory_usage = Gauge(
    "finsight_memory_usage_percent",
    "Memory usage percentage"
)

disk_usage = Gauge(
    "finsight_disk_usage_percent",
    "Disk usage percentage"
)

network_usage_bytes = Gauge(
    "finsight_network_usage_bytes_total",
    "Total network bytes sent and received since boot"
)

# ---------------------------------------------------------
# Metric collection logic
# ---------------------------------------------------------

def collect_metrics():
    """
    Collect current system metrics using psutil
    and update Prometheus Gauges.
    """

    # CPU
    cpu = psutil.cpu_percent(interval=None)
    cpu_usage.set(cpu)

    # Memory
    memory = psutil.virtual_memory().percent
    memory_usage.set(memory)

    # Disk
    disk = psutil.disk_usage("/").percent
    disk_usage.set(disk)

    # Network
    net = psutil.net_io_counters()
    total_bytes = net.bytes_sent + net.bytes_recv
    network_usage_bytes.set(total_bytes)

    logging.info(
        f"CPU: {cpu}% | Memory: {memory}% | Disk: {disk}% | Net bytes: {total_bytes}"
    )

# ---------------------------------------------------------
# Main service loop
# ---------------------------------------------------------

def main():
    """
    Starts HTTP metrics server and begins metric collection loop.
    """

    # Start Prometheus metrics endpoint
    start_http_server(METRICS_PORT)

    logging.info(
        f"FinSight Observer started. Metrics available at http://localhost:{METRICS_PORT}/metrics"
    )

    # Continuous monitoring loop
    while True:
        collect_metrics()
        time.sleep(COLLECTION_INTERVAL)


# ---------------------------------------------------------
# Entry point
# ---------------------------------------------------------


if __name__ == "__main__":
    main()
