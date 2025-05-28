# Proyecto Observabilidad

Proyecto de Observabilidad con OpenTelemetry y Dynatrace.

## Modificaciones previas a la ejecución del proyecto

Para poder ejecutar el proyecto, se debe de modificar el fichero ```.env```. Se deben de modificar las dos variables, con tu ```TOKEN``` y tu ```ENDPOINT``` personal.



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

Aquí se encuentra las gráficas de las métricas recibidas de la app en python creada anteriormente.

![imagen](https://github.com/albmart2/proyecto-observabilidad/blob/main/CapturasGraficas/Dynatrace.jpg)
