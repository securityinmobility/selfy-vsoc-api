## Requirements
| Package        | Version
| ---            | ---
| docker-compose | 3.8+
| docker-engine  | 19.03.0+
## Configuration
```sh
$ cd src/elk/
```
Create a *.env* file
```sh
$ touch .env
```
Open the file inside a text editor and paste these parameters into it.\
\
Choose *ELASTIC_PASSWORD* and *KIBANA_PASSWORD*.
```sh
# Password for the 'elastic' user (at least 6 characters)
ELASTIC_PASSWORD=!!!changethis!!!

# Password for the 'kibana_system' user (at least 6 characters)
KIBANA_PASSWORD=!!!changethis!!!

# Version of Elastic products
STACK_VERSION=8.13.0

# Set the cluster name
CLUSTER_NAME=elk-stack

# Set to 'basic'
LICENSE=basic

# Port to expose Elasticsearch HTTP API to the host
ES_PORT=9200

# Port to expose Kibana to the host
KIBANA_PORT=5601

# Increase or decrease based on the available host memory (in bytes)
MEM_LIMIT=1073741824
```
## How to start the ELK stack
After configuration you should be able to run *docker-compose*:
```sh
$ cd src/elk/

$ docker-compose up -d
```
This will pull all the required images and start the containers.\
\
It will also create three volumes
| Volume         | Purpose
| ---            | ---
| elk_certs      | Certificates for HTTPS communication with the Elasticsearch instance
| elk_esdata     | Elasticsearch data
| elk_kibanadata | Kibana data

Once the command has finished running, you can open [Kibana](http://127.0.0.1:5601) inside a browser.\
\
The username is 'elastic' and the password is the one you chose for *ELASTIC_PASSWORD*.
## How to shut it down
```sh
$ cd src/elk/

$ docker-compose down
```
This will stop and delete the containers. The volumes are persistent.
