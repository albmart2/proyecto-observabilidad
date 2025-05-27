from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter

# Configura el recurso con el nombre del servicio
resource = Resource(attributes={
    "service.name": "demo-python-service"
})

# Inicializa el proveedor de trazas y el exportador OTLP
provider = TracerProvider(resource=resource)
otlp_exporter = OTLPSpanExporter(endpoint="http://localhost:4318/v1/traces")
span_processor = BatchSpanProcessor(otlp_exporter)
provider.add_span_processor(span_processor)
trace.set_tracer_provider(provider)

# Obtiene el tracer
tracer = trace.get_tracer("demo-python-service")

def suma(a, b):
    with tracer.start_as_current_span("suma") as span:
        resultado = a + b
        span.set_attribute("param.a", a)
        span.set_attribute("param.b", b)
        span.set_attribute("resultado", resultado)
        return resultado

if __name__ == "__main__":
    print("Resultado:", suma(5, 7))

