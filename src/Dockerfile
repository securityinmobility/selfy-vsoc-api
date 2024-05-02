# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

RUN opentelemetry-bootstrap --action=install

#CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]
ENTRYPOINT ["opentelemetry-instrument"]
CMD ["--traces_exporter", "otlp,console", "--metrics_exporter", "otlp,console", "--logs_exporter", "console", "--exporter_otlp_protocol", "grpc", "--exporter_otlp_endpoint", "opentelemetry-collector:4317", "--exporter_otlp_insecure", "true", "--service_name", "vsoc-api", "flask", "--app", "app.py", "run", "--host=0.0.0.0", "-p", "5002"]

EXPOSE 5002
