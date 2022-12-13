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
| `parameter-name` |  required / optional | type  | description |

#### Responses

| http code     | content-type                      | response      |
|---------------|-----------------------------------|---------------|
| `201`         | `text/plain;charset=UTF-8`        | `Configuration created successfully` |
| `400`         | `application/json`                | `{"code":"400","message":"Bad Request"}` |
| `405`         | `text/html;charset=utf-8`         | None              |

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
| `parameter-name` |  required / optional | type  | description |

#### Responses

| http code     | content-type                      | response      |
|---------------|-----------------------------------|---------------|
| `201`         | `text/plain;charset=UTF-8`        | `Configuration created successfully` |
| `400`         | `application/json`                | `{"code":"400","message":"Bad Request"}` |
| `405`         | `text/html;charset=utf-8`         | None              |

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
| `parameter-name` |  required / optional | type  | description |

#### Responses

| http code     | content-type                      | response      |
|---------------|-----------------------------------|---------------|
| `201`         | `text/plain;charset=UTF-8`        | `Configuration created successfully` |
| `400`         | `application/json`                | `{"code":"400","message":"Bad Request"}` |
| `405`         | `text/html;charset=utf-8`         | None              |

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
| `parameter-name` |  required / optional | type  | description |

#### Responses

| http code     | content-type                      | response      |
|---------------|-----------------------------------|---------------|
| `201`         | `text/plain;charset=UTF-8`        | `Configuration created successfully` |
| `400`         | `application/json`                | `{"code":"400","message":"Bad Request"}` |
| `405`         | `text/html;charset=utf-8`         | None              |

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
| `parameter-name` |  required / optional | type  | description |

#### Responses

| http code     | content-type                      | response      |
|---------------|-----------------------------------|---------------|
| `201`         | `text/plain;charset=UTF-8`        | `Configuration created successfully` |
| `400`         | `application/json`                | `{"code":"400","message":"Bad Request"}` |
| `405`         | `text/html;charset=utf-8`         | None              |

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
| `parameter-name` |  required / optional | type  | description |

#### Responses

| http code     | content-type                      | response      |
|---------------|-----------------------------------|---------------|
| `201`         | `text/plain;charset=UTF-8`        | `Configuration created successfully` |
| `400`         | `application/json`                | `{"code":"400","message":"Bad Request"}` |
| `405`         | `text/html;charset=utf-8`         | None              |

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
| `parameter-name` |  required / optional | type  | description |

#### Responses

| http code     | content-type                      | response      |
|---------------|-----------------------------------|---------------|
| `201`         | `text/plain;charset=UTF-8`        | `Configuration created successfully` |
| `400`         | `application/json`                | `{"code":"400","message":"Bad Request"}` |
| `405`         | `text/html;charset=utf-8`         | None              |

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
| `parameter-name` |  required / optional | type  | description |

#### Responses

| http code     | content-type                      | response      |
|---------------|-----------------------------------|---------------|
| `201`         | `text/plain;charset=UTF-8`        | `Configuration created successfully` |
| `400`         | `application/json`                | `{"code":"400","message":"Bad Request"}` |
| `405`         | `text/html;charset=utf-8`         | None              |

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
| `parameter-name` |  required / optional | type  | description |

#### Responses

| http code     | content-type                      | response      |
|---------------|-----------------------------------|---------------|
| `201`         | `text/plain;charset=UTF-8`        | `Configuration created successfully` |
| `400`         | `application/json`                | `{"code":"400","message":"Bad Request"}` |
| `405`         | `text/html;charset=utf-8`         | None              |

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
| `parameter-name` |  required / optional | type  | description |

#### Responses

| http code     | content-type                      | response      |
|---------------|-----------------------------------|---------------|
| `201`         | `text/plain;charset=UTF-8`        | `Configuration created successfully` |
| `400`         | `application/json`                | `{"code":"400","message":"Bad Request"}` |
| `405`         | `text/html;charset=utf-8`         | None              |

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
| `parameter-name` |  required / optional | type  | description |

#### Responses

| http code     | content-type                      | response      |
|---------------|-----------------------------------|---------------|
| `201`         | `text/plain;charset=UTF-8`        | `Configuration created successfully` |
| `400`         | `application/json`                | `{"code":"400","message":"Bad Request"}` |
| `405`         | `text/html;charset=utf-8`         | None              |

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
| `parameter-name` |  required / optional | type  | description |

#### Responses

| http code     | content-type                      | response      |
|---------------|-----------------------------------|---------------|
| `201`         | `text/plain;charset=UTF-8`        | `Configuration created successfully` |
| `400`         | `application/json`                | `{"code":"400","message":"Bad Request"}` |
| `405`         | `text/html;charset=utf-8`         | None              |

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
| `parameter-name` |  required / optional | type  | description |

#### Responses

