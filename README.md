# SELFY VSOC API

This repository holds all source-code and documentation from the SELFY VSOC API.

## Docker

To run the VSOC docker image you need to have Docker version 24.0.2 or higher installed. The following commands will start and run the docker image:

```
# navigate to the src folder
cd src

# build the docker image and assign the tag "vsoc-api"
docker build --tag vsoc-api .

# check if the docker image was build sucessfully 
docker images 

# the result should show somethink like this:
# REPOSITORY          TAG           IMAGE ID       CREATED         SIZE
# vsoc-api            latest        21bf57473b97   9 minutes ago   148MB

# run the vsoc-api and expose (publish) the host’s port 8000 to the container’s port 5000
# both ports must be exposed to allow interaction with our local client
docker run --publish 8000:5000 vsoc-api

# check if the vsoc-api is running
# this must be done in another terminal if you did not start docker in detached mode with -d
curl localhost:8000 

# you should get the following output (version might be changed)
# {"SELFY VSOC":"by THI","version":"v0.1"}
```

➜  src git:(main) docker run -d --name vsoc-api 27276da04e14 tail -F /dev/null 
➜  src git:(main) docker exec -ti vsoc-api bash

