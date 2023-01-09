from flask import Flask
import paho.mqtt.client as mqtt


def on_connect(mqttc, obj, flags, rc):
    print("Connected!")


mqttc = mqtt.Client("Publisher")
mqttc.on_connect = on_connect
mqttc.connect("192.168.1.191", 2000)
mqttc.loop_start()

app = Flask(__name__)
