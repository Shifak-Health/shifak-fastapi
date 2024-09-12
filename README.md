# Shifak FastAPI

A repository to host simple fast api application for Shifak to use pretrained LLM.

## Technologies

- **Python** API developed in Python which supports many popular web frameworks.
- **FastAPI** a recent and trendy Python web framework supporting async out-of-the-box and
data validation based on *type hints*.
- **Docker** container platform used to quickly, easily and reliably deploy our web application
into production.

## API Endpoints

This API implements the following routes:

| **Endpoint**     	| **HTTP method**   | **CRUD method** 	| **Description**      	|
|-----------------	|----------------  	|---------------	|----------------------	|
| `/generate`     	| POST           	| INSERT        	| Generate response     |

## Build the API image

```bash
docker compose up
```