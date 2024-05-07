from typing import Any

from flask import Flask, jsonify, request, Response, abort, make_response
from http import HTTPStatus
from werkzeug.exceptions import BadRequest, UnsupportedMediaType
import requests
import time
import uuid

#from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry import trace#, metrics

#instrumentor = FlaskInstrumentor()
tracer = trace.get_tracer("vsoc-api.tracer")

app = Flask(__name__) # Dictionary to store the data

#instrumentor.intrument_app(app)

data = {
    "statusMessage": "",
    "securityStatus": ""
}

# GLOBALS
sota_endpoint = "http://uptane-bridge.sota.selfy.ota.ce/vsoctrigger"
ras_endpoint = "http://127.0.0.1:4201"
ais_endpoint = "http://127.0.0.1:4202"
ab_endpoint = "http://127.0.0.1:4203"

# Default
@app.route('/')
def index():
    return jsonify({'SELFY VSOC': 'by THI',
                       'version': 'v0.2'})

def sota_request_update(vin, action):
    """
    Requests and update to the SOTA infrastructure.

    :param vin: vehicle identification number
    :param device_id: ID of the device to send the request to
    :param action: 1 update, 0 nothing, 2 tbd
    """
    # {"toolId": 8, "timeStamp": "2023-11-21T06:14:00Z", "VIN": "2a910ebe-b39a-4813-9992-373738ab4599", "action": 1}
    req_obj = {"toolId": 8, "timeStamp": str(time.time()), "VIN": str(vin), "action": action}

    response = requests.get(sota_endpoint, json=req_obj)
    return Response(
            response.text,
            status = response.status_code,
            content_type = response.headers['content-type'],
            )

@app.route('/sota/updateInfo', methods=['POST'])
def sota_receive_info():
    """
    Getting information from the SOTA infrastructure regarding the status of an update.
    """
    required_fields = ['action', 'vin', 'deviceID', 'status', 'deviceMetadata']
    data = parse_and_validate_data(required_fields)

    with tracer.start_as_current_span('sota.updateInfo') as sota_updateInfo_span:
        action = data['action']
        sota_updateInfo_span.set_attribute('sota.updateInfo.action', action)

        vin = data['vin']
        sota_updateInfo_span.set_attribute('sota.updateInfo.vin', vin)

        device_id = data['deviceID']
        sota_updateInfo_span.set_attribute('sota.updateInfo.device_id', device_id)

        status = data['status']
        sota_updateInfo_span.set_attribute('sota.updateInfo.status', status)

        device_metadata = data['deviceMetadata']
        sota_updateInfo_span.set_attribute('sota.updateInfo.deviceMetadata', device_metadata)

        # TODO: error handling
        return jsonify({'data': 'Update information updated successfully.', 'receivedInformation': data})

def ras_attestation_request(target):
    """
    Send a request to the RAS to perform an attestation.

    :param target: ID of the target tool
    """

    nonce = uuid.uuid4().hex
    req_obj = {"target_tool": target, "timeStamp": str(time.time()), "verifier": "ID18", "VSOC": "ID08", "nonce": nonce}
    response = requests.get(ras_endpoint, json=req_obj)
    return Response(
            response.text,
            status = response.status_code,
            content_type = response.headers['content-type'],
            )
    
@app.route('/ras/attestationResult', methods=['POST'])
def ras_attestation_result():
    """
    Getting information from the RAS their attestation result.
    """
    data = request.get_json(force=True)

    with tracer.start_as_current_span('ras.attestationResult') as ras_attestation_result_span:
        verifier = data['verifier']
        ras_attestation_result_span.set_attribute('ras.attestationResult.verifier', verifier)

        vsoc = data['VSOC']
        ras_attestation_result_span.set_attribute('ras.attestationResult.vsoc', vsoc)

        target_tool = data['target_tool']
        ras_attestation_result_span.set_attribute('ras.attestationResult.targetTool', target_tool)

        state = data['state']
        ras_attestation_result_span.set_attribute('ras.attestationResult.state', state)

        nonce = data['nonce']
        ras_attestation_result_span.set_attribute('ras.attestationResult.nonce', nonce)

        cts = data['created']
        ras_attestation_result_span.set_attribute('ras.attestationResult.createdTimeStamp', cts)

        # TODO: error handling
        return jsonify({'data': 'Attestation results updated successfully', 'receivedInformation': data})

def ais_change_config(ais_id, config):
    """
    Change the configuration of an AIS tool.

    :param ais_id: ID of the AIS to change.
    :param config: Configuration parameters for the AIS.
    """

    if not config:
        cfg_json = {}
    else:
        for i in range(config):
            cfg_json = {"configuration_param"+str(i): x for x in config}

    req_obj = { 
               "version": "1.0", 
               "action": "set", 
               "target": { 
                          "type": "ais", 
                          "specifiers": { 
                                         "ais_id": str(ais_id)
                                         } 
                          }, 
               "actuator": { 
                            "type": "vsoc", 
                            "specifiers": { 
                                           "vsoc_id": "VSOC" 
                                           } 
                            }, 
               "args": cfg_json
               }
    response = requests.get(ais_endpoint, json=req_obj)
    return Response(
            response.text,
            status = response.status_code,
            content_type = response.headers['content-type'],
            )


