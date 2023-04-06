from app import app, db, mqttc, socketio_app, Devices, Rooms
from flask_socketio import emit
import json


@socketio_app.on('setupDevices')
def setup(devices):
    for device in devices:
        db_record = Devices.query.filter_by(
            _mqttId=device["mqtt_Id"]).first()
        if (db_record):
            device["status"] = db_record._status
            device["settings"] = db_record._settings if db_record._settings != None else {}
        else:
            newDevice = Devices(
                _id=int(device["id"]), _type=device["type"], _mqttId=device["mqtt_Id"], _status="Off")
            db.session.add(newDevice)
            db.session.commit()
            device["status"] = "Off"
        print("SETUP " + str(device))
    emit("setupDevices", devices)


@socketio_app.on('setupRoom')
def setup(room):
    db_record = Rooms.query.filter_by(
        _id=room["id"]).first()

    emit("setupRoom", {'temp': db_record._temperature,
                       "humidity": db_record._humidity, "pearsonCount": db_record._pearsonCount}, broadcast=True)


@socketio_app.on('changeState')
def setup(devices):
    for device in devices:
        dbDev = Devices.query.filter_by(
            _mqttId=device["mqtt_Id"]).first()
        dbDev._settings = device['settings']
        dbDev._status = device['status']
        db.session.commit()
        mqttc.publish(device["mqtt_Id"], json.dumps(
            device['settings']))

        if device['emit']:
            emit("stateChanged", device, broadcast=True)
    print(device["name"] + ": " + str(device["settings"]))
