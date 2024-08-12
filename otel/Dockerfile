# Use the Jaeger All-in-One image as the base
FROM jaegertracing/all-in-one:latest

# Download and install the OpenTelemetry Collector
FROM otel/opentelemetry-collector:latest as otel

# Copy the OpenTelemetry Collector binary and config from the OpenTelemetry image
COPY --from=otel /otelcontribcol /usr/bin/otelcontribcol
COPY otel-collector-config.yaml /etc/otel-collector-config.yaml

# Expose necessary ports
EXPOSE 14250 16686 8889

# Command to start both Jaeger and OpenTelemetry Collector
CMD /usr/bin/otelcontribcol --config=/etc/otel-collector-config.yaml & /go/bin/all-in-one

