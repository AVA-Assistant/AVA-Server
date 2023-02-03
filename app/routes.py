from app import app, db, mqttc, socketio_app, rgb, onOff, rgbCct, brightness
from flask_socketio import emit
import json


@socketio_app.on('setup')
def setup(devices):
    print(devices)
    for device in devices:
        if (device["type"] == "onf"):
            db_record = onOff.query.filter_by(
                _mqttId=device["mqtt_Id"]).first()
            if (db_record):
                device["state"] = db_record._state
            else:
                newDevice = onOff(_id=int(device["id"]),
                                  _mqttId=device["mqtt_Id"], _state=False)
                db.session.add(newDevice)
                db.session.commit()
