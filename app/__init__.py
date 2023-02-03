from flask import Flask
import paho.mqtt.client as mqtt
from flask_sqlalchemy import SQLAlchemy
import json
from flask_socketio import SocketIO
import uuid


def on_connect(mqttc, obj, flags, rc):
    print("Connected!")


mqttc = mqtt.Client("AVA-Server_" + str(uuid.uuid4()))
mqttc.on_connect = on_connect


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///IoT_Devices.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
socketio_app = SocketIO(app, cors_allowed_origins="*")


class onOff(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    _mqttId = db.Column(db.String, unique=True, nullable=False)
    _state = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f"<Device: {self._mqttId}>"


class brightness(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    _mqttId = db.Column(db.String, unique=True, nullable=False)
    _state = db.Column(db.Boolean, nullable=False)
    _value = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Device: {self._mqttId}>"


class rgb(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    _mqttId = db.Column(db.String, unique=True, nullable=False)
    _state = db.Column(db.Boolean, nullable=False)
    _mode = db.Column(db.String, nullable=False)
    _value = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Device: {self._mqttId}>"


class rgbCct(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    _mqttId = db.Column(db.String, unique=True, nullable=False)
    _state = db.Column(db.Boolean, nullable=False)
    _mode = db.Column(db.String, nullable=False)
    _rgbValue = db.Column(db.Integer, nullable=False)
    _cctValue = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Device: {self._mqttId}>"
