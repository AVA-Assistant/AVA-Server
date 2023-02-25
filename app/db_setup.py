from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///IoT_Devices.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Devices(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    _type = db.Column(db.String, nullable=False)
    _mqttId = db.Column(db.String, unique=True, nullable=False)
    _state = db.Column(db.Boolean, nullable=False)
    _status = db.Column(db.String, nullable=False)
    _settings = db.Column(
        db.JSON(), nullable=False)

    def __repr__(self):
        return f"<Device: {self._mqttId}>"


class Rooms(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    _name = db.Column(db.String, nullable=False)
    _pearsonCount = db.Column(db.Integer, nullable=False)
    _pearsonList = db.Column(db.Table, nullable=True)
    _temperature = db.Column(db.Float, nullable=False)
    _humidity = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<Room: {self._name}>"


with app.app_context():
    db.create_all()
