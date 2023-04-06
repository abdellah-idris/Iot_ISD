from flask import Flask, render_template, redirect, url_for
import paho.mqtt.client as mqtt


tankID = None
team = ""
qrcode = ""
affichage = ""

mqttBroker = "192.168.0.102"
client = mqtt.Client("Dolhamid_server")

try:
    client.connect(mqttBroker)
except TimeoutError:
    raise TimeoutError("Timeout")


def on_message(client, userdata, message):
    global tankID, team, qrcode, affichage
    liste_msg = message.payload.decode("utf-8").split()

    if liste_msg[0] == "Dolhamid":
        tankID = liste_msg[1]
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
        affichage = "START_CATCHING"
    elif liste_msg[0] == "FLAG_CATCHED":
        affichage = "FLAG_CATCHED"
    elif liste_msg[0] == "ABORT_CATCHING_EXIT":
        affichage = "ABORT_CATCHING_EXIT"
    elif message.topic == "tanks/" + tankID + "/shots/in" and liste_msg[0] == "SHOT":
        affichage = "SHOT IN"
    elif message.topic == "tanks/" + tankID + "/shots/out" and liste_msg[0] == "SHOT":
        affichage = "SHOT OUT"
    elif liste_msg[0] == "FRIENDLY_FIRE":
        affichage = "FRIENDLY_FIRE"
    elif liste_msg[0] == "FLAG_LOST":
        affichage = "FLAG_LOST"
    elif liste_msg[0] == "ABORT_CATCHING_SHOT":
        affichage  = "ABORT_CATCHING_SHOT"
    elif liste_msg[0] == "SCAN_SUCCESSFUL":
        affichage = "SCAN_SUCCESSFUL"
    elif liste_msg[0] == "SCAN_FAILED":
        affichage = "SCAN_FAILED"
    elif liste_msg[0] == "WIN " + team:
        affichage = "WIN " + team


client.subscribe("Dolhamid")
client.on_message = on_message

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('client_ui.html', rasptank_ID=tankID, team=team, qrcode=qrcode, affichage=affichage)


@app.route("/servo/<id>")
def servo(id):
    try:
        client.publish("servo" + tankID, id)
    except:
        print("Timeout")

    return redirect('/')


@app.route("/move/<id>")
def move(id):
    try:
        client.publish("move" + tankID, id)
    except:
        print("Timeout")

    return redirect('/')


@app.route("/shoot/")
def shoot():
    try:
        client.publish("shoot" + tankID, '*')
    except:
        print("Timeout")

    return redirect('/')


@app.route("/picture/")
def picture():
    try:
        client.publish("picture" + tankID, "*")
    except:
        print("Timeout")

    return redirect('/')


# run the app
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
