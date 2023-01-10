from flask import Flask
import paho.mqtt.client as mqtt
from flask_sqlalchemy import SQLAlchemy
import json
from flask_socketio import SocketIO


def on_connect(mqttc, obj, flags, rc):
    print("Connected!")
    with app.app_context():
        device = IoT_device.query.filter_by(name="led_1").first()
        mqttc.publish("led", json.dumps({"state": device.state}))


mqttc = mqtt.Client("Publisher")
mqttc.on_connect = on_connect


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///IoT_Devices.db'
db = SQLAlchemy(app)
socketio_app = SocketIO(app, cors_allowed_origins="*")


class IoT_device(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    state = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Device: {self.name}>"
