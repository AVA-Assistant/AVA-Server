from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///IoT_Devices.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class onOff(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    _mqttId = db.Column(db.String, unique=True, nullable=False)
    _state = db.Column(db.Boolean, nullable=False)
    _status = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"<Device: {self._mqttId}>"


class brightness(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    _mqttId = db.Column(db.String, unique=True, nullable=False)
    _state = db.Column(db.Boolean, nullable=False)
    _value = db.Column(db.Float, nullable=False)
    _status = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"<Device: {self._mqttId}>"


class rgb(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    _mqttId = db.Column(db.String, unique=True, nullable=False)
    _state = db.Column(db.Boolean, nullable=False)
    _mode = db.Column(db.String, nullable=False)
    _value = db.Column(db.Integer, nullable=False)
    _status = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"<Device: {self._mqttId}>"


class rgbCct(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    _mqttId = db.Column(db.String, unique=True, nullable=False)
    _state = db.Column(db.Boolean, nullable=False)
    _mode = db.Column(db.String, nullable=False)
    _rgbValue = db.Column(db.Integer, nullable=False)
    _cctValue = db.Column(db.Integer, nullable=False)
    _status = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"<Device: {self._mqttId}>"


with app.app_context():
    db.create_all()
