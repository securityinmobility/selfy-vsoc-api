### Setting up the ELK stack

- The first step was to find a suitable docker-compose configuration that would be easy to work with in the SELFY environment
- A good example can be retrieved from the [Elastic website](https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html) itself
- To set parameters like the password a separate `.env` file is needed
- The `docker-compose.yml` needed to be modified to run with a single Elasticsearch node and appended with the config for an APM server instance so that you could ingest OpenTelemetry data

### Configuring the OpenTelemetry collector

- A good example for the OpenTelemetry collector configuration can be found on the [Elastic website](https://www.elastic.co/guide/en/observability/current/apm-open-telemetry-direct.html) 
- The `endpoint` field needed to be modified since Flask traces are being sent to a locally hosted APM server on port 8200
- The collector is part of the Docker ELK stack and set-up inside the `docker-compose.yml`

### Changes to the OpenTelemetry instrumentation

The `opentelemetry-instrument` command used to run the Flask app also needs to be changed so that the traces and metrics get sent to the collector. The Dockerfile that is used to build the VSOC API image also needed to be modified.

| Before                     | After                           |
| -------------------------- | ------------------------------- |
| --traces_exporter console  | --traces_exporter otlp,console  |
| --metrics_exporter console | --metrics_exporter otlp,console |
| `new`                      | --exporter_otlp_protocol grpc   |
