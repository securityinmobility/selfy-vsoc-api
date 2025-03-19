from flask import Flask, jsonify, request, Response, abort, make_response
import http.client
import json
from jsonschema import validate, ValidationError, RefResolver, Draft7Validator
import requests
from datetime import datetime
import uuid
import json
import http.client

import trust_score

# from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry import trace  # , metrics

# instrumentor = FlaskInstrumentor()
tracer = trace.get_tracer("vsoc-api.tracer")

app = Flask(__name__)  # Dictionary to store the data

# instrumentor.intrument_app(app)

response = {
    "statusCode": 501,  # Not Implemented
    "statusMessage": http.client.responses[501]
}
data = {
    "statusCode": "",
    "statusMessage": "",
    "securityStatus": ""
}

# GLOBALS
sota_endpoint = "http://uptane-bridge.sota.selfy.ota.ce/vsoctrigger"
ras_endpoint = "http://127.0.0.1:4201"
ais_endpoint = "http://127.0.0.1:4202"
ab_endpoint = "http://127.0.0.1:4203"
sot_endpoint = "http://127.0.0.1:4204"
ivt_endpoint = "http://172.17.0.1:4205"

# Default
@app.route('/')
def index():
    return jsonify({'SELFY VSOC': 'by THI', 'version': 'v0.0.9'})


def sota_request_update(vin, action):
    """
    Requests and update to the SOTA infrastructure.

    :param vin: vehicle identification number (string)
    :param action: 1 update, 0 nothing, 2 tbd (integer)
    """
    req_obj = {"toolId": 8, "timeStamp": datetime.now().replace(microsecond=0).isoformat()+"Z", "VIN": str(vin), "action": action}

    response = requests.get(sota_endpoint, json=req_obj)
    return Response(
        response.text,
        status=response.status_code,
        content_type=response.headers['content-type'],
    )


@app.route('/sota/updateInfo', methods=['POST'])
def sota_receive_info():
    """
    Getting information from the SOTA infrastructure regarding the status of an update.
    """

    schema_path = './jsonschema/sota/updateInfo.json'
    opentelemetrie_prefix = 'sota.updateInfo'

    if check_for_json(request):
        return check_for_json(request)

    request_json = request.get_json()

    status = request_json["message"]["status"] 
    vin = request_json["message"]["vin"]
    target = "08"
    
    # Use-Case 34/35/36
    if status == 0:
        # post RAS, AIS, AB 

        # target: vin
        ras_attestation_request(target, str(vin))

        # process: ais_1, asset_id: endpoint.example.com
        ais_start_process("ais_1", "endpoint.example.com")

        # ab_id:28, priority:1, vin, scan_type: fast scan
        ab_trigger_audit(28, 1, str(vin), 1)
    else:
        # update TS
        trust_score.set_ts()

    return response_to_json(request_json, schema_path, opentelemetrie_prefix)


def ras_attestation_request(target, vin):
    """
    Send a request to the RAS to perform an attestation.

    :param target: ID of the target tool
    """

    nonce = uuid.uuid4().hex
    req_obj = {"target_tool": target, "timeStamp": datetime.now().replace(microsecond=0).isoformat()+"Z", "VIN": str(vin), "verifier": "ID18", "VSOC": "ID08", "nonce": nonce}

    try:
        response = requests.get(ras_endpoint, json=req_obj)
        return Response(
                response.text,
                status=response.status_code,
                content_type=response.headers['content-type'],
                )
    except:
        print("[SELFY VSOC] Could not connect to ", ras_endpoint)
        return ""



@app.route('/ras/attestationResult', methods=['POST'])
def ras_attestation_result():
    schema_path = './jsonschema/ras/attestationResult.json'
    opentelemetrie_prefix = 'ras.attestationResult'

    if check_for_json(request):
        return check_for_json(request)

    request_json = request.get_json()

    return response_to_json(request_json, schema_path, opentelemetrie_prefix)


