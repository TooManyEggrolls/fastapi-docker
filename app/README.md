# Metrics API
[FastAPI](https://github.com/tiangolo/fastapi) based app for collecting deployment metrics.

## Running the application
Demo versions of this application are deployed to *WIP*. Options for local execution are below.

### uvicorn
If desired, the app can be run directly, without gunicorn or Docker. A remote database is required.

```bash
pip install -r requirements.txt
export DATABASE_HOST=<DATABASE_HOSTNAME>
export DATABASE_PORT=<DATABASA_PORT>
export DATABASE_NAME=<DATABASE_NAME>
export DATABASE_USER=<DATBASE_PASSWORD>
export DATABASE_PASSWORD=<DATABASE_PASSWORD>
uvicorn app.main:app
```

After launch the openapi spec can be browsed at:
<http://localhost:80/docs>

### docker-compose
This compose file will spin up an instance of the API at localhost:80, as well as a psql database with persistent local disks at localhost:5432.

```yml
version: "3.9"
services:
  database:
    image: postgres
    ports:
      - "5432:5432"
    volumes:
      - ./data/db:/var/lib/postgresql/data
    environment:
      - POSTGRES_DB=postgres
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=testpass123
  web:
    build: .
    ports:
      - "80:80"
    environment:
      - DATABASE_HOST=database
      - DATABASE_PORT=5432
      - DATABASE_USER=postgres
      - DATABASE_PASSWORD=testpass123
      - DATABASE_NAME=postgres
```
Build and run the containers:
```bash
docker-compose build
docker-compose create
docker-compose start
```

After launch the openapi spec can be browsed at:
<http://localhost:80/docs>
