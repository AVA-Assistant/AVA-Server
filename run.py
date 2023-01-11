from app import app, mqttc, routes, socketio_app

mqttc.connect("192.168.0.100", 2000)
mqttc.loop_start()

if __name__ == "__main__":
    socketio_app.run(app=app, host='192.168.0.100', port=2500)
