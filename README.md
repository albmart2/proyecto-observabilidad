# Proyecto Observabilidad

Proyecto de Observabilidad con OpenTelemetry y Dynatrace

## Ejecución del proyecto

Necesitamos tener dos terminales. A continuación vamos a ver como ejecutar el proyecto correctamente:

1. En la primera terminal, debemos de general el docker compose con todas las configuraciones.

	```bash
	docker compose up --build
	```

2. En la segunda terminal, debemos de ejecutar la app para que empieze mandar métricas a Dynatrace.

	```bash
	python3 app.py
	```

## Gráficas con las métricas recibidas