@app.route('/ais/deviationUnknown', methods=['POST'])
def ais_deviation_unknown():
    """
    Getting information from the AIS for an unknown deviation.
    """
    data = request.get_json()
    extensions = data[0]['extensions']['extension-definition--d83fce45-ef58-4c6c-a3f4-1fbc32e98c6e']

    with tracer.start_as_current_span('ais.deviationUnknown') as ais_deviation_unknown_span:
        extension_type = extensions['extension_type']
        ais_deviation_unknown_span.set_attribute('ais.deviationUnknown.extensionType', extension_type)

        source_vehicle = extensions['source_vehicle']
        ais_deviation_unknown_span.set_attribute('ais.deviationUnknown.sourceVehicle', source_vehicle)

        source_ais = extensions['source_ais']
        ais_deviation_unknown_span.set_attribute('ais.deviationUnknown.sourceAis', source_ais)

        source_rsu = extensions['source_rsu']
        ais_deviation_unknown_span.set_attribute('ais.deviationUnknown.sourceRsu', source_rsu)

        observable = extensions['observable']
        ais_deviation_unknown_span.set_attribute('ais.deviationUnknown.observableObject', observable)

        # TODO: error handling
        return jsonify({'data': 'Unknown deviation updated successfully', 'receivedInformation': data})

@app.route('/ais/deviationKnown', methods=['POST'])
def ais_deviation_known():
    """
    Getting information from the AIS for a known devication.
    """
    data = request. get_json(force=True)
    extensions = data[0]['extensions']['extension-definition--d83fce45-ef58-4c6c-a3f4-1fbc32e98c6e']

    with tracer.start_as_current_span('ais.deviationKnown') as ais_deviation_known_span:
        extension_type = extensions['extension_type']
        ais_deviation_known_span.set_attribute('ais.deviationKnown.extensionType', extension_type)

        source_vehicle = extensions['source_vehicle']
        ais_deviation_known_span.set_attribute('ais.deviationKnown.sourceVehicle', source_vehicle)

        source_ais = extensions['source_ais']
        ais_deviation_known_span.set_attribute('ais.deviationKnown.sourceAis', source_ais)

        source_rsu = extensions['source_rsu']
        ais_deviation_known_span.set_attribute('ais.deviationKnown.sourceRsu', source_rsu)

        observable = extensions['observable']
        ais_deviation_known_span.set_attribute('ais.deviationKnown.observableObject', observable)

        relationship_id = extensions['id']
        ais_deviation_known_span.set_attribute('ais.deviationKnown.relationshipId', relationship_id)

        source_ref = extensions['source_ref']
        ais_deviation_known_span.set_attribute('ais.deviationKnown.sourceRef', source_ref)

        target_ref = extensions['target_ref']
        ais_deviation_known_span.set_attribute('ais.deviationKnown.targetRef', target_ref)

        description = extensions['description']
        ais_deviation_known_span.set_attribute('ais.deviationKnown.description', description)

        # TODO: error handling
        return jsonify({'data': 'Unknown deviation updated successfully', 'receivedInformation': data})

def ab_trigger_audit(vin, scan_type):
    """
    Trigger an audit to audit a vehicle with a specific VIN.

    :param vin: vehicle identification number
    :param scan_type: type of scan; 1 is fast scan, 2 is deep scan
    """
    req_obj = {"AB_id": 28, "timeStamp": str(time.time()), "VIN": str(vin), "scanType": scan_type, "priority": 1}

    response = requests.get(sota_endpoint, json=req_obj)
    return Response(
            response.text,
            status = response.status_code,
            content_type = response.headers['content-type'],
            )

@app.route('/ab/vulnReport', methods=['POST'])
def ab_vuln_report():

    data = request.get_json(force=True)

    with tracer.start_as_current_span('ab.vulnReport') as ab_vuln_report_span:
        ab_ID = data['AB_id']
        ab_vuln_report_span.set_attribute('ab.vulnReport.abID', ab_ID)

        timeStamp = data['timeStamp']
        ab_vuln_report_span.set_attribute('ab.vulnReport.timeStamp', timeStamp)

        vin = data['VIN']
        ab_vuln_report_span.set_attribute('ab.vulnReport.vin', vin)

        scanType = data['scanType']
        ab_vuln_report_span.set_attribute('ab.vulnReport.scanType', scanType)

        result = data['result']
        ab_vuln_report_span.set_attribute('ab.vulnReport.result', result)

        # TODO: error handling
        return jsonify({'data': 'Vulnerability report received successfully', 'receivedInformation': data})


app.route('/vsoc/getTrustScore', methods=['GET'])
def vsoc_get_trustscore():
    """
    Getting the trust-score for a specific entity and distributing it.
    """
    # file ./trust-score.py

    return ""

#
#
#
# Deprecated endpoints below
#
#
#

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
        #message = request.get_json().get('message')
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

# Add more endpoints and methods here as needed

@app.errorhandler(HTTPStatus.NOT_FOUND.value)
def not_found(error):
    return jsonify({"error":"The requested URL does not exist"}), HTTPStatus.NOT_FOUND.value

@app.errorhandler(HTTPStatus.UNSUPPORTED_MEDIA_TYPE.value)
def unsupported_mimetype(error):
    return jsonify({"error":"Only application/json is currently supported"}), HTTPStatus.UNSUPPORTED_MEDIA_TYPE.value

def parse_and_validate_data(required_fields: list[str]) -> Any:
    json_data: Any
    try:
        json_data = request.get_json()
    except BadRequest:
        abort_with_message("The data could not be parsed as valid JSON", HTTPStatus.BAD_REQUEST.value)
        return
    if not all(field in json_data for field in required_fields):
        abort_with_message("The JSON is valid but it doesn't have all the required fields", HTTPStatus.BAD_REQUEST.value)
        return
    return json_data

def abort_with_message(message: str, code: int) -> None:
    abort(make_response(jsonify(error=message), code))

if __name__ == '__main__':
    app.run()
