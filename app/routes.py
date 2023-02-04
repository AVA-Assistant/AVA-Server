from app import app, db, mqttc, socketio_app, rgb, onOff, rgbCct, brightness
from flask_socketio import emit, send
import json


@socketio_app.on('setup')
def setup(devices):
    for device in devices:
        if (device["type"] == "onf"):
            db_record = onOff.query.filter_by(
                _mqttId=device["mqtt_Id"]).first()
            if (db_record):
                device["status"] = "On" if db_record._state else "Off"
                device["state"] = {'status': db_record._state}
            else:
                newDevice = onOff(
                    _id=int(device["id"]), _mqttId=device["mqtt_Id"], _state=False)
                db.session.add(newDevice)
                db.session.commit()
        elif (device["type"] == "brht"):
            db_record = brightness.query.filter_by(
                _mqttId=device["mqtt_Id"]).first()
            if (db_record):
                device["status"] = "Off" if not db_record._state else '{db_record._value}%'
                device["state"] = {
                    "status": db_record._state, "value": db_record._value}
            else:
                newDevice = brightness(
                    _id=int(device["id"]), _mqttId=device["mqtt_Id"], _state=False, _value=0)
                db.session.add(newDevice)
                db.session.commit()
        elif (device["type"] == "rgb"):
            db_record = rgb.query.filter_by(
                _mqttId=device["mqtt_Id"]).first()
            if (db_record):
                device["status"] = "Off"
                device["state"] = {
                    "status": db_record._state, "mode": db_record._mode, "value": db_record._value}
            else:
                newDevice = rgb(
                    _id=int(device["id"]), _mqttId=device["mqtt_Id"], _state=False, _mode="auto", _value=0)
                db.session.add(newDevice)
                db.session.commit()
        elif (device["type"] == "rgbcct"):
            db_record = rgbCct.query.filter_by(
                _mqttId=device["mqtt_Id"]).first()
            if (db_record):
                device["status"] = "Off"
                device["state"] = {
                    "status": db_record._state, "mode": db_record._mode, "rgbValue": db_record._rgbValue, "cctValue": db_record._cctValue}
            else:
                newDevice = rgbCct(
                    _id=int(device["id"]), _mqttId=device["mqtt_Id"], _state=False, _mode="auto", _rgbValue=0, _cctValue=0)
                db.session.add(newDevice)
                db.session.commit()
    emit("setup", devices)
