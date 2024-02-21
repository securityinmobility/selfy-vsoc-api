from flask import Flask, jsonify, request, Response
import requests
import time

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

sota_endpoint = "http://uptane-bridge.sota.selfy.ota.ce/vsoctrigger"

# Default
@app.route('/')
def index():
    return jsonify({'SELFY VSOC': 'by THI',
                       'version': 'v0.1'})

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
    data = request.get_json(force=True)

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

if __name__ == '__main__':
    app.run()
