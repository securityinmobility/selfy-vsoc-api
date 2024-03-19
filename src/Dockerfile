# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

RUN opentelemetry-bootstrap --action=install

#CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]
CMD ["opentelemetry-instrument", "--traces_exporter", "console", "--metrics_exporter", "console", "--logs_exporter", "console", "--service_name", "vsoc-api", "flask", "--app", "app.py", "run", "--host=0.0.0.0", "-p", "5002"]

EXPOSE 5002
