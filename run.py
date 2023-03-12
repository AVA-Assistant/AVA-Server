from app import app, mqttc, routes, socketio_app

mqttc.connect("localhost", 2000)
mqttc.loop_start()

if __name__ == "__main__":
    socketio_app.run(app=app, host='localhost', port=2500)
