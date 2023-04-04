from flask import Flask, render_template, request, redirect, url_for
import paho.mqtt.client as mqtt
import time
from random import randrange, uniform

tankID = None
team = ""
qrcode = None
mqttBroker = "192.168.0.102"
client = mqtt.Client("Dolhamid")
client.connect(mqttBroker)


def on_message(client, userdata, message):
    global tankID, team, qrcode
    liste_msg = message.payload.decode("utf-8").split()
    if liste_msg[0] == "Dolhamid":
        tankID = message.payload.decode("utf-8")
        client.subscribe("tanks/" + tankID + "/init")
        client.subscribe("tanks/" + tankID + "/shots/in")
        client.subscribe("tanks/" + tankID + "/shots/out")
        client.subscribe("tanks/" + tankID + "/qr_code")
        client.subscribe("tanks/" + tankID + "/flag")
    elif liste_msg[0] == "TEAM":
        team = liste_msg[1]
    elif liste_msg[0] == "QR_CODE":
        qrcode = liste_msg[1]
    elif liste_msg[0] == "START_CATCHING":
        pass
    elif liste_msg[0] == "FLAG_CATCHED":
        pass
    elif liste_msg[0] == "ABORT_CATCHING_EXIT":
        pass
    elif message.topic == "tanks/" + tankID + "/shots/in" and liste_msg[0] == "SHOT":
        pass
    elif message.topic == "tanks/" + tankID + "/shots/out" and liste_msg[0] == "SHOT":
        pass
    elif liste_msg[0] == "FRIENDLY_FIRE":
        pass
    elif liste_msg[0] == "FLAG_LOST":
        pass
    elif liste_msg[0] == "ABORT_CATCHING_SHOT":
        pass
    elif liste_msg[0] == "SCAN_SUCCESSFUL":
        pass
    elif liste_msg[0] == "SCAN_FAILED":
        pass
    elif liste_msg[0] == "WIN " + team:
        pass


client.subscribe("Dolhamid")
client.on_message = on_message

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('client_ui.html')


@app.route("/servo/<id>")
def servo(id):
    client.publish("servo" + tankID, id)
    return redirect('/')


@app.route("/move/<id>")
def move(id):
    client.publish("move" + tankID, id)
    return redirect('/')


@app.route("/shoot/")
def shoot():
    client.publish("shoot" + tankID, '*')
    return redirect('/')


@app.route("/picture/")
def picture():
    client.publish("picture" + tankID, "*")
    return redirect('/')


# run the app
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
