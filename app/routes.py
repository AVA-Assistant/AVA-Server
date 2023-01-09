from app import app, db, mqttc, IoT_device
from flask import request
import json


@app.route('/led', methods=['POST'])
def led():
    value = request.get_json()

    mqttc.publish("led", json.dumps({"state": value.get("status")}))

    device = IoT_device.query.filter_by(name="led_1").first()
    device.status = value.get("state")
    db.session.commit()

    return value, 200


@app.route('/ledStatus', methods=['GET'])
def ledStatus():
    device = IoT_device.query.filter_by(name="led_1").first()

    return str(device.status),  200
