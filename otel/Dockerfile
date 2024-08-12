# Dockerfile in /otel directory

FROM otel/opentelemetry-collector:latest

# Copy the configuration file
COPY otel-collector-config.yaml /etc/otel/config.yaml

# Expose necessary ports
EXPOSE 4317 55680

# Command to run the OpenTelemetry Collector
CMD ["otelcol", "--config=/etc/otel/config.yaml"]

