from flask import Flask  # Import Flask from the flask module
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry import trace

# Set up the tracer provider
trace.set_tracer_provider(TracerProvider())
tracer = trace.get_tracer(__name__)

# Set up the OTLP exporter
otlp_exporter = OTLPSpanExporter(endpoint="http://51.20.6.50/:4317", insecure=True)

# Set up the span processor and add it to the tracer provider
span_processor = BatchSpanProcessor(otlp_exporter)
trace.get_tracer_provider().add_span_processor(span_processor)

# Create the Flask app
app = Flask(__name__)
FlaskInstrumentor().instrument_app(app)

# Define a simple route
@app.route("/")
def hello():
    return "Hello, World!"

# Run the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

