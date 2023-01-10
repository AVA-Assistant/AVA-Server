from app import app, db, mqttc, IoT_device, socketio_app
from flask_socketio import emit
import json


@socketio_app.on('ledState')
def ledState():
    device = IoT_device.query.filter_by(name="led_1").first()
    emit('ledState', json.dumps({"state": str(device.state)}))


@socketio_app.on("led")
def led(msg):

    mqttc.publish("led", json.dumps({"state": msg["state"]}))

    device = IoT_device.query.filter_by(name="led_1").first()
    device.state = msg["state"]
    db.session.commit()

    if msg["final"] == True:
        emit("led",  json.dumps(msg), broadcast=True)
