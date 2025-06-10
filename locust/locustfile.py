from locust import HttpUser, task, between, constant_throughput
from datetime import datetime
import random
from secrets import token_hex

HttpUser.host = "http://127.0.0.1:8000"
HttpUser.wait_time = constant_throughput(10)
wait_time = between(2, 2)

class VehicleSafetyStatUser(HttpUser):
    @task
    def post_vehicle_safety_status(self):
        velocity = random.randint(10, 50)
        risk = random.uniform(0, 1)

        self.client.post(
            "/sot/vehicleSafetyStatus",
            json={
                "VIN": "WUAWFAFLXB7K5C4A9",
                "operationMode": 0,
                "velocity": velocity,
                "gnssStatus": 0,
                "latitude": 41.404853005972576,
                "longitude": 2.202048715342343,
                "riskLevel": risk
            }
        )

class AISUser(HttpUser):
    @task 
    def deviationKnown(self):
        request = {
                "relationships": [
                    {
                        "type": "relationship",
                        "spec_version": "2.1",
                        "id": "relationship--a72b8f4a-bb5d-4b1e-abc5-9fd3c5d8c123",
                        "created": "2024-10-24T15:50:10.983Z",
                        "modified": "2024-10-24T15:50:10.983Z",
                        "relationship_type": "indicates",
                        "source_ref": "indicator--c23b8f7e-1a34-4a5b-8f2e-9fd4d7d8a567",
                        "target_ref": "indicator--d24a6f8c-bb2c-4a2e-abc9-9ed8c8b9c987"
                        }
                    ],
                "indicator": {
                    "type": "indicator",
                    "spec_version": "2.1",
                    "id": "indicator--c23b8f7e-1a34-4a5b-8f2e-9fd4d7d8a567",
                    "created": "2024-10-24T14:25:15.127Z",
                    "modified": "2024-10-24T14:25:15.127Z",
                    "name": "Anomaly detection",
                    "description": "An immunological algorithm detected a deviation in real-time dataset.",
                    "indicator_types": ["anomaly"],
                    "pattern": "[ipv4-addr:value = '192.168.1.1']",
                    "pattern_type": "stix",
                    "pattern_version": "2.1",
                    "valid_from": "2024-10-24T14:25:15.127Z",
                    "valid_until": "2024-12-24T14:25:15.127Z",
                    "labels": ["suspicious-activity"],
                    "extensions": {
                        "extension-definition--f62b6c4d-e9c5-42d7-b06a-c8e8d8c8c6a5": {
                            "extension_type": "property-extension"
                            }
                        },
                    "source_vehicle": "1HGBH41JXMN109186",
                    "source_ais": "AIS-1234",
                    "source_rsu": "RSU-5678",
                    "src_ref": "192.168.1.1",
                    "dst_ref": "10.0.0.1",
                    "src_port": "8080",
                    "dst_port": "443",
                    "protocol_type": "TCP",
                    "service": "http",
                    "flag": "SYN",
                    "timestamp": "2024-10-24T14:25:15.127Z"
                    }
                }
        self.client.post("/ais/deviationKnown", json=request)

    @task 
    def deviationUnknown(self):
        request = {
                "type": "indicator",
                "spec_version": "2.1",
                "id": "indicator--a25e9f78-8e9a-4c7b-821c-5b8a5fd9f0cb",
                "created": "2024-10-24T15:50:10.983Z",
                "modified": "2024-10-24T15:50:10.983Z",
                "name": "Anomaly detection",
                "description": "An immunological algorithm detected a deviation in real-time dataset.",
                "indicator_types": ["unknown-deviation"],
                "pattern": "[ipv4-addr:value = '203.0.113.10']",
                "pattern_type": "stix",
                "pattern_version": "2.1",
                "valid_from": "2024-10-24T15:50:10.983Z",
                "valid_until": "2024-12-24T15:50:10.983Z",
                "labels": ["unknown-anomaly"],
                "extensions": {
                    "extension-definition--b9f6a1b5-e9c7-4f65-b4b6-1f1c13e8e6f2": {
                        "extension_type": "property-extension"
                        }
                    },
                "source_vehicle": "1HGCM82633A123456",
                "source_ais": "AIS-unknown",
                "source_rsu": "RSU-unknown",
                "src_ref": "203.0.113.10",
                "dst_ref": "198.51.100.5",
                "src_port": "1234",
                "dst_port": "80",
                "protocol_type": "TCP",
                "service": "http",
                "flag": "ACK",
                "timestamp": "2024-10-24T15:50:10.983Z"
                }
        self.client.post("/ais/deviationUnknown", json=request)


