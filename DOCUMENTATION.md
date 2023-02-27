*VSOC API v0.1*

# VSOC API

This is the documentation of the VSOC API.

# RSU

The roadside unit (RSU) collects data from V2X systems, collects them, and performs analysis. The component sends and receives data.

### RSU status messages

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

### Safe operational modes (SOM)

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


## Virtual vehicle

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



### Tool information

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


## Trust data management system (TDMS)

The TDMS is a set of tools holding all relevant assets for data management.

### Healing procedures 

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

## VSOC data subscription

Different services one and subscribe to.

### Knowledge 

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

### Security controls 

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

### Security information


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

## VSOC analysis capabilities

Different services that allow analysis of data.

### Binary analysis

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