# AIS start process
def ais_start_process(nproc, asset_id):
    """
    Start the AIS process with a specific process name.

    :param nproc: name of the process to start.
    :param asset_id: url of the actuator endpoint.
    """

    req_obj = {
            "id": "04be1c1b-0d81-400b-9085-015a7746e401",
            "action": "start",
            "target": {
                "process": {
                    "name": str(nproc)
                    }
                },
            "actuator": {
                "endpoint": {
                    "asset_id": str(asset_id)
                    }
                }
            }

    try:
        response = requests.get(ais_endpoint, json=req_obj)
        return Response(
                response.text,
                status=response.status_code,
                content_type=response.headers['content-type'],
                )
    except:
        print("[SELFY VSOC] Could not connect to ", ais_endpoint)
        return ""


# AIS stop process
# curl -X POST "http://127.0.0.1:4202/api/stop_process/" -H "Content-Type: application/json" -d
def ais_stop_process(nproc, asset_id):
    """
    Stop the AIS process with a specific process name.

    :param nproc: name of the process to start.
    :param asset_id: url of the actuator endpoint.
    """

    req_obj = {
            "id": "04be1c1b-0d81-400b-9085-015a7746e401",
            "action": "stop",
            "target": {
                "process": {
                    "name": str(nproc)
                    }
                },
            "actuator": {
                "endpoint": {
                    "asset_id": str(asset_id)
                    }
                }
            }
    try:
        response = requests.get(ais_endpoint, json=req_obj)
        return Response(
            response.text,
            status=response.status_code,
            content_type=response.headers['content-type'],
            )
    except:
        print("[SELFY VSOC] Could not connect to ", ais_endpoint)
        return ""

# AIS train
# curl -X POST "http://127.0.0.1:4202/api/train_process/" -H "Content-Type: application/json" -d
def ais_train_process(nproc, asset_id):
    """
    Stop the AIS process with a specific process name.

    :param nproc: name of the process to start.
    :param asset_id: url of the actuator endpoint.
    """

    req_obj = {
            "id": "04be1c1b-0d81-400b-9085-015a7746e401",
            "action": "train",
            "target": {
                "process": {
                    "name": str(nproc)
                    }
                },
            "actuator": {
                "endpoint": {
                    "asset_id": str(asset_id)
                    }
                }
            }
    try:
        response = requests.get(ais_endpoint, json=req_obj)
        return Response(
            response.text,
            status=response.status_code,
            content_type=response.headers['content-type'],
            )
    except:
        print("[SELFY VSOC] Could not connect to ", ais_endpoint)
        return ""

# AIS finetune
# curl -X POST "http://127.0.0.1:4202/api/finetune_process/" -H "Content-Type: application/json" -d
def ais_finetune(nproc, asset_id, args):
    """
    Stop the AIS process with a specific process name.

    :param nproc: name of the process to start.
    :param asset_id: url of the actuator endpoint.
    :param args: argument to set finetuning options.
    """

    if args == "":
        args = {    
                "max_detectors_from": "1024",
                "max_detectors_to": "2048",
                "max_attempts_from": "10",
                "max_attempts_to": "10",
                "threshold_1_from": "0.01",
                "threshold_1_to": "0.10",
                "threshold_2_from": "1",
                "threshold_2_to": "9"
                }

    req_obj = {
            "id": "04be1c1b-0d81-400b-9085-015a7746e401",
            "action": "finetune",
            "target": {
                "process": {
                    "name": str(nproc)
                    }
                },
            "actuator": {
                "endpoint": {
                    "asset_id": str(asset_id)
                    }
                },
            "args": str(args)
            }
    try:
        response = requests.get(ais_endpoint, json=req_obj)
        return Response(
            response.text,
            status=response.status_code,
            content_type=response.headers['content-type'],
            )
    except:
        print("[SELFY VSOC] Could not connect to ", ais_endpoint)
        return ""

