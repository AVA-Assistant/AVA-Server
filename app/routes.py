from app import app, db, mqttc, IoT_device
from flask import request
import json


@app.route('/led', methods=['POST'])
def led():
    value = request.get_json()

    mqttc.publish("led", json.dumps({"state": value.get("state")}))

    device = IoT_device.query.filter_by(name="led_1").first()
    device.state = value.get("state")
    db.session.commit()

    return value, 200


@app.route('/ledState', methods=['GET'])
def ledState():
    device = IoT_device.query.filter_by(name="led_1").first()

    return str(device.state),  200
