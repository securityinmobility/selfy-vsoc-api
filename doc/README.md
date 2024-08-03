*VSOC API v0.0.3*

# VSOC API

This is the documentation of the VSOC API.

# Structure

This document contains general informations about api endpoints. Precise endpoint definitions can be found in the `./endpoint/` directory.

# Gen Docs
Run the following commands to generate the endoint documentation.
```shell
deactivate
python3 -m venv jsonschema
source jsonschema/bin/activate
pip3 install json-schema-for-humans
./gen-doc-endpoints.sh
```
*Note:* Remember to reaktivate the correct venv afterwards

# Responses
Each response contains three properties:
```
{
  "data": "***",
  "statusCode": ***,
  "statusMessage": "***"
}
```
In case everything goes as expected a copy of the received data is sent back in the data block with status code 200. If no JSON was received status code 415 will appear and if the JSON is formatted incorrectly, an error message is transmitted in the data-property with status code 400.


# SOTA (Software over the air)

The endpoint `/sota` describes requests targeting the SOTA infrastructure that runs [Uptane](https://uptane.org/).

## Requesting an update 

In order to request an update the VSOC introduces the function `sota_request_update(vin, action)` that takes the Vehicle Identification Number (`VIN`) and the `action` as an input. The `action` parameter is currently implementing the following keys: 1 update, 0 nothing, 2 tbd.

**Important**: The function is triggered automatically by the VSOC internals without using the HTTP REST interface. So no `POST` or `GET` method is used.

### JSON schema

An example of the request from the VSOC to the SOTA:
```
{
  "toolId": 8,
  "timeStamp": "2023-11-21T06:14:00Z",
  "vin": "2a910ebe-b39a-4813-9992-373738ab4599",
  "action": "1",
  "deviceID": 8,
  "status": 2,
  "deviceMetadata": "Such nice metadata"
}
```

## Update status information
`POST / sota/updateInfo`

The function `sota_receive_info()`describes the HTTP REST `POST` method to send information from the SOTA to the VSOC. This information contains the current status of a requested update.

The function takes no parameters and is constructed by the SOTA infrastructure as a `POST` request towards the VSOC endpoint.

<details>
    <summary>
        <span style="font-size: large; ">Examples</span>
    </summary>
Request
```json

```
Response
```json

```
</details>

# RAS (Remote Attestation Service)


## Remote attestation request 

In order to request an attestation, the VSOC introduces the function `ras_attestation_request(target)` that takes the `target` identified as an input. The `target` parameter is the SELFY tool ID. For example, `ID08` for the VSOC.

**Important**: The function is triggered automatically by the VSOC internals without using the HTTP REST interface. So no `POST` or `GET` method is used.

### JSON schema 

An example request send from the VSOC to the RAS:
```
{  
    "target_tool": "ID19",  
    "verifier": "ID18",  
    "VSOC": "ID08",  
    "nonce": "f9bf78b9a18ce6d46a0cd2b0b86df9da"  
} 
```

## Remote attestation result 
`POST / ras/attestationResult`

The VSOC is introducing an HTTP REST endpoint where the RAS can send a `POST` request containing attestation results. This function is called `ras_attestation_result()` in the VSOC. 

<details>
    <summary>
        <span style="font-size: large; ">Examples</span>
    </summary>
Request
```json

```
Response
```json

```
</details>


# AIS (Artificial Immune System) 

## Changing the configuration 

The VSOC can request to change the configuration of the AIS. For this, the function `ais_change_config(ais_id, config)` is used. The `ais_id` is the unique identified of the AIS and the `config` parameter contain the new configuration.

**Important**: The function is triggered automatically by the VSOC internals without using the HTTP REST interface. So no `POST` or `GET` method is used.

### JSON schema 
```
    "version": "1.0", 
    "action": "set", 
    "target": { 
        "type": "ais", 
        "specifiers": { 
            "ais_id": "<ais-id>"
        } 
    }, 
    "actuator": { 
        "type": "vsoc", 
        "specifiers": { 
            "vsoc_id": "VSOC" 
        } 
    }, 
    "args": "cfg"
```

## Deviation unknown 
`POST / ais/deviationUnknown`

The VSOC also receives information from the AIS. For this, the function `ais_deviation_unknown()` to get information from the AIS for an unknown deviation. The request is a `POST` request from the AIS to the VSOC.

<details>
    <summary>
        <span style="font-size: large; ">Examples</span>
    </summary>
Request:
```json

```
Response
```json

```
</details>

## Deviation known 
`POST / ais/deviationKnown`

The VSOC also receives information from the AIS. For this, the function `ais_deviation_known()` to get information from the AIS for an known deviation. The request is a `POST` request from the AIS to the VSOC.

<details>
    <summary>
        <span style="font-size: large; ">Examples</span>
    </summary>
Request:
```json

```
Response
```json

```
</details>

# VSOC receiving endpoint

The endpoint `/vsoc` implements different endpoints to receive data.

## Trust score 

The path `/vsoc/getTrustScore` implements the endpoint to receive the trust score. It can be requested through a HTTP REST `GET` request and is implemented in the VSOC by the `vsoc_get_trustscore()` function.

<details>
    <summary>
        <code>GET</code> <!-- for example GET or POST -->
        <code><b>/</b></code> 
        <code>vsoc/getTrustScore</code> <!-- Endpoint path -->
    </summary>

#### Parameters
| name      |  type     | data type               | description |
|-----------|-----------|-------------------------|-------------|
| `tbd` | tbd | tbd | tbd |

#### Responses

| http code     | content-type                      | response      |
|---------------|-----------------------------------|---------------|
| `200`         | `application/json`                | `{"code":"200","message":"transmitted successfully"}` |
| `400`         | `application/json`                | `{"code":"400","message":"Bad Request"}` |
| `401`         | `application/json`                | `{"code":"401","message":"Unauthorized"}` |
| `404`         | `application/json`                | `{"code":"404","message":"Not Found"}` |

</details>






# RSU (deprecated)

The roadside unit (RSU) collects data from V2X systems, collects them, and performs analysis. The component sends and receives data.


### RSU status messages (deprecated)

<details>
    <summary>
        <code>POST</code> <!-- for example GET or POST -->
        <code><b>/</b></code> 
        <code>statusMessage</code> <!-- Endpoint path -->
    </summary>

#### Parameters

| name      |  type     | data type               | description |
|-----------|-----------|-------------------------|-------------|
| `rsuDeviceID` |  required  | string | unique ID of the RSU |
| `messageTime` |  required  | string | timestamp of the message in ISO-8601 (UTC) |
| `statusMessage` |  required  | string | data of the status message |

#### Responses

| http code     | content-type                      | response      |
|---------------|-----------------------------------|---------------|
| `200`         | `application/json`                | `{"code":"200","message":"transmitted successfully"}` |
| `400`         | `application/json`                | `{"code":"400","message":"Bad Request"}` |
| `401`         | `application/json`                | `{"code":"401","message":"Unauthorized"}` |
| `404`         | `application/json`                | `{"code":"404","message":"Not Found"}` |

#### Example cURL

```javascript
curl -X POST -H "Content-Type: application/json" --data @post.json http://localhost:8889/
```

#### Example Python3.8+
```python
...
```

#### Status
| Status | Python | 
| ------ | ------ |
| Developed | in app.py|

</details>

<details>
    <summary>
        <code>POST</code> <!-- for example GET or POST -->
        <code><b>/</b></code> 
        <code>securityStatus</code> <!-- Endpoint path -->
    </summary>

#### Parameters
| name      |  type     | data type               | description |
|-----------|-----------|-------------------------|-------------|
| `rsuDeviceID` |  required  | string | unique ID of the RSU |
| `messageTime` |  required  | string | timestamp of the message in ISO-8601 (UTC) |
| `securityStatus` |  required  | string | current security status |

#### Responses

| http code     | content-type                      | response      |
|---------------|-----------------------------------|---------------|
| `200`         | `application/json`                | `{"code":"200","message":"transmitted successfully"}` |
| `400`         | `application/json`                | `{"code":"400","message":"Bad Request"}` |
| `401`         | `application/json`                | `{"code":"401","message":"Unauthorized"}` |
| `404`         | `application/json`                | `{"code":"404","message":"Not Found"}` |

#### Example cURL

```javascript
curl -X POST -H "Content-Type: application/json" --data @post.json http://localhost:8889/
```

#### Example Python3.8+
```python
...
```
</details>

<details>
    <summary>
        <code>POST</code> <!-- for example GET or POST -->
        <code><b>/</b></code> 
        <code>healthCheck</code> <!-- Endpoint path -->
    </summary>

#### Parameters
| name      |  type     | data type               | description |
|-----------|-----------|-------------------------|-------------|
| `rsuDeviceID` |  required  | string | unique ID of the RSU |
| `messageTime` |  required  | string | timestamp of the message in ISO-8601 (UTC) |
| `healthCheck` |  required  | string | result of the health check |

#### Responses

| http code     | content-type                      | response      |
|---------------|-----------------------------------|---------------|
| `200`         | `application/json`                | `{"code":"200","message":"transmitted successfully"}` |
| `400`         | `application/json`                | `{"code":"400","message":"Bad Request"}` |
| `401`         | `application/json`                | `{"code":"401","message":"Unauthorized"}` |
| `404`         | `application/json`                | `{"code":"404","message":"Not Found"}` |

#### Example cURL

```javascript
curl -X POST -H "Content-Type: application/json" --data @post.json http://localhost:8889/
```

#### Example Python3.8+
```python
...
```
</details>

### Safe operational modes (SOM) (deprecated)

<details>
    <summary>
        <code>POST</code> <!-- for example GET or POST -->
        <code><b>/</b></code> 
        <code>lastSOM</code> <!-- Endpoint path -->
    </summary>

#### Parameters
| name      |  type     | data type               | description |
|-----------|-----------|-------------------------|-------------|
| `rsuDeviceID` |  required  | string | unique ID of the RSU |
| `messageTime` |  required  | string | timestamp of the message in ISO-8601 (UTC) |
| `lastSOM` |  required  | string | last used safe operational mode |

#### Responses

| http code     | content-type                      | response      |
|---------------|-----------------------------------|---------------|
| `200`         | `application/json`                | `{"code":"200","message":"transmitted successfully"}` |
| `400`         | `application/json`                | `{"code":"400","message":"Bad Request"}` |
| `401`         | `application/json`                | `{"code":"401","message":"Unauthorized"}` |
| `404`         | `application/json`                | `{"code":"404","message":"Not Found"}` |

#### Example cURL

```javascript
curl -X POST -H "Content-Type: application/json" --data @post.json http://localhost:8889/
```

#### Example Python3.8+
```python
...
```
</details>

<details>
    <summary>
        <code>POST</code> <!-- for example GET or POST -->
        <code><b>/</b></code> 
        <code>currentSOM</code> <!-- Endpoint path -->
    </summary>

#### Parameters
| name      |  type     | data type               | description |
|-----------|-----------|-------------------------|-------------|
| `rsuDeviceID` |  required  | string | unique ID of the RSU |
| `messageTime` |  required  | string | timestamp of the message in ISO-8601 (UTC) |
| `currentSOM` |  required  | string | current safe operational mode in place |

#### Responses

| http code     | content-type                      | response      |
|---------------|-----------------------------------|---------------|
| `200`         | `application/json`                | `{"code":"200","message":"transmitted successfully"}` |
| `400`         | `application/json`                | `{"code":"400","message":"Bad Request"}` |
| `401`         | `application/json`                | `{"code":"401","message":"Unauthorized"}` |
| `404`         | `application/json`                | `{"code":"404","message":"Not Found"}` |

#### Example cURL

```javascript
curl -X POST -H "Content-Type: application/json" --data @post.json http://localhost:8889/
```

#### Example Python3.8+
```python
...
```
</details>

<details>
    <summary>
        <code>GET</code> <!-- for example GET or POST -->
        <code><b>/</b></code> 
        <code>triggerSafeOperationalMode</code> <!-- Endpoint path -->
    </summary>

#### Parameters
| name      |  type     | data type               | description |
|-----------|-----------|-------------------------|-------------|
| `rsuDeviceID` |  required  | string | unique ID of the RSU |
| `messageTime` |  required  | string | timestamp of the message in ISO-8601 (UTC) |
| `currentSOM` |  optional | string | current safe operational mode in place |

#### Responses

| http code     | content-type                      | response      |
|---------------|-----------------------------------|---------------|
| `200`         | `application/json`                | `{"code":"200","message":"transmitted successfully"}` |
| `400`         | `application/json`                | `{"code":"400","message":"Bad Request"}` |
| `401`         | `application/json`                | `{"code":"401","message":"Unauthorized"}` |
| `404`         | `application/json`                | `{"code":"404","message":"Not Found"}` |

#### Example cURL

```javascript
curl -X POST -H "Content-Type: application/json" --data @post.json http://localhost:8889/
```

#### Example Python3.8+
```python
...
```
</details>

<details>
    <summary>
        <code>GET</code> <!-- for example GET or POST -->
        <code><b>/</b></code> 
        <code>triggerMinimumRiskManeuver</code> <!-- Endpoint path -->
    </summary>

#### Parameters
| name      |  type     | data type               | description |
|-----------|-----------|-------------------------|-------------|
| `rsuDeviceID` |  required  | string | unique ID of the RSU |
| `messageTime` |  required  | string | timestamp of the message in ISO-8601 (UTC) |
| `currentSOM` |  optional | string | current safe operational mode in place |

#### Responses

| http code     | content-type                      | response      |
|---------------|-----------------------------------|---------------|
| `200`         | `application/json`                | `{"code":"200","message":"transmitted successfully"}` |
| `400`         | `application/json`                | `{"code":"400","message":"Bad Request"}` |
| `401`         | `application/json`                | `{"code":"401","message":"Unauthorized"}` |
| `404`         | `application/json`                | `{"code":"404","message":"Not Found"}` |

#### Example cURL

```javascript
curl -X POST -H "Content-Type: application/json" --data @post.json http://localhost:8889/
```

#### Example Python3.8+
```python
...
```
</details>


## Virtual vehicle (deprecated)

The control architecture from virtual vehicle (VIF) is able to simulate and collect data from vehicle sources such as in-vehicle data and V2X.

### Vehicle information

<details>
    <summary>
        <code>POST</code> <!-- for example GET or POST -->
        <code><b>/</b></code> 
        <code>egoVehiclePosition</code> <!-- Endpoint path -->
    </summary>

#### Parameters
| name      |  type     | data type               | description |
|-----------|-----------|-------------------------|-------------|
| `vehicleID` |  required  | string | unique ID of the vehicle |
| `messageTime` |  required  | string | timestamp of the message in ISO-8601 (UTC) |
| `egoVehiclePosition` |  required | string | current position of the ego vehicle |

#### Responses

| http code     | content-type                      | response      |
|---------------|-----------------------------------|---------------|
| `200`         | `application/json`                | `{"code":"200","message":"transmitted successfully"}` |
| `400`         | `application/json`                | `{"code":"400","message":"Bad Request"}` |
| `401`         | `application/json`                | `{"code":"401","message":"Unauthorized"}` |
| `404`         | `application/json`                | `{"code":"404","message":"Not Found"}` |

#### Example cURL

```javascript
curl -X POST -H "Content-Type: application/json" --data @post.json http://localhost:8889/
```

#### Example Python3.8+
```python
...
```
</details>

<details>
    <summary>
        <code>POST</code> <!-- for example GET or POST -->
        <code><b>/</b></code> 
        <code>egoVehicleStatus</code> <!-- Endpoint path -->
    </summary>

#### Parameters
| name      |  type     | data type               | description |
|-----------|-----------|-------------------------|-------------|
| `vehicleID` |  required  | string | unique ID of the vehicle |
| `messageTime` |  required  | string | timestamp of the message in ISO-8601 (UTC) |
| `egoVehicleStatus` |  required | string | current status of the ego vehicle |

#### Responses

| http code     | content-type                      | response      |
|---------------|-----------------------------------|---------------|
| `200`         | `application/json`                | `{"code":"200","message":"transmitted successfully"}` |
| `400`         | `application/json`                | `{"code":"400","message":"Bad Request"}` |
| `401`         | `application/json`                | `{"code":"401","message":"Unauthorized"}` |
| `404`         | `application/json`                | `{"code":"404","message":"Not Found"}` |

#### Example cURL

```javascript
curl -X POST -H "Content-Type: application/json" --data @post.json http://localhost:8889/
```

#### Example Python3.8+
```python
...
```
</details>



### Tool information (deprecated)

<details>
    <summary>
        <code>POST</code> <!-- for example GET or POST -->
        <code><b>/</b></code> 
        <code>toolStatus</code> <!-- Endpoint path -->
    </summary>

#### Parameters
| name      |  type     | data type               | description |
|-----------|-----------|-------------------------|-------------|
| `toolID` |  required  | string | unique ID of the tool |
| `messageTime` |  required  | string | timestamp of the message in ISO-8601 (UTC) |
| `toolStatus` |  required | string | current status of the tool |

#### Responses

| http code     | content-type                      | response      |
|---------------|-----------------------------------|---------------|
| `200`         | `application/json`                | `{"code":"200","message":"transmitted successfully"}` |
| `400`         | `application/json`                | `{"code":"400","message":"Bad Request"}` |
| `401`         | `application/json`                | `{"code":"401","message":"Unauthorized"}` |
| `404`         | `application/json`                | `{"code":"404","message":"Not Found"}` |

#### Example cURL

```javascript
curl -X POST -H "Content-Type: application/json" --data @post.json http://localhost:8889/
```

#### Example Python3.8+
```python
...
```
</details>


## Trust data management system (TDMS) (deprecated)

The TDMS is a set of tools holding all relevant assets for data management.

### Healing procedures (deprecated)

<details>
    <summary>
        <code>GET</code> <!-- for example GET or POST -->
        <code><b>/</b></code> 
        <code>healingProcedures</code> <!-- Endpoint path -->
    </summary>

#### Parameters
| name      |  type     | data type               | description |
|-----------|-----------|-------------------------|-------------|
| `toolID` |  optional | string | unique ID of the tool |
| `messageTime` |  required  | string | timestamp of the message in ISO-8601 (UTC) |
| `healingProcedures` |  required | string | current set of healing procedures |

#### Responses

| http code     | content-type                      | response      |
|---------------|-----------------------------------|---------------|
| `200`         | `application/json`                | `{"code":"200","message":"transmitted successfully"}` |
| `400`         | `application/json`                | `{"code":"400","message":"Bad Request"}` |
| `401`         | `application/json`                | `{"code":"401","message":"Unauthorized"}` |
| `404`         | `application/json`                | `{"code":"404","message":"Not Found"}` |

#### Example cURL

```javascript
curl -X POST -H "Content-Type: application/json" --data @post.json http://localhost:8889/
```

#### Example Python3.8+
```python
...
```
</details>

<details>
    <summary>
        <code>POST</code> <!-- for example GET or POST -->
        <code><b>/</b></code> 
        <code>healingProcedures</code> <!-- Endpoint path -->
    </summary>

#### Parameters
| name      |  type     | data type               | description |
|-----------|-----------|-------------------------|-------------|
| `toolID` |  optional | string | unique ID of the tool |
| `messageTime` |  required  | string | timestamp of the message in ISO-8601 (UTC) |
| `healingProcedures` |  required | string | current set of healing procedures |

#### Responses

| http code     | content-type                      | response      |
|---------------|-----------------------------------|---------------|
| `200`         | `application/json`                | `{"code":"200","message":"transmitted successfully"}` |
| `400`         | `application/json`                | `{"code":"400","message":"Bad Request"}` |
| `401`         | `application/json`                | `{"code":"401","message":"Unauthorized"}` |
| `404`         | `application/json`                | `{"code":"404","message":"Not Found"}` |

#### Example cURL

```javascript
curl -X POST -H "Content-Type: application/json" --data @post.json http://localhost:8889/
```

#### Example Python3.8+
```python
...
```
</details>

## VSOC data subscription (deprecated)


Different services one and subscribe to.

### Knowledge  (deprecated)


<details>
    <summary>
        <code>GET</code> <!-- for example GET or POST -->
        <code><b>/</b></code> 
        <code>securityScenario</code> <!-- Endpoint path -->
    </summary>

#### Parameters
| name      |  type     | data type               | description |
|-----------|-----------|-------------------------|-------------|
| `toolID` |  optional | string | unique ID of the tool |
| `messageTime` |  required  | string | timestamp of the message in ISO-8601 (UTC) |
| `securityScenario` |  required | string | current set of security scenarios |

#### Responses

| http code     | content-type                      | response      |
|---------------|-----------------------------------|---------------|
| `200`         | `application/json`                | `{"code":"200","message":"transmitted successfully"}` |
| `400`         | `application/json`                | `{"code":"400","message":"Bad Request"}` |
| `401`         | `application/json`                | `{"code":"401","message":"Unauthorized"}` |
| `404`         | `application/json`                | `{"code":"404","message":"Not Found"}` |

#### Example cURL

```javascript
curl -X POST -H "Content-Type: application/json" --data @post.json http://localhost:8889/
```

#### Example Python3.8+
```python
...
```
</details>

<details>
    <summary>
        <code>GET</code> <!-- for example GET or POST -->
        <code><b>/</b></code> 
        <code>ontology</code> <!-- Endpoint path -->
    </summary>

#### Parameters
| name      |  type     | data type               | description |
|-----------|-----------|-------------------------|-------------|
| `toolID` |  optional | string | unique ID of the tool |
| `messageTime` |  required  | string | timestamp of the message in ISO-8601 (UTC) |
| `ontologyID` | required | string | ID of the requested ontology |

#### Responses

| http code     | content-type                      | response      |
|---------------|-----------------------------------|---------------|
| `200`         | `application/json`                | `{"code":"200","message":"transmitted successfully"}` |
| `400`         | `application/json`                | `{"code":"400","message":"Bad Request"}` |
| `401`         | `application/json`                | `{"code":"401","message":"Unauthorized"}` |
| `404`         | `application/json`                | `{"code":"404","message":"Not Found"}` |

#### Example cURL

```javascript
curl -X POST -H "Content-Type: application/json" --data @post.json http://localhost:8889/
```

#### Example Python3.8+
```python
...
```
</details>

### Security controls  (deprecated)


<details>
    <summary>
        <code>GET</code> <!-- for example GET or POST -->
        <code><b>/</b></code> 
        <code>patchForComponent</code> <!-- Endpoint path -->
    </summary>

#### Parameters
| name      |  type     | data type               | description |
|-----------|-----------|-------------------------|-------------|
| `toolID` |  required | string | unique ID of the tool |
| `messageTime` |  required  | string | timestamp of the message in ISO-8601 (UTC) |
| `currentPatchLevel` | optional | string | current version of the installed patch |

#### Responses

| http code     | content-type                      | response      |
|---------------|-----------------------------------|---------------|
| `200`         | `application/json`                | `{"code":"200","message":"transmitted successfully"}` |
| `400`         | `application/json`                | `{"code":"400","message":"Bad Request"}` |
| `401`         | `application/json`                | `{"code":"401","message":"Unauthorized"}` |
| `404`         | `application/json`                | `{"code":"404","message":"Not Found"}` |

#### Example cURL

```javascript
curl -X POST -H "Content-Type: application/json" --data @post.json http://localhost:8889/
```

#### Example Python3.8+
```python
...
```
</details>

<details>
    <summary>
        <code>GET</code> <!-- for example GET or POST -->
        <code><b>/</b></code> 
        <code>triggerAudit</code> <!-- Endpoint path -->
    </summary>

#### Parameters
| name      |  type     | data type               | description |
|-----------|-----------|-------------------------|-------------|
| `toolID` |  required | string | unique ID of the tool |
| `messageTime` |  required  | string | timestamp of the message in ISO-8601 (UTC) |
| `lastAudit` | optional | string | timestamp of the last audit (ISO-8601 UTC) |

#### Responses

| http code     | content-type                      | response      |
|---------------|-----------------------------------|---------------|
| `200`         | `application/json`                | `{"code":"200","message":"transmitted successfully"}` |
| `400`         | `application/json`                | `{"code":"400","message":"Bad Request"}` |
| `401`         | `application/json`                | `{"code":"401","message":"Unauthorized"}` |
| `404`         | `application/json`                | `{"code":"404","message":"Not Found"}` |

#### Example cURL

```javascript
curl -X POST -H "Content-Type: application/json" --data @post.json http://localhost:8889/
```

#### Example Python3.8+
```python
...
```
</details>

<details>
    <summary>
        <code>GET</code> <!-- for example GET or POST -->
        <code><b>/</b></code> 
        <code>triggerPentest</code> <!-- Endpoint path -->
    </summary>

#### Parameters
| name      |  type     | data type               | description |
|-----------|-----------|-------------------------|-------------|
| `toolID` |  required | string | unique ID of the tool |
| `messageTime` |  required  | string | timestamp of the message in ISO-8601 (UTC) |
| `lastPentest` | optional | string | timestamp of the last pentest (ISO-8601 UTC) |

#### Responses

| http code     | content-type                      | response      |
|---------------|-----------------------------------|---------------|
| `200`         | `application/json`                | `{"code":"200","message":"transmitted successfully"}` |
| `400`         | `application/json`                | `{"code":"400","message":"Bad Request"}` |
| `401`         | `application/json`                | `{"code":"401","message":"Unauthorized"}` |
| `404`         | `application/json`                | `{"code":"404","message":"Not Found"}` |

#### Example cURL

```javascript
curl -X POST -H "Content-Type: application/json" --data @post.json http://localhost:8889/
```

#### Example Python3.8+
```python
...
```
</details>

<details>
    <summary>
        <code>GET</code> <!-- for example GET or POST -->
        <code><b>/</b></code> 
        <code>triggerUpdate</code> <!-- Endpoint path -->
    </summary>

#### Parameters
| name      |  type     | data type               | description |
|-----------|-----------|-------------------------|-------------|
| `toolID` |  required | string | unique ID of the tool |
| `messageTime` |  required  | string | timestamp of the message in ISO-8601 (UTC) |
| `lastUpdate` | optional | string | timestamp of the last update (ISO-8601 UTC) |

#### Responses

| http code     | content-type                      | response      |
|---------------|-----------------------------------|---------------|
| `200`         | `application/json`                | `{"code":"200","message":"transmitted successfully"}` |
| `400`         | `application/json`                | `{"code":"400","message":"Bad Request"}` |
| `401`         | `application/json`                | `{"code":"401","message":"Unauthorized"}` |
| `404`         | `application/json`                | `{"code":"404","message":"Not Found"}` |

#### Example cURL

```javascript
curl -X POST -H "Content-Type: application/json" --data @post.json http://localhost:8889/
```

#### Example Python3.8+
```python
...
```
</details>

### Security information (deprecated)



<details>
    <summary>
        <code>GET</code> <!-- for example GET or POST -->
        <code><b>/</b></code> 
        <code>vehicleTrustScore</code> <!-- Endpoint path -->
    </summary>

#### Parameters
| name      |  type     | data type               | description |
|-----------|-----------|-------------------------|-------------|
| `vehicleID` |  required | string | unique ID of the tool |
| `messageTime` |  required  | string | timestamp of the message in ISO-8601 (UTC) |

#### Responses

| http code     | content-type                      | response      |
|---------------|-----------------------------------|---------------|
| `200`         | `application/json`                | `{"code":"200","message":"transmitted successfully"}` |
| `400`         | `application/json`                | `{"code":"400","message":"Bad Request"}` |
| `401`         | `application/json`                | `{"code":"401","message":"Unauthorized"}` |
| `404`         | `application/json`                | `{"code":"404","message":"Not Found"}` |

#### Example cURL

```javascript
curl -X POST -H "Content-Type: application/json" --data @post.json http://localhost:8889/
```

#### Example Python3.8+
```python
...
```
</details>

<details>
    <summary>
        <code>GET</code> <!-- for example GET or POST -->
        <code><b>/</b></code> 
        <code>groupOfVehiclesTrustScore</code> <!-- Endpoint path -->
    </summary>

#### Parameters
| name      |  type     | data type               | description |
|-----------|-----------|-------------------------|-------------|
| `vehicleGroupID` |  required | string | unique ID of the tool |
| `messageTime` |  required  | string | timestamp of the message in ISO-8601 (UTC) |

#### Responses

| http code     | content-type                      | response      |
|---------------|-----------------------------------|---------------|
| `200`         | `application/json`                | `{"code":"200","message":"transmitted successfully"}` |
| `400`         | `application/json`                | `{"code":"400","message":"Bad Request"}` |
| `401`         | `application/json`                | `{"code":"401","message":"Unauthorized"}` |
| `404`         | `application/json`                | `{"code":"404","message":"Not Found"}` |

#### Example cURL

```javascript
curl -X POST -H "Content-Type: application/json" --data @post.json http://localhost:8889/
```

#### Example Python3.8+
```python
...
```
</details>

<details>
    <summary>
        <code>GET</code> <!-- for example GET or POST -->
        <code><b>/</b></code> 
        <code>toolTrustScore</code> <!-- Endpoint path -->
    </summary>

#### Parameters
| name      |  type     | data type               | description |
|-----------|-----------|-------------------------|-------------|
| `toolID` |  required | string | unique ID of the tool |
| `messageTime` |  required  | string | timestamp of the message in ISO-8601 (UTC) |

#### Responses

| http code     | content-type                      | response      |
|---------------|-----------------------------------|---------------|
| `200`         | `application/json`                | `{"code":"200","message":"transmitted successfully"}` |
| `400`         | `application/json`                | `{"code":"400","message":"Bad Request"}` |
| `401`         | `application/json`                | `{"code":"401","message":"Unauthorized"}` |
| `404`         | `application/json`                | `{"code":"404","message":"Not Found"}` |

#### Example cURL

```javascript
curl -X POST -H "Content-Type: application/json" --data @post.json http://localhost:8889/
```

#### Example Python3.8+
```python
...
```
</details>


<details>
    <summary>
        <code>GET</code> <!-- for example GET or POST -->
        <code><b>/</b></code> 
        <code>vehicleSecurityState</code> <!-- Endpoint path -->
    </summary>

#### Parameters
| name      |  type     | data type               | description |
|-----------|-----------|-------------------------|-------------|
| `vehicleID` |  required | string | unique ID of the tool |
| `messageTime` |  required  | string | timestamp of the message in ISO-8601 (UTC) |

#### Responses

| http code     | content-type                      | response      |
|---------------|-----------------------------------|---------------|
| `200`         | `application/json`                | `{"code":"200","message":"transmitted successfully"}` |
| `400`         | `application/json`                | `{"code":"400","message":"Bad Request"}` |
| `401`         | `application/json`                | `{"code":"401","message":"Unauthorized"}` |
| `404`         | `application/json`                | `{"code":"404","message":"Not Found"}` |

#### Example cURL

```javascript
curl -X POST -H "Content-Type: application/json" --data @post.json http://localhost:8889/
```

#### Example Python3.8+
```python
...
```
</details>

<details>
    <summary>
        <code>GET</code> <!-- for example GET or POST -->
        <code><b>/</b></code> 
        <code>networkSecurityState</code> <!-- Endpoint path -->
    </summary>

#### Parameters
| name      |  type     | data type               | description |
|-----------|-----------|-------------------------|-------------|
| `networkID` |  required | string | unique ID of the tool |
| `messageTime` |  required  | string | timestamp of the message in ISO-8601 (UTC) |

#### Responses

| http code     | content-type                      | response      |
|---------------|-----------------------------------|---------------|
| `200`         | `application/json`                | `{"code":"200","message":"transmitted successfully"}` |
| `400`         | `application/json`                | `{"code":"400","message":"Bad Request"}` |
| `401`         | `application/json`                | `{"code":"401","message":"Unauthorized"}` |
| `404`         | `application/json`                | `{"code":"404","message":"Not Found"}` |

#### Example cURL

```javascript
curl -X POST -H "Content-Type: application/json" --data @post.json http://localhost:8889/
```

#### Example Python3.8+
```python
...
```
</details>

## VSOC analysis capabilities (deprecated)


Different services that allow analysis of data.

### Binary analysis (deprecated)


<details>
    <summary>
        <code>POST</code> <!-- for example GET or POST -->
        <code><b>/</b></code> 
        <code>binaryAnalysis</code> <!-- Endpoint path -->
    </summary>

#### Parameters
| name      |  type     | data type               | description |
|-----------|-----------|-------------------------|-------------|
| `toolID` |  optional | string | unique ID of the tool |
| `messageTime` |  required  | string | timestamp of the message in ISO-8601 (UTC) |
| `binary` |  required | object | the file which need to be analysed |

#### Responses

| http code     | content-type                      | response      |
|---------------|-----------------------------------|---------------|
| `200`         | `application/json`                | `{"code":"200","message":"transmitted successfully"}` |
| `400`         | `application/json`                | `{"code":"400","message":"Bad Request"}` |
| `401`         | `application/json`                | `{"code":"401","message":"Unauthorized"}` |
| `404`         | `application/json`                | `{"code":"404","message":"Not Found"}` |

#### Example cURL

```javascript
curl -X POST -H "Content-Type: application/json" --data @post.json http://localhost:8889/
```

#### Example Python3.8+
```python
...
```
</details>