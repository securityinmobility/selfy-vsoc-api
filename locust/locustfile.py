from locust import HttpUser, task, constant_throughput
from secrets import token_hex

HttpUser.host = "http://127.0.0.1:8000"
HttpUser.wait_time = constant_throughput(10)


class SOTAUser(HttpUser):
    @task
    def update_info(self):
        request = {
            "toolId": 8,
            "timeStamp": "2023-11-21T06:14:00Z",
            "vin": "2a910ebe-b39a-4813-9992-373738ab4599",
            "action": "1",
            "deviceID": 8,
            "status": 2,
            "deviceMetadata": "Such nice metadata",
        }
        self.client.post("/sota/updateInfo", json=request)


class RASUser(HttpUser):
    @task
    def attestation_result(self):
        request = {
            "verifier": "ID18",
            "VSOC": "ID08",
            "target_tool": "ID19",
            "state": 0,
            "nonce": token_hex(32),
            "created": "2023-06-05 12:00:00 UTC",
        }
        self.client.post("/ras/attestationResult", json=request)


class ABUser(HttpUser):
    @task
    def vuln_report(self):
        request = {
            "AB_id": 28,
            "timeStamp": "2023-11-21T06:14:00Z",
            "VIN": "WAUEA88DXTA287834",
            "scanType": 0,
            "result": True
        }
        self.client.post("/ab/vulnReport", json=request)


class AISUser(HttpUser):
    @task
    def deviation_known(self):
        request = {
            "extension_type": "property-extension",
            "source_vehicle": "12",
            "source_ais": "24",
            "source_rsu": "55",
            "observable": {
                "type": "type",
                "value": "value",
            },
            "id": "relationship--0ee40e86-99ce-405f-820e-d5d4e2648ca4",
            "source_ref": "indicator--e5c3e257-031f-4df1-88a3-19bbd25acacc",
            "target_ref": "indicator--11b76a96-5d2b-45e0-8a5a-f6994f370731",
            "description": "An immunological algorithm detected a deviation in a real-time data set "
                           "that is apparently similar to a previously reported deviation.",
        }
        self.client.post("/ais/deviationKnown", json=request)
