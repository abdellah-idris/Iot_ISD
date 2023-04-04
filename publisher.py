import paho.mqtt.client as mqtt
import time
from random import randrange,uniform

tankID=""
def on_message(client, userdata,message):
    global tankID
    tankID=str(message.payload.decode("utf-8"))

mqttBroker="192.168.0.102"
client=mqtt.Client("Dolhamid")
client.connect(mqttBroker)
client.subscribe("Dolhamid")
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