# AIS change config
# curl -X POST "http://127.0.0.1:4202/api/set_process/" -H "Content-Type: application/json" -d
def ais_change_config(nproc, ais_id, config):
    """
    Change the configuration of an AIS tool.

    :param ais_id: ID of the AIS to change.
    :param config: Configuration parameters for the AIS.
    """

    if config == "":
        args =  {
                "max_detectors": "2048",
                "max_attempts": "10",
                "threshold_1": "0.01",
                "threshold_2": "5" 
                }
    else:
        args = config

    req_obj = {
            "id": "04be1c1b-0d81-400b-9085-015a7746e401",
            "action": "set",
            "target": {
                "process": {
                    "name": str(nproc)
                    }
                },
            "actuator": {
                "endpoint": {
                    "asset_id": str(ais_id)
                    }
                },
            "args": str(args)  
            }
    try:
        response = requests.get(ais_endpoint, json=req_obj)
        return Response(
            response.text,
            status=response.status_code,
            content_type=response.headers['content-type'],
            )
    except:
        print("[SELFY VSOC] Could not connect to ", ais_endpoint)
        return ""


@app.route('/ais/deviationUnknown', methods=['POST'])
def ais_deviation_unknown():
    """
    Getting information from the AIS for an unknown deviation.
    """
    schema_path: str = 'jsonschema/ais/deviationUnknown.json'
    opentelemetrie_prefix = 'ais.deviationUnknown'

    if check_for_json(request):
        return check_for_json(request)

    request_json = request.get_json()

    return response_to_json(request_json, schema_path, opentelemetrie_prefix)


@app.route('/ais/deviationKnown', methods=['POST'])
def ais_deviation_known():
    """
        Getting information from the AIS for an known deviation.
        """
    schema_path: str = 'jsonschema/ais/deviationKnown.json'
    opentelemetrie_prefix = 'ais.deviationKnown'

    if check_for_json(request):
        return check_for_json(request)

    request_json = request.get_json()
    vin = request_json["indicator"]["source_vehicle"]
    target = "00"
    print(vin)

    # Use-Case 34/35/36
    # target: vin
    ras_attestation_request(target, str(vin))

    # process: ais_1, asset_id: endpoint.example.com
    ais_start_process("ais_1", "endpoint.example.com")

    # ab_id:28, priority:1, vin, scan_type: fast scan
    ab_trigger_audit(28, 1, str(vin), 1)

    # update trust-score
    trust_score.set_ts()

    return response_to_json(request_json, schema_path, opentelemetrie_prefix)


def ab_trigger_audit(ab_id, priority, vin, scan_type):
    """
    Trigger an audit to audit a vehicle with a specific VIN.

    :param ab_id: ID of the audit box (integer)
    :param priority: priorty value of the can (integer)
    :param vin: vehicle identification number (string)
    :param scan_type: type of scan; 1 is fast scan, 2 is deep scan (integer)
    """
    req_obj = {"AB_id": ab_id, "timeStamp": datetime.now().replace(microsecond=0).isoformat()+"Z", "VIN": str(vin), "scanType": scan_type, "priority": priority}


    try:
        response = requests.get(ab_endpoint, json=req_obj)
        return Response(
            response.text,
            status=response.status_code,
            content_type=response.headers['content-type'],
            )
    except:
        print("[SELFY VSOC] Could not connect to ", ab_endpoint)
        return ""


@app.route('/ab/vulnReport', methods=['POST'])
def ab_vulnReport():
    schema_path = './jsonschema/ab/vulnReport.json'
    opentelemetrie_prefix = 'ab.vulnReport'

    if check_for_json(request):
        return check_for_json(request)

    request_json = request.get_json()

    return response_to_json(request_json, schema_path, opentelemetrie_prefix)

@app.route('/ab/vulnReportKO', methods=['POST'])
def ab_vulnReportKO():
    schema_path = './jsonschema/ab/vulnReportKO.json'
    opentelemetrie_prefix = 'ab.vulnReportKO'

    if check_for_json(request):
        return check_for_json(request)

    request_json = request.get_json()

    return response_to_json(request_json, schema_path, opentelemetrie_prefix)

