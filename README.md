# FinSight Observer

FinSight Observer is a lightweight system observability agent designed to collect and expose host-level metrics for monitoring and reliability engineering.

## Features

- CPU usage monitoring
- Memory usage monitoring
- Disk usage monitoring
- Network I/O tracking
- Prometheus-compatible metrics endpoint
- Lightweight Python implementation

## Architecture

FinSight Observer runs as a background agent that:

1. Collects system metrics using `psutil`
2. Exposes metrics via an HTTP endpoint
3. Allows Prometheus or other monitoring systems to scrape metrics


## Installation

Clone the repository:


git clone git@github.com:fahdsliman/FinSight-Observer.git
cd FinSight-Observer

## install dependencies

pip install psutil prometheus_client

## Run the observer

python sysmon.py

## Access the metrics

http://localhost:9090/metrics

## Example metrics


finsight_cpu_usage_percent
finsight_memory_usage_percent
finsight_disk_usage_percent
finsight_network_usage_bytes_total


Author 

Fahd Sliman
Site Reliability Engineering / Observability Project
