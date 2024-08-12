FROM openjdk:11-jre-slim
COPY otel-collector-config.yaml /etc/otel/config.yaml
EXPOSE 4317 55680
CMD ["otelcol", "--config=/etc/otel/config.yaml"]

