# integracion con HubSpot y ClickUp

## Acerca del proyecto
Integración de Python y el framework FastAPI con PostgreSQL, HubSpot y ClickUp.

## Caratecristica
1. API Endpoints: 
```sh
/clickup    method: GET - POST
```
```sh
/hubspot    method: GET - POST
```
2. El sistema siempre guarda todas las peticiones realizadas a los endpoint GET y POST.

### Variables de entorno
Se deben de crear las siguiente variables de entorno con sus respectivos datos:
1. ACCESS_TOKEN_HUBSPOT
2. TOKEN_CLICKUP
3. LIST_ID_CLICKUP
4. DB_HOST
5. DB_PORT
6. DB_USER
7. DB_PASS
8. DB_NAME

### Construido con
* Lenguaje: Python3.10.5
* Framework: FastApi
* Base de dato: PostgreSQL

### Intalacion 

1. Instalar virtualEnv e instalarlo
```sh
$ virtualenv -p python3 venv
```
```sh
$ source venv/bin/activate
```
2. Instalar requirements.txt
```sh
$ pip3 install -r requirements.txt
```
### Correr servidor

```sh
$ uvicorn config:app --host=localhost --port=8001 --reload
```

### Documentacion de la API

La documentacion esta hecha cumpliendo los estadares de OpenAPI con ayuda del framework FastAPI y la libreria BaseModel.

La ruta de la documentacion se encuentra disponible en http://localhost:8001/docs