@app.route('/ab/jamAlarm', methods=['POST'])
def ab_jamAlarm():
    schema_path = './jsonschema/ab/jamAlarm.json'
    opentelemetrie_prefix = 'ab.jamAlarm'

    if check_for_json(request):
        return check_for_json(request)

    request_json = request.get_json()

    return response_to_json(request_json, schema_path, opentelemetrie_prefix)

@app.route('/ab/heartbeat', methods=['POST'])
def ab_heartbeat():
    schema_path = './jsonschema/ab/heartbeat.json'
    opentelemetrie_prefix = 'ab.heartbeat'
    if check_for_json(request):
        return check_for_json(request)

    request_json = request.get_json()

    return response_to_json(request_json, schema_path, opentelemetrie_prefix)

@app.route('/ab/configStatus', methods=['POST'])
def ab_configStatus():
    schema_path = './jsonschema/ab/configStatus.json'
    opentelemetrie_prefix = 'ab.configStatus'
    if check_for_json(request):
        return check_for_json(request)

    request_json = request.get_json()

    return response_to_json(request_json, schema_path, opentelemetrie_prefix)


def ab_set_config(ab_id, config_status, new_ab_id, enable, selective_mode, reset, stoprq, mintime, jamfreq, hbfreq, audittechs):
    """
    Set the configuration of an audit box.

    :param ab_id: ID of the Audit Box
    :param config_status: (0 or 1) 1 means the VSOC wants to know current configuration status
    :param new_ab_id: if this field is filled, then the VSOC assigns a new AB_id to the Audit Box
    :param enable: (0 or 1) 1 is Enable, 0 is Disable
    :param selective_mode: (0 or 1): 1 means that Audit Box only audits (exclusively) the IDs selected by the VSOC. 0 means that the Audit Box will audit with priority the IDs selected by the VSOC but also will audit the rest of IDs (without priority)
    :param reset: 1 forces a reset on the Audit Box. 0 makes nothing
    :param mintime: parameter with the minimum time it has to happen to re-scan a vehicle (By default 10 minutes)
    :param stoprq: 1 or 0 . If the value is 1 the VSOC can reset all previous scan triggers
    :param jamfreq: is the parameter defined for this function The jamming signal is sent immediately after a jamming detection and it is sent every JAMSIGFREQ minutes to the VSOC (by default every 5 minutes) until the jamming is over. Minimum 0 and Maximum 255 minutes. (unsigned char) 
    :param hbfreq: by default 1 minute. (Minimum is 1 and Maximum 255 minutes) (unsigned char) 
    :param audittechs: this field says to the Audit Box which technologies have to be audited
    """
    req_obj = {"AB_id": ab_id, "timeStamp": datetime.now().replace(microsecond=0).isoformat()+"Z", "config_status": config_status, "new_ab_id": new_ab_id, "enable": enable, "selective_mode": selective_mode, "reset": reset, "STOPALLREQUESTS": stoprq, "MINTIMETORESCAN": mintime, "JAMSIGFREQ": jamfreq, "HEARTBEATFREQ": hbfreq, "AUDITTECHS": audittechs,}


    try:
        response = requests.get(ab_endpoint, json=req_obj)
        return Response(
            response.text,
            status=response.status_code,
            content_type=response.headers['content-type'],
            )
    except:
        print("[SELFY VSOC] Could not connect to ", ab_endpoint)
        return ""


@app.route('/vsoc/getTrustScore', methods=['GET'])
def vsoc_get_trustscore():
    """
    Getting the trust-score for a specific entity and distributing it.
    """
    # file ./trust-score.py

    return ""


@app.route('/rsu/misbehaviour', methods=['POST'])
def rsu_misbehaviour():
    schema_path = './jsonschema/rsu/misbehaviour.json'
    opentelemetrie_prefix = 'rsu.misbehaviour'

    if check_for_json(request):
        return check_for_json(request)

    request_json = request.get_json()

    # use-case 43 and 30
    try:
        response = requests.post(url=ivt_endpoint, data=request_json)
        print("[SELFY VSOC] Response of " + ivt_endpoint + " is ", response)
    except:
        print("[SELFY VSOC] Could not connect to ", ivt_endpoint)

    return response_to_json(request_json, schema_path, opentelemetrie_prefix)

# SOT vehicleLog
@app.route('/sot/vehicleLog', methods=['POST'])
def sot_vehiclelog():
    schema_path = './jsonschema/sot/vehicleLog.json'
    opentelemetrie_prefix = 'sot.vehicleLog'
    if check_for_json(request):
        return check_for_json(request)

    request_json = request.get_json()

    # use-case 25
    try:
        response = requests.post(url=ivt_endpoint, json=request_json)
        print("[SELFY VSOC] Response of " + ivt_endpoint + " is ", response)
    except:
        print("[SELFY VSOC] Could not connect to ", ivt_endpoint)

    return response_to_json(request_json, schema_path, opentelemetrie_prefix)

# SOT vehicleSafetyStatus
@app.route('/sot/vehicleSafetyStatus', methods=['POST'])
def sot_vehicleSafetyStatus():
    schema_path = './jsonschema/sot/vehicleSafetyStatus.json'
    opentelemetrie_prefix = 'sot.vehicleSafetyStatus'

    if check_for_json(request):
        return check_for_json(request)

    request_json = request.get_json()

    return response_to_json(request_json, schema_path, opentelemetrie_prefix)    

#
#
#
# Deprecated endpoints below
#
#
#

# SOT vehicleInfoArray
@app.route('/sot/vehicleInfoArray', methods=['POST'])
def sot_vehicleinfoarray():
    schema_path = './jsonschema/sot/vehicleInfoArray.json'
    opentelemetrie_prefix = 'sot.vehicleInfoArray'
    if check_for_json(request):
        return check_for_json(request)

    request_json = request.get_json()

    # use-case 25
    try:
        response = requests.post(url=ivt_endpoint, json=request_json)
        print("[SELFY VSOC] Response of " + ivt_endpoint + " is ", response)
    except:
        print("[SELFY VSOC] Could not connect to ", ivt_endpoint)

    return response_to_json(request_json, schema_path, opentelemetrie_prefix)
    

# POST endpoint: RSU/statusMessage
@app.route('/RSU/statusMessage', methods=['POST'])
def set_status_message():
    with tracer.start_as_current_span("rsu.statusMessage") as rsu_statusMessage_span:
        message = request.get_json().get('message')
        data['statusMessage'] = message
        rsu_statusMessage_span.set_attribute("rsu.statusMessage", data['statusMessage'])
        return jsonify({'message': 'Status message updated successfully', 'statusMessage': message})


# POST endpoint: RSU/securityStatus
@app.route('/RSU/securityStatus', methods=['POST'])
def set_security_status():
    status = request.get_json().get('status')
    data['securityStatus'] = status
    return jsonify({'message': 'Security status updated successfully', 'securityStatus': status})


# GET endpoint: RSU/triggerSafeOperationalMode
@app.route('/RSU/triggerSafeOperationalMode', methods=['GET'])
def trigger_safe_operational_mode():
    with tracer.start_as_current_span("rsu.triggerSafeOperationalMode") as rsuTrigSaOpModeSpan:
        # message = request.get_json().get('message')
        data['triggerSafeOperationalMode'] = "1"
        rsuTrigSaOpModeSpan.set_attribute("rsu.triggerSafeOperationalMode", data['triggerSafeOperationalMode'])
        return jsonify({'message': 'Safe operational mode triggered'})
    # Add your logic here to trigger safe operational mode


# GET endpoint: RSU/triggerMinimumRiskManeuver
@app.route('/RSU/triggerMinimumRiskManeuver', methods=['GET'])
def trigger_minimum_risk_maneuver():
    # Add your logic here to trigger minimum risk maneuver
    return jsonify({'message': 'Minimum risk maneuver triggered'})


