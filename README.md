# Proyecto Observabilidad

Este proyecto muestra cómo monitorizar una aplicación Python usando OpenTelemetry y enviar las métricas a Dynatrace para visualización y análisis.

## ¿Qué es OpenTelemetry?

OpenTelemetry (OTel) es un proyecto de código abierto que proporciona un estándar y un conjunto de herramientas para recopilar, procesar y exportar datos de telemetría (trazas, métricas y registros) de aplicaciones y sistemas distribuidos.

## ¿Qué es Dynatrace?

Dynatrace es una plataforma global que combina la observabilidad, AIOps y seguridad de aplicaciones en una única solución. Esta plataforma ayuda a los equipos a innovar más rápido, operar de manera más eficiente y mejorar los resultados de negocio. Dynatrace utiliza inteligencia artificial y automatización para proporcionar respuestas precisas y rápidas a los problemas de rendimiento, seguridad y experiencia de usuario en sus aplicaciones y sistemas.

## Estructura del proyecto

```
proyecto-observabilidad/
├── app/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── .env
└── docker-compose.yml
```

## Requisitos previos

- Docker y Docker compose instalados.

- Python instalado en el sistema.

- Cuenta y acceso a Dynatrace (para obtener el API Token y el endpoint).

## Modificaciones previas a la ejecución del proyecto

Para poder ejecutar el proyecto, se debe de modificar el fichero ```.env```. Se deben de modificar las dos variables, con tu ```TOKEN``` y tu ```ENDPOINT``` personal.

![imagen](https://github.com/albmart2/proyecto-observabilidad/blob/main/capturas/CapturaEnv.jpg)

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

## Comprobación de estado

- Ver contenedores activos:

	```bash
	docker compose ps
	```

- Ver logs de los servicios:

	```bash
	docker compose logs otel-collector
	```

	```bash
	docker compose logs app-python
	```

## Ver métricas

- URL típica: ```https://<TU_ENTORNO>.live.dynatrace.com/ui/metrics```.

- Crear un nuevo Dashboards y elegir las métricas necesarias, como por ejemplo, ```http.server.requests``` o ```system.memory.usage```.

## Solución porblemas comunes

|Problema|Solución|
|--------|--------|
|El contenedor se detiene|Revisar logs|
|No aparecen métricas en Dynatrace|Revisar la configuración de endpoints y variables de entorno|
|Error de tipo de métrica|Asegurarse de usar temporality DELTA|

## Gráficas con las métricas recibidas

Aquí se encuentra las gráficas de las métricas recibidas de la app en python creada anteriormente.

![imagen](https://github.com/albmart2/proyecto-observabilidad/blob/main/CapturasGraficas/Dynatrace.jpg)
