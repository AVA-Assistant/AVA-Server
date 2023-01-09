from app import app
import json
from app import mqttc
from flask import request


@app.route('/led', methods=['POST'])
def led():
    value = request.get_json()

    mqttc.publish("led", json.dumps({"state": value.get("status")}))

    return value, 200
