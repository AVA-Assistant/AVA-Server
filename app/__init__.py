from flask import Flask
import paho.mqtt.client as mqtt
from flask_sqlalchemy import SQLAlchemy
import json
from flask_socketio import SocketIO
import uuid
import os


def on_connect(mqttc, obj, flags, rc):
    print("Connected!")


mqttc = mqtt.Client("AVA-Server_" + str(uuid.uuid4()))
mqttc.on_connect = on_connect


app = Flask(__name__)


basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'IoT_Devices.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
socketio_app = SocketIO(app, cors_allowed_origins="*")


class Devices(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    _type = db.Column(db.String, nullable=False)
    _mqttId = db.Column(db.String, unique=True, nullable=False)
    _status = db.Column(db.String, nullable=False)
    _baseline = db.Column(db.JSON(), nullable=True)
    _settings = db.Column(db.JSON(), nullable=True)

    def __repr__(self):
        return f"<Device: {self._mqttId}>"


class Rooms(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    _name = db.Column(db.String, nullable=False)
    _pearsonCount = db.Column(db.Integer, nullable=False)
    _temperature = db.Column(db.Float, nullable=False)
    _humidity = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<Room: {self._name}>"
