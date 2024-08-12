FROM jaegertracing/all-in-one:1.29
COPY jaeger-config.yml /etc/jaeger/jaeger-config.yml
EXPOSE 16686 14268
CMD ["--config-file=/etc/jaeger/jaeger-config.yml"]
