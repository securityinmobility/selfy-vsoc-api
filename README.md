# SELFY VSOC

This repository holds all source-code and documentation from the SELFY VSOC.

## Content of this README

- [Version history](#version-history)
- [Docker](#docker)
- [Starting the VSOC manually](#starting-the-vsoc-manually)


## Version history 

| Version | Description | Status |
| ------- | ----------- | ------ |
| v0.0.7 | SELFY use-cases | stable |
| v0.0.6 | implemenation of the RSU endpoint and Locust tests for all endpoints | stable |
| v0.0.5 | implemenation of the SOT endpoint | stable |
| v0.0.4 | various fixes, extensions, and documentation  | stable |
| v0.0.3 | supports all interfaces and implements a SIEM (ELK) | stable |
| v0.0.2 | supports all interfaces that are required by the SELFY use-cases. The generated logs are shown in the terminal output. There is currently no SIEM solution connected to the VSOC | deprecated |
| v0.0.1 | basic functionality for some interfaces | deprecated |


## Docker

| Requirements   | Version |
| -------------- | ------- |
| docker         | 24.0.2+ |
| docker-compose | 3.0+    |

First, you will need to build the VSOC docker image.
```
# build the docker image and assign the tag "vsoc-api"
docker build --tag vsoc-api src/

# check if the docker image was build sucessfully 
docker images 

# the result should show something like this:
# REPOSITORY          TAG           IMAGE ID       CREATED         SIZE
# vsoc-api            latest        21bf57473b97   9 minutes ago   148MB
```

### Set-up of Elasticsearch and Kibana
### Configuration
Open the `.env` file inside a text editor.

Choose `ELASTIC_PASSWORD` and `KIBANA_PASSWORD`.
```sh
# Password for the 'elastic' user (at least 6 characters)
ELASTIC_PASSWORD=changeme

# Password for the 'kibana_system' user (at least 6 characters)
KIBANA_PASSWORD=changemetoo

# Set a secret token for the apm server communication
APM_SECRET_TOKEN=generate_this_token

# Version of Elastic products
STACK_VERSION=8.13.2

# Set the cluster name
CLUSTER_NAME=elk-stack

# Set to 'basic' or 'trial' to automatically start the 30-day trial
LICENSE=basic

# Increase or decrease based on the available host memory (in bytes)
MEM_LIMIT=1073741824
```
You can generate the token needed for APM with this command:
```sh
sed -i -e "s/APM_SECRET_TOKEN=.*/APM_SECRET_TOKEN=$(python -c "import secrets; print(secrets.token_urlsafe(32))")/g" .env
```
This will automatically replace the placeholder token inside the `.env` file with a generated one.
### How to start the VSOC stack incl. ELK
After configuration you should be able to run `docker-compose`:
```sh
docker-compose up -d
```
This will pull all the required images and start the containers.

Once the command has finished running, you can check whether the VSOC API is working via curl:
```sh
curl http://localhost:8000

# in case of success this will return
# {"SELFY VSOC":"by THI","version":"v0.2"}
```
You can also now open [Kibana](https://localhost:5601) inside a browser. Opening Kibana for the first time will warn you because of the self-signed TLS root certificate; this can be ignored.

The username is 'elastic' and the password is the one you chose for `ELASTIC_PASSWORD`.

The following volumes will be created:

| Volume          | Purpose                                                 |
| --------------- | ------------------------------------------------------- |
| vsoc_certs      | Certificates for HTTPS communication with the ELK stack |
| vsoc_esdata     | Elasticsearch data                                      |
| vsoc_kibanadata | Kibana data                                             |

### How to shut it down
```sh
docker-compose down
```
This will stop and delete the containers. The volumes are persistent.

➜  src git:(main) docker run -d --name vsoc-api 27276da04e14 tail -F /dev/null 
➜  src git:(main) docker exec -ti vsoc-api bash


## Starting the VSOC manually (not suggested)

You should have installed `python3` and `pip` installed.

First, navigate to the `./src/` folder.
```
cd src/
```

Activate the Python virtual environment.
```
source .vsocapi/bin/activate
```

Install all requirements from the `./src/requirements.txt` file.
```
pip install -r requirements.txt
```

Start the VSOC using while using OpenTelemetry.
```
opentelemetry-instrument --traces_exporter otlp,console --metrics_exporter otlp,console --logs_exporter console --exporter_otlp_protocol grpc --service_name vsoc-api flask run -p 8080
```

The following console output should be shown:
```
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:8080
Press CTRL+C to quit
```

Now, the VSOC is running on localhost (127.0.0.1) and port 8080. You can send requests to the desired endpoint.

For example, the following `curl` request is send by the SOTA environment to the VSOC updating information for an update.
```
curl -H "Content-type: application/json" -X POST -d '{"toolId": 8, "timeStamp": "2023-11-21T06:14:00Z", "vin": "2a910ebe-b39a-4813-9992-373738ab4599", "action": "1", "deviceID": 8, "status": 2, "deviceMetadata": "Such nice metadata"}' http://127.0.0.1:8080/sota/updateInfo
```

Check the terminal output where the VSOC is running. There, you can see logs that are generated by OpenTelemetry.