| http code     | content-type                      | response      |
|---------------|-----------------------------------|---------------|
| `201`         | `text/plain;charset=UTF-8`        | `Configuration created successfully` |
| `400`         | `application/json`                | `{"code":"400","message":"Bad Request"}` |
| `405`         | `text/html;charset=utf-8`         | None              |

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
| `parameter-name` |  required / optional | type  | description |

#### Responses

| http code     | content-type                      | response      |
|---------------|-----------------------------------|---------------|
| `201`         | `text/plain;charset=UTF-8`        | `Configuration created successfully` |
| `400`         | `application/json`                | `{"code":"400","message":"Bad Request"}` |
| `405`         | `text/html;charset=utf-8`         | None              |

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
| `componentName` |  required | int | unique identifier of the the component |

#### Responses

| http code     | content-type                      | response      |
|---------------|-----------------------------------|---------------|
| `201`         | `text/plain;charset=UTF-8`        | `Configuration created successfully` |
| `400`         | `application/json`                | `{"code":"400","message":"Bad Request"}` |
| `405`         | `text/html;charset=utf-8`         | None              |

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
| `parameter-name` |  required / optional | type  | description |

#### Responses

| http code     | content-type                      | response      |
|---------------|-----------------------------------|---------------|
| `201`         | `text/plain;charset=UTF-8`        | `Configuration created successfully` |
| `400`         | `application/json`                | `{"code":"400","message":"Bad Request"}` |
| `405`         | `text/html;charset=utf-8`         | None              |

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
| `parameter-name` |  required / optional | type  | description |

#### Responses

| http code     | content-type                      | response      |
|---------------|-----------------------------------|---------------|
| `201`         | `text/plain;charset=UTF-8`        | `Configuration created successfully` |
| `400`         | `application/json`                | `{"code":"400","message":"Bad Request"}` |
| `405`         | `text/html;charset=utf-8`         | None              |

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
| `parameter-name` |  required / optional | type  | description |

#### Responses

| http code     | content-type                      | response      |
|---------------|-----------------------------------|---------------|
| `201`         | `text/plain;charset=UTF-8`        | `Configuration created successfully` |
| `400`         | `application/json`                | `{"code":"400","message":"Bad Request"}` |
| `405`         | `text/html;charset=utf-8`         | None              |

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
| `parameter-name` |  required / optional | type  | description |

#### Responses

| http code     | content-type                      | response      |
|---------------|-----------------------------------|---------------|
| `201`         | `text/plain;charset=UTF-8`        | `Configuration created successfully` |
| `400`         | `application/json`                | `{"code":"400","message":"Bad Request"}` |
| `405`         | `text/html;charset=utf-8`         | None              |

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
| `parameter-name` |  required / optional | type  | description |

#### Responses

| http code     | content-type                      | response      |
|---------------|-----------------------------------|---------------|
| `201`         | `text/plain;charset=UTF-8`        | `Configuration created successfully` |
| `400`         | `application/json`                | `{"code":"400","message":"Bad Request"}` |
| `405`         | `text/html;charset=utf-8`         | None              |

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
| `parameter-name` |  required / optional | type  | description |

#### Responses

| http code     | content-type                      | response      |
|---------------|-----------------------------------|---------------|
| `201`         | `text/plain;charset=UTF-8`        | `Configuration created successfully` |
| `400`         | `application/json`                | `{"code":"400","message":"Bad Request"}` |
| `405`         | `text/html;charset=utf-8`         | None              |

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
| `vehicleIdentifier` |  required | string  | unique vehicle identifier (VIN) |

#### Responses

| http code     | content-type                      | response      |
|---------------|-----------------------------------|---------------|
| `201`         | `text/plain;charset=UTF-8`        | `Configuration created successfully` |
| `400`         | `application/json`                | `{"code":"400","message":"Bad Request"}` |
| `405`         | `text/html;charset=utf-8`         | None              |

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
| `networkIdentifier` |  required | string  | unique network identifier |

#### Responses

| http code     | content-type                      | response      |
|---------------|-----------------------------------|---------------|
| `201`         | `text/plain;charset=UTF-8`        | `Configuration created successfully` |
| `400`         | `application/json`                | `{"code":"400","message":"Bad Request"}` |
| `405`         | `text/html;charset=utf-8`         | None              |

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
| `binary` |  required | object | the file which need to be analysed |

#### Responses

| http code     | content-type                      | response      |
|---------------|-----------------------------------|---------------|
| `201`         | `text/plain;charset=UTF-8`        | `Configuration created successfully` |
| `400`         | `application/json`                | `{"code":"400","message":"Bad Request"}` |
| `405`         | `text/html;charset=utf-8`         | None              |

#### Example cURL

```javascript
curl -X POST -H "Content-Type: application/json" --data @post.json http://localhost:8889/
```

#### Example Python3.8+
```python
...
```
</details>