# GET endpoint: TDMS/healingProcedures
@app.route('/TDMS/healingProcedures', methods=['GET'])
def get_healing_procedures():
    # Add your logic here to retrieve healing procedures from TDMS
    healing_procedures = ['Procedure 1', 'Procedure 2', 'Procedure 3']
    return jsonify({'healingProcedures': healing_procedures})


# GET endpoint: VSOC/securityScenario
@app.route('/VSOC/securityScenario', methods=['GET'])
def get_security_scenario():
    # Add your logic here to retrieve security scenario from VSOC
    security_scenario = 'Scenario 1'
    return jsonify({'securityScenario': security_scenario})


# GET endpoint: VSOC/healingProcedures
@app.route('/VSOC/healingProcedures', methods=['GET'])
def get_vsoc_healing_procedures():
    # Add your logic here to retrieve healing procedures from VSOC
    vsoc_healing_procedures = ['Procedure 1', 'Procedure 2']
    return jsonify({'healingProcedures': vsoc_healing_procedures})


# GET endpoint: VSOC/ontology
@app.route('/VSOC/ontology', methods=['GET'])
def get_ontology():
    # Add your logic here to retrieve ontology from VSOC
    ontology = ['Term 1', 'Term 2', 'Term 3']
    return jsonify({'ontology': ontology})


# GET endpoint: VSOC/patchForComponent
@app.route('/VSOC/patchForComponent', methods=['GET'])
def get_patch_for_component():
    # Add your logic here to retrieve patch for component from VSOC
    patch = 'Component patch'
    return jsonify({'patchForComponent': patch})

# Add more endpoints as needed

#
#
#
# Utilities below
#
#
#

def response_to_json(request_json, schema_path, opentelemetrie_prefix):
    is_valid, error_message = validate_json_with_schema(schema_path, request_json)

    if is_valid:
        with tracer.start_as_current_span(opentelemetrie_prefix) as current_span:
            current_span.set_attribute(opentelemetrie_prefix + '.' + 'http.body',  str(request_json))
            for required_item, value in iterate_required_items(schema_path, request_json):
                current_span.set_attribute(opentelemetrie_prefix + '.' + required_item.lower(), str(value))

        response['statusCode'] = 200
        response['statusMessage'] = http.client.responses[response['statusCode']]
        response['data'] = request_json
        return jsonify(response), response['statusCode']
    else:
        response['statusCode'] = 400
        response['statusMessage'] = http.client.responses[response['statusCode']]
        response['data'] = error_message
        return jsonify(response), response['statusCode']


def check_for_json(request):
    if request.content_type != 'application/json':
        response['statusCode'] = 415
        response['statusMessage'] = http.client.responses[response['statusCode']]
        return jsonify(response), response['statusCode']

    if not request.data:
        response['statusCode'] = 400
        response['statusMessage'] = http.client.responses[response['statusCode']]
        response['data'] = 'no data sent in the POST request'
        return jsonify(response), response['statusCode']

    return None


# Function to validate the request with the json schema
def validate_json_with_schema(schema_path, json_dict):
    with open(schema_path, 'r') as f:
        schema = json.load(f)
#        resolver = RefResolver(base_uri='file://' + os.path.dirname(os.path.realpath(__file__)) + '/jsonschema', referrer=schema)  # use with jsonschema refs
        try:
#            validator = Draft7Validator(schema, resolver=resolver) # use with jsonschema refs
#            validator.validate(json_dict)                          #
            validate(instance=json_dict, schema=schema)   # use without jsonschema refs
            return True, None
        except ValidationError as e:
            return False, e.message


# Function to iterate through required items
def iterate_required_items(schema_path, validated_json):
    with open(schema_path, 'r') as f:
        schema = json.load(f)
        required_items = schema.get("required", [])
        for required_item in required_items:
            yield required_item, validated_json.get(required_item)


# Add more methods here as needed

if __name__ == '__main__':
    app.run()
