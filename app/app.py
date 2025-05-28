import time
import random
import psutil
from opentelemetry import metrics
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.exporter.otlp.proto.http.metric_exporter import OTLPMetricExporter
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader

# 1. Exporter
exporter = OTLPMetricExporter(endpoint="http://otel-collector:4318/v1/metrics")

# 2. MetricReader
reader = PeriodicExportingMetricReader(exporter)

# 3. MeterProvider con el reader
provider = MeterProvider(metric_readers=[reader])

# 4. Registrar el MeterProvider globalmente
metrics.set_meter_provider(provider)

# 5. Obtener el meter y crear la métrica
meter = metrics.get_meter("demo-python-service")
counter = meter.create_counter(
    name="requests.total",
    description="Número total de solicitudes",
    unit="1"
)

request_counter = meter.create_counter(
    name="http.server.requests",
    description="Total number of HTTP requests received.",
    unit="{requests}"
)

# Counter: total de errores
error_counter = meter.create_counter(
    name="http.server.errors",
    description="Total number of HTTP errors.",
    unit="{errors}"
)

# UpDownCounter: peticiones activas
active_requests = meter.create_up_down_counter(
    name="http.server.active_requests",
    description="Number of in-flight requests.",
    unit="{requests}"
)

# Histogram: latencia de peticiones
latency_histogram = meter.create_histogram(
    name="http.server.duration",
    description="Duration of HTTP requests.",
    unit="ms"
)

def get_memory_usage(observer):
    mem = psutil.Process().memory_info().rss
    observer.observe(mem, {})


memory_gauge = meter.create_observable_gauge(
    name="system.memory.usage",
    callbacks=[get_memory_usage],
    description="Memory usage of the application.",
    unit="By"
)

# 3. Simula peticiones en bucle
if __name__ == "__main__":
    while True:
        active_requests.add(1)
        start = time.time()
        status = "200"
        try:
            # Simula una petición que tarda entre 100 y 500 ms
            duration = random.randint(100, 500)
            time.sleep(duration / 1000)
            # Simula error aleatorio
            if random.random() < 0.2:
                status = "500"
                error_counter.add(1, {"http.route": "/api/data", "status": status})
                print("Error en la petición")
            else:
                print("Petición exitosa")
        finally:
            elapsed = int((time.time() - start) * 1000)
            latency_histogram.record(elapsed, {"http.route": "/api/data", "http.method": "GET"})
            request_counter.add(1, {"http.route": "/api/data", "http.method": "GET", "status": status})
            active_requests.add(-1)
        time.sleep(2)