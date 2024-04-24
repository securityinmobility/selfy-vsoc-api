# Set-up of Elasticsearch and Kibana
## Requirements
| Package        | Version
| ---            | ---
| docker-compose | 3.0+
| docker-engine  | 19.03.0+
## Configuration
```sh
cd src/elk/
```
Create a `.env` file
```sh
touch .env
```
Open the file inside a text editor and paste the following parameters into it.\
\
Choose `ELASTIC_PASSWORD` and `KIBANA_PASSWORD`.
```sh
# Password for the 'elastic' user (at least 6 characters)
ELASTIC_PASSWORD=changeme

# Password for the 'kibana_system' user (at least 6 characters)
KIBANA_PASSWORD=changemetoo

# Set a secret token for the apm server communication
APM_SECRET_TOKEN=generate_this_token

# The ip address of your apm server
APM_ID_ADDRESS=ip_address

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
This will automatically replace the placeholder token inside the `.env` file with a generated one.\
\
You can also replace the APM IP address with your host IP address with this command:
```sh
sed -i -e "s/APM_IP_ADDRESS=.*/APM_IP_ADDRESS=$(ifconfig | grep -Pio "(?<=inet )\S*" | sed -n -e "2{p;q;}")/g" .env
```
## How to start the ELK stack
After configuration you should be able to run `docker-compose`:
```sh
cd src/elk/
```
```sh
docker-compose up -d
```
This will pull all the required images and start the containers.\
\
It will also create three volumes
| Volume         | Purpose
| ---            | ---
| elk_certs      | Certificates for HTTPS communication with the Elasticsearch instance
| elk_esdata     | Elasticsearch data
| elk_kibanadata | Kibana data

Once the command has finished running, you can open [Kibana](https://localhost:5601) inside a browser. Opening Kibana for the first time will warn you because of the self-signed TLS root certificate; this can be ignored.\
\
The username is 'elastic' and the password is the one you chose for `ELASTIC_PASSWORD`.\
\
The only remaining thing to do is to copy the TLS root certificate from one of the containers.
```sh
cd src/elk/
```
Run this command to pull the `ca.crt` file from a container.
```sh
docker cp elasticsearch:/usr/share/elasticsearch/config/certs/ca/ca.crt .
```
## How to shut it down
```sh
cd src/elk/
```
```sh
docker-compose down
```
This will stop and delete the containers. The volumes are persistent.