from app import app, db, mqttc, IoT_device, socketio_app
from flask_socketio import send
import json


@socketio_app.on('ledState')
def ledState():
    device = IoT_device.query.filter_by(name="led_1").first()

    send({"state": str(device.state)})


@socketio_app.on("led")
def led(msg):

    mqttc.publish("led", json.dumps({"state": msg.get("state")}))

    device = IoT_device.query.filter_by(name="led_1").first()
    device.state = msg.get("state")
    db.session.commit()

    if msg.get("final") == True:
        send(msg, broadcast=True)
