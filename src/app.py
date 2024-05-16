from typing import Any

import requests
import time
import uuid
import json
import http.client

from flask import Flask, jsonify, request, Response, abort, make_response
from werkzeug.exceptions import BadRequest
from http import HTTPStatus
from jsonschema import validate, ValidationError

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


# Default
@app.route('/')
def index():
    return jsonify({'SELFY VSOC': 'by THI',
                    'version': 'v0.2'})


def sota_request_update(vin, action):
    """
    Requests and update to the SOTA infrastructure.

    :param vin: vehicle identification number
    :param action: 1 update, 0 nothing, 2 tbd
    """
    # {"toolId": 8, "timeStamp": "2023-11-21T06:14:00Z", "VIN": "2a910ebe-b39a-4813-9992-373738ab4599", "action": 1}
    req_obj = {"toolId": 8, "timeStamp": str(time.time()), "VIN": str(vin), "action": action}

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

    schema_path = 'jsonschemas/sota/updateInfo.json'
    opentelemetry_prefix = 'sota.updateInfo'

    request_json = parse_and_validate_data(schema_path)

    return response_to_json(request_json, schema_path, opentelemetry_prefix)


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
        status=response.status_code,
        content_type=response.headers['content-type'],
    )


@app.route('/ras/attestationResult', methods=['POST'])
def ras_attestation_result():
    schema_path = 'jsonschemas/ras/attestationResult.json'
    opentelemetry_prefix = 'ras.attestationResult'

    request_json = parse_and_validate_data(schema_path)

    return response_to_json(request_json, schema_path, opentelemetry_prefix)


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
            cfg_json = {"configuration_param" + str(i): x for x in config}

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
        status=response.status_code,
        content_type=response.headers['content-type'],
    )


@app.route('/ais/deviationUnknown', methods=['POST'])
def ais_deviation_unknown():
    """
    Getting information from the AIS for an unknown deviation.
    """
    schema_path: str = 'jsonschemas/ais/deviationUnknown.json'
    opentelemetry_prefix = 'ais.deviationUnknown'

    request_json = parse_and_validate_data(schema_path)

    return response_to_json(request_json['extensions']['extension-definition--d83fce45-ef58-4c6c-a3f4-1fbc32e98c6e'],
                            schema_path, opentelemetry_prefix)


@app.route('/ais/deviationKnown', methods=['POST'])
def ais_deviation_known():
    """
    Getting information from the AIS for an unknown deviation.
    """
    schema_path: str = 'jsonschemas/ais/deviationUnknown.json'
    opentelemetry_prefix = 'ais.deviationUnknown'

    request_json = parse_and_validate_data(schema_path)

    return response_to_json(request_json['extensions']['extension-definition--d83fce45-ef58-4c6c-a3f4-1fbc32e98c6e'],
                            schema_path,
                            opentelemetry_prefix)  # request_json[0] had to be removed (can't access a dictionary that way)


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
        status=response.status_code,
        content_type=response.headers['content-type'],
    )


@app.route('/ab/vulnReport', methods=['POST'])
def ab_vuln_report():
    schema_path = 'jsonschemas/ab/vulnReport.json'
    opentelemetry_prefix = 'ab.vulnReport'

    request_json = parse_and_validate_data(schema_path)

    return response_to_json(request_json, schema_path, opentelemetry_prefix)


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

# Utilities

def response_to_json(request_json, schema_path, opentelemetry_prefix):
    with tracer.start_as_current_span(opentelemetry_prefix) as sota_updateInfo_span:
        for required_item, value in iterate_required_items(schema_path, request_json):
            sota_updateInfo_span.set_attribute(opentelemetry_prefix + '.' + required_item.lower(), value)

    response['statusCode'] = 200
    response['statusMessage'] = http.client.responses[response['statusCode']]
    response['data'] = request_json
    return jsonify(response), response['statusCode']


# Function to validate the request with the json schema
def validate_json_with_schema(schema_path, json_dict) -> bool:
    with open(schema_path, 'r') as f:
        schema = json.load(f)
        try:
            validate(instance=json_dict, schema=schema)
            return True
        except ValidationError:
            abort_with_message(message="The JSON is valid but it doesn't have all the required fields",
                               status_code=HTTPStatus.BAD_REQUEST,
                               span="http.badRequest")


# Function to iterate through required items
def iterate_required_items(schema_path, validated_json):
    with open(schema_path, 'r') as f:
        schema = json.load(f)
        required_items = schema.get("required", [])
        for required_item in required_items:
            yield required_item, validated_json.get(required_item)


def parse_and_validate_data(schema_path: str) -> Any:
    """
    Parses the ingoing request and aborts if
    the mime-type is not `application/json`,
    the data can not be parsed as JSON,
    or the JSON schema is not satisfied

    :param schema_path: file path of the JSON schema
    """
    json_data: Any = None

    if not request.data and request.is_json:
        abort_with_message(message="There was no data in the request",
                           status_code=HTTPStatus.BAD_REQUEST,
                           span="http.badRequest")

    try:
        json_data = request.get_json()  # will abort with code 415 if mime-type is not application/json
    except BadRequest:
        abort_with_message(message="The data could not be parsed as valid JSON",
                           status_code=HTTPStatus.BAD_REQUEST,
                           span="http.badRequest")

    if validate_json_with_schema(schema_path, json_data):
        return json_data


def abort_with_message(message: str, status_code: int, span: str = None) -> None:
    if span is not None:
        create_error_trace(message, status_code, span)

    abort(make_response(jsonify(error=message), status_code))


def create_error_trace(message: str, status_code: int, span: str) -> None:
    with tracer.start_as_current_span(span) as current_span:
        current_span.set_attribute(f"{span}.errorMessage", message)
        current_span.set_attribute(f"{span}.statusCode", status_code)
        current_span.set_attribute(f"{span}.headers", str(request.headers))
        current_span.set_attribute(f"{span}.body", request.data)


@app.errorhandler(HTTPStatus.NOT_FOUND)  # 404
def not_found(_):
    message: str = "The requested URL does not exist"
    status_code: int = HTTPStatus.NOT_FOUND
    create_error_trace(message, status_code, "http.notFound")
    return jsonify(error=message), status_code


@app.errorhandler(HTTPStatus.METHOD_NOT_ALLOWED)  # 405
def method_not_allowed(_):
    message: str = "The requested method is not allowed"
    status_code: int = HTTPStatus.METHOD_NOT_ALLOWED
    create_error_trace(message, status_code, "http.methodNotAllowed")
    return jsonify(error=message), status_code


@app.errorhandler(HTTPStatus.UNSUPPORTED_MEDIA_TYPE)  # 415
def unsupported_mimetype(_):
    message: str = "Only application/json is currently supported"
    status_code: int = HTTPStatus.UNSUPPORTED_MEDIA_TYPE
    create_error_trace(message, status_code, "http.unsupportedMediaType")
    return jsonify(error=message), status_code


if __name__ == '__main__':
    app.run()
