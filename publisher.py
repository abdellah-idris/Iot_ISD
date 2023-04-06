import paho.mqtt.client as mqtt
import time
from random import randrange,uniform

tankID=None
team=""
qrcode=None

def on_message(client, userdata,message):
    global tankID,team,qrcode
    liste_msg=message.payload.decode("utf-8").split()
    if liste_msg[0]=="Dolhamid":
        tankID=liste_msg[1]
        client.subscribe("tanks/"+tankID+"/init")
        client.subscribe("tanks/"+tankID+"/shots/in")
        client.subscribe("tanks/"+tankID+"/shots/out")
        client.subscribe("tanks/"+tankID+"/qr_code")
        client.subscribe("tanks/"+tankID+"/flag")
    elif liste_msg[0]=="TEAM":
        team=liste_msg[1]
    elif liste_msg[0]=="QR_CODE":
        qrcode=liste_msg[1]
    elif liste_msg[0]=="START_CATCHING":
        pass
    elif liste_msg[0]=="FLAG_CATCHED":
        pass
    elif liste_msg[0]=="ABORT_CATCHING_EXIT":
        pass
    elif message.topic=="tanks/"+tankID+"/shots/in" and  liste_msg[0]=="SHOT":
        pass
    elif message.topic=="tanks/"+tankID+"/shots/out" and  liste_msg[0]=="SHOT":
        pass
    elif liste_msg[0]=="FRIENDLY_FIRE":
        pass
    elif liste_msg[0]=="FLAG_LOST":
        pass
    elif liste_msg[0]=="ABORT_CATCHING_SHOT":
        pass
    elif liste_msg[0]=="SCAN_SUCCESSFUL":
        pass
    elif liste_msg[0]=="SCAN_FAILED":
        pass
    elif liste_msg[0]=="WIN "+team:
        pass
mqttBroker="192.168.0.102"
client=mqtt.Client("Dolhamid_client")
client.connect(mqttBroker)
client.loop_start()
client.subscribe("Dolhamid_")
client.on_message=on_message

while True:

    msg=input("cmd:")
    if msg=="a":
        client.publish("servo"+tankID,"11_0")
    elif msg=="z":
        client.publish("servo"+tankID,"12_0")
    elif msg=="e":
        client.publish("servo"+tankID,"13_0")
    elif msg=="r":
        client.publish("servo"+tankID,"14_0")
    elif msg=="t":
        client.publish("servo"+tankID,"15_0")
    if msg=="q":
        client.publish("servo"+tankID,"11_1")
    elif msg=="s":
        client.publish("servo"+tankID,"12_1")
    elif msg=="d":
        client.publish("servo"+tankID,"13_1")
    elif msg=="f":
        client.publish("servo"+tankID,"14_1")
    elif msg=="g":
        client.publish("servo"+tankID,"15_1")
    elif msg=="u":
        client.publish("move"+tankID,"forward_no")
    elif msg=="n":
        client.publish("move"+tankID,"backward_no")
    elif msg=="k":
        client.publish("move"+tankID,"no_right")
    elif msg=="h":
        client.publish("move"+tankID,"no_left")
    elif msg=="i":
        client.publish("move"+tankID,"forward_right")
    elif msg=="o":
        client.publish("move"+tankID,"forward_left")
    elif msg=="p":
        client.publish("move"+tankID,"backward_right")
    elif msg=="l":
        client.publish("move"+tankID,"backward_left")
    elif msg=="m":
        client.publish("picture"+tankID,"*")