class RASUser(HttpUser):
    @task 
    def attestationResult(self):
        request = {
                "verifier": "ID18",
                "VSOC": "ID08",
                "target_tool": "RAS12345",
                "state": 0,
                "nonce": "d9b4b5c7a2f45678",
                "created": "2024-10-24T15:50:10.983Z",
                "VIN": "1HGCM82633A123456"
                }

        self.client.post("/ras/attestationResult", json=request)


class RSUUser(HttpUser):
    @task 
    def misbehaviour(self):
        request = {
                "type": 1,
                "data": {
                    "v2x_agent_ids": [
                        {
                            "id": "V2X12345",
                            "obtained_timestamp": "2024-10-24T12:34:56Z"
                            },
                        {
                            "id": "V2X67890",
                            "obtained_timestamp": "2024-10-24T12:36:10Z"
                            }
                        ]
                    }
                }
        self.client.post("/rsu/misbehaviour", json=request)

class SOTUser(HttpUser):
    @task 
    def vehicleInfoArray(self):
        request = [
                {
                    "valid": True,
                    "vehicle_status": {
                        "acceleration": 1,
                        "throttle_input": 0,
                        "lane_position": -1
                        },
                    "platoon_status": {
                        "distance_error": 1,
                        "relative_speed": 0,
                        "id_of_preceeding_vehicle": 1001
                        },
                    "safety_mode": 1
                    },
                {
                    "valid": False,
                    "vehicle_status": {
                        "acceleration": 0,
                        "throttle_input": -1,
                        "lane_position": 1
                        },
                    "platoon_status": {
                        "distance_error": -1,
                        "relative_speed": 1,
                        "id_of_preceeding_vehicle": 1002
                        },
                    "safety_mode": 0
                    },
                {
                    "valid": True,
                    "vehicle_status": {
                        "acceleration": -1,
                        "throttle_input": 1,
                        "lane_position": 0
                        },
                    "platoon_status": {
                        "distance_error": 0,
                        "relative_speed": -1,
                        "id_of_preceeding_vehicle": 1003
                        },
                    "safety_mode": 2
                    }
                ]
        self.client.post("/sot/vehicleInfoArray", json=request)

class SOTAUser(HttpUser):
    @task 
    def updateInfo(self):
        request = {
                "selfy_id": 12345,
                "timeStamp": "2024-10-24T12:34:56Z",
                "message": {
                    "action": 1,
                    "vin": "1HGCM82633A123456",
                    "deviceID": "Device5678",
                    "status": 1,
                    "deviceMetadata": "Update version 2.1.5 available"
                    }
                }
        self.client.post("/sota/updateInfo", json=request)

