import paho.mqtt.client as mqtt
import time
from random import randrange,uniform


mqttBroker="mqtt.eclipseprojects.io"
client=mqtt.Client("hamid")
client.connect(mqttBroker)
while True:

    msg=input("cmd:")
    if msg=="a":
        client.publish("servo","11_0")
    elif msg=="z":
        client.publish("servo","12_0")
    elif msg=="e":
        client.publish("servo","13_0")
    elif msg=="r":
        client.publish("servo","14_0")
    elif msg=="t":
        client.publish("servo","15_0")
    if msg=="q":
        client.publish("servo","11_1")
    elif msg=="s":
        client.publish("servo","12_1")
    elif msg=="d":
        client.publish("servo","13_1")
    elif msg=="f":
        client.publish("servo","14_1")
    elif msg=="g":
        client.publish("servo","15_1")
    elif msg=="u":
        client.publish("move","forward_no")
    elif msg=="n":
        client.publish("move","backward_no")
    elif msg=="k":
        client.publish("move","no_right")
    elif msg=="h":
        client.publish("move","no_left")
    elif msg=="i":
        client.publish("move","forward_right")
    elif msg=="o":
        client.publish("move","forward_left")
    elif msg=="p":
        client.publish("move","backward_right")
    elif msg=="l":
        client.publish("move","backward_left")
    elif msg=="m":
        client.publish("picture","*")