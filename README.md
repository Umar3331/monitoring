# Monitoring, Logging, and Tracing Setup on AWS EC2

## Overview

This document outlines the steps to set up a complete monitoring, logging, and tracing solution on an AWS EC2 instance using the following open-source tools:

- **Prometheus**: For metrics collection and monitoring.
- **Node Exporter**: For exporting system metrics to Prometheus.
- **Fluent Bit**: For log collection and forwarding.
- **Loki**: For storing and querying logs.
- **OpenTelemetry**: For tracing.
- **Jaeger**: For storing and querying traces.
- **Grafana**: For visualizing metrics, logs, and traces.

### Infrastructure
- **AWS EC2 Instance**: Running Ubuntu 20.04
- **Docker**: Used to containerize Prometheus, Fluent Bit, Loki, OpenTelemetry, Jaeger, and Grafana.

---

## 1. Setting Up the Docker Network

### 1.1 Create a Custom Docker Network

To ensure that all services can communicate seamlessly, a custom Docker network named `monitoring-network` is created. This network allows all containers (Prometheus, Fluent Bit, Loki, OpenTelemetry, Jaeger, and Grafana) to interact with each other using service names.

---

## 2. Deploy Prometheus for Metrics Collection

### 2.1 Create Prometheus Configuration

A configuration file is created for Prometheus, defining global settings like the scrape interval and scrape configurations. Scrape configurations specify the endpoints from which Prometheus collects metrics, such as the Node Exporter running on the EC2 instance.

### 2.2 Deploy Prometheus Using Docker

Prometheus is deployed in a Docker container using a Docker Compose file. This file specifies the Prometheus service, including the configuration file mount and the network it will join (`monitoring-network`).

### 2.3 Deploy Node Exporter

Node Exporter is deployed to collect system metrics from the EC2 instance, such as CPU usage, memory usage, disk I/O, and network traffic. These metrics are exposed to Prometheus.

---

## 3. Deploy Fluent Bit for Logs Collection

### 3.1 Create Fluent Bit Configuration

A configuration file is created for Fluent Bit to define how it collects logs from the EC2 instance (e.g., system logs) and where these logs should be sent (e.g., Loki).

### 3.2 Deploy Fluent Bit Using Docker

Fluent Bit is deployed in a Docker container using a Docker Compose file. This setup ensures Fluent Bit is part of the `monitoring-network`, allowing it to send logs to Loki.

---

## 4. Deploy Loki for Log Storage

### 4.1 Deploy Loki Using Docker

Loki is deployed in a Docker container using a Docker Compose file. Loki stores logs forwarded by Fluent Bit and enables querying through Grafana.

---

## 5. Deploy OpenTelemetry for Tracing

### 5.1 Create OpenTelemetry Configuration

A configuration file is created for OpenTelemetry Collector, specifying how it receives traces (e.g., via OTLP) and where it exports them (e.g., to Jaeger).

### 5.2 Deploy OpenTelemetry Using Docker

OpenTelemetry is deployed in a Docker container using a Docker Compose file. This ensures that OpenTelemetry can collect traces from instrumented applications and send them to Jaeger.

---

## 6. Deploy Jaeger for Tracing Storage

### 6.1 Deploy Jaeger Using Docker

Jaeger is deployed in a Docker container using a Docker Compose file. Jaeger stores traces collected by OpenTelemetry and provides an interface for querying and visualizing them.

---

## 7. Set Up Grafana for Visualization

### 7.1 Deploy Grafana Using Docker

Grafana is deployed in a Docker container using a Docker Compose file. Grafana is used to visualize metrics, logs, and traces collected by Prometheus, Loki, and Jaeger.

### 7.2 Configure Grafana

In Grafana, data sources are configured to connect to Prometheus, Loki, and Jaeger. These data sources allow Grafana to query and visualize the data collected by these tools.

### 7.3 Import Grafana Dashboard Templates

Grafana dashboards are created or imported from the Grafana dashboard library. These dashboards visualize the metrics, logs, and traces, providing a comprehensive view of the system’s performance and behavior.

---

## 8. Setting Up Alerts in Prometheus

### 8.1 Create an Alerting Rule File

An alerting rule file is created for Prometheus, specifying conditions under which alerts should be triggered. For example, an alert might be triggered if CPU usage exceeds a certain threshold for a specified period.

### 8.2 Modify the Prometheus Configuration

The alerting rule file is referenced in the Prometheus configuration, enabling Prometheus to evaluate the rules and trigger alerts as necessary.

### 8.3 Reflect Alerts in Grafana

In Grafana, the `ALERTS` metric is used to visualize the status of the alerts configured in Prometheus. This allows for easy monitoring of potential issues in the system.

---

## Conclusion

This setup provides a comprehensive solution for monitoring, logging, and tracing on an AWS EC2 instance using open-source tools. Prometheus handles metrics collection, Fluent Bit collects and forwards logs to Loki, OpenTelemetry collects traces and sends them to Jaeger, and Grafana is used for visualization and alerting. All components are containerized using Docker and communicate over a custom Docker network.

This documentation can serve as a reference for deploying a similar observability stack in other environments or for expanding the current setup with additional features or integrations.

