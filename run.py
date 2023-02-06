from app import app, mqttc, routes, socketio_app

# mqttc.connect("localhost", 2000)
# mqttc.loop_start()

if __name__ == "__main__":
    socketio_app.run(app=app, host='10.10.5.233', port=2500)