class ABUser(HttpUser):
    @task
    def heartbeat(self):
        request = {
                "AB_id": 0,
                "timeStamp": datetime.utcnow().isoformat() + "Z",
                "DTCs": 0,
                "lastResetTimeStamp": datetime.utcnow().isoformat() + "Z",
                "lastResetCause": 0
                }
        self.client.post("/ab/heartbeat", json=request)

    @task 
    def jamAlarm(self):
        request = {
                "type": "bundle",
                "id": "bundle--123e4567-e89b-12d3-a456-426614174000",
                "objects": [
                    {
                        "type": "identity",
                        "spec_version": "2.1",
                        "id": "identity--123e4567-e89b-12d3-a456-426614174001",
                        "created": "2024-10-25T14:30:00Z",
                        "modified": "2024-10-25T14:30:00Z",
                        "name": "Audit Box SELFY Solution",
                        "description": "Identity of the Audit Box SELFY Solution."
                        },
                    {
                        "type": "attack-pattern",
                        "spec_version": "2.1",
                        "id": "attack-pattern--123e4567-e89b-12d3-a456-426614174002",
                        "created": "2024-10-25T14:30:00Z",
                        "modified": "2024-10-25T14:30:00Z",
                        "name": "Jamming",
                        "external_references": [
                            {
                                "source_name": "MITRE",
                                "external_id": "T1200"
                                }
                            ]
                        },
                    {
                        "type": "intrusion-set",
                        "spec_version": "2.1",
                        "id": "intrusion-set--123e4567-e89b-12d3-a456-426614174003",
                        "created": "2024-10-25T14:30:00Z",
                        "modified": "2024-10-25T14:30:00Z",
                        "name": "Jamming",
                        "description": "Jamming situation detected near the Audit Box",
                        "first_seen": "2024-10-24T14:30:00Z",
                        "last_seen": "2024-10-25T14:30:00Z"
                        },
                    {
                        "type": "relationship",
                        "spec_version": "2.1",
                        "id": "relationship--123e4567-e89b-12d3-a456-426614174004",
                        "created": "2024-10-25T14:30:00Z",
                        "modified": "2024-10-25T14:30:00Z",
                        "relationship_type": "indicates",
                        "source_ref": "intrusion-set--123e4567-e89b-12d3-a456-426614174003",
                        "target_ref": "attack-pattern--123e4567-e89b-12d3-a456-426614174002"
                        }
                    ]
                }
        self.client.post("/ab/jamAlarm", json=request)

    @task 
    def vulnReport(self):
        request = {
                "AB_id": 12345,
                "timeStamp": "2024-10-31T12:00:00Z",
                "VIN": "1HGCM82633A123456",
                "scanType": 1,
                "result": True
                }
        self.client.post("/ab/vulnReport", json=request)

    @task 
    def vulnReportKO(self):
        request = {
                "type": "bundle",
                "id": "bundle--bffb7325-cc64-40b4-9b3b-55d2b6d5e857",
                "objects": [
                    {
                        "type": "identity",
                        "spec_version": "2.1",
                        "id": "identity--0e49eb8f-1b4b-4931-975f-0e3454817f8c",
                        "created": "2024-10-25T12:00:00Z",
                        "modified": "2024-10-25T12:00:00Z",
                        "name": "Audit Box SELFY Solution",
                        "description": "An identity representing the Audit Box SELFY Solution.",
                        "identity_class": "vehicle identification number (VIN)"
                        },
                    {
                        "type": "vulnerability",
                        "spec_version": "2.1",
                        "id": "vulnerability--b56c09f8-d0b0-4565-914b-b7455f5d84f2",
                        "created": "2024-10-20T10:00:00Z",
                        "modified": "2024-10-21T15:00:00Z",
                        "name": "CVE-2024-56789",
                        "description": "SQL injection vulnerability in the database module."
                        },
                    {
                        "type": "course-of-action",
                        "spec_version": "2.1",
                        "id": "course-of-action--54f1b1a3-8963-4df1-a98c-6f57c1a2e72f",
                        "created": "2024-10-20T12:00:00Z",
                        "modified": "2024-10-21T15:00:00Z",
                        "name": "80",
                        "description": "Update the database module to prevent SQL injection."
                        },
                    {
                        "type": "relationship",
                        "spec_version": "2.1",
                        "id": "relationship--cc93b8ae-5b80-45db-9e3a-e6a1a1b29299",
                        "created": "2024-10-20T10:00:00Z",
                        "modified": "2024-10-21T15:00:00Z",
                        "relationship_type": "mitigates",
                        "source_ref": "vulnerability--b56c09f8-d0b0-4565-914b-b7455f5d84f2",
                        "target_ref": "course-of-action--54f1b1a3-8963-4df1-a98c-6f57c1a2e72f"
                        },
                    {
                        "type": "software",
                        "spec_version": "2.1",
                        "id": "software--123455",
                        "name": "Software",
                        "vendor":  "Software Vendor",
                        "version": "v.0.3"
                        }
                    ]
                }
        self.client.post("/ab/vulnReportKO", json=request)

    @task 
    def configStatus(self):
        request = {
                "AB_id": 12345,
                "timeStamp": "2024-10-31T10:30:00Z",
                "Enable": 1,
                "Selectivemode": 2,
                "MINTIMETORESCAN": 15,
                "JAMSIGFREQ": 30,
                "HEARTBEATFREQ": 60,
                "AUDITTECHS": "CAN, LIN, FlexRay"
                }
        self.client.post("/ab/configStatus", json=request)
