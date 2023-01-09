from app import app, mqttc, routes

mqttc.connect("192.168.1.191", 2000)
mqttc.loop_start()

if __name__ == "__main__":
    app.run(host='192.168.1.191', port=2500)
