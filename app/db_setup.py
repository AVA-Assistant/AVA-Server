from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///IoT_Devices.db'
db = SQLAlchemy(app)


class IoT_device(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    status = db.Column(db.Integer, nullable=False)


with app.app_context():

    db.create_all()
    led_1 = IoT_device(name="led_1", status=0)
    db.session.add(led_1)
    db.session.commit()