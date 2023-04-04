import paho.mqtt.client as mqtt
import time
import os
from server.move import *
import Adafruit_PCA9685
import  uuid
import InfraLib

SERVO_POSITION = [300, 300, 300, 300, 300]
tankID  =  uuid.getnode()

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)

#def init():
#    for i in range (11,16):
#        pwm.set_pwm(i, 0, SERVO_POSITION)
    
#init()


def on_message(client, userdata,message):
    global SERVO_POSITION
    if message.topic == 'servo'+tankID:
        msg = message.payload.decode("utf-8")
        direction = int(msg[-1])
        servo = int(msg[0:2])
        
        if direction == 0: 
            SERVO_POSITION[servo-11] = (SERVO_POSITION[servo-11] - 20) if SERVO_POSITION[servo-11] >= 120 else 100
        else:
            SERVO_POSITION[servo-11] = (SERVO_POSITION[servo-11] + 20) if SERVO_POSITION[servo-11] <= 480 else 500
                
        pwm.set_pwm(servo, 0, SERVO_POSITION[servo-11])
            
    if message.topic == 'move'+tankID:
        direction = str(message.payload.decode("utf-8")).split('_')
        tmp(direction[0], direction[1])
 

    if message.topic == 'led'+tankID:
        pass
        
    if message.topic == 'picture'+tankID:
        os.system('raspistill -t 3000 -o image.jpg')
    
    if message.topic == 'shot'+tankID:
        InfraLib.IRBlast(tankID,"LASER")
    
    liste_msg=message.payload.decode("utf-8").split()
    if liste_msg[0]=="TEAM":
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
client=mqtt.Client("Dolhamid")
client.connect(mqttBroker)
client.loop_start()
IR_RECEIVER=15
GPIO.setmode(GPIO.BOARD)
GPIO.setup(IR_RECEIVER,GPIO.IN)
GPIO.add_event_detect(IR_RECEIVER,GPIO.FALLING,callback=lambda x: InfraLib.getSignal(IR_RECEIVER,client),bouncetime=100)
client.subscribe("move"+str(tankID))
client.subscribe("servo"+str(tankID))
client.subscribe("led"+str(tankID))
client.subscribe("picture"+str(tankID))
client.publish("init","INIT "+str(tankID))
client.subscribe("tanks/"+str(tankID)+"/init")
client.subscribe("tanks/"+str(tankID)+"/shots/in")
client.subscribe("tanks/"+str(tankID)+"/shots/out")
client.subscribe("tanks/"+str(tankID)+"/qr_code")
client.subscribe("tanks/"+str(tankID)+"/flag")
client.on_message=on_message


while True:
    pass