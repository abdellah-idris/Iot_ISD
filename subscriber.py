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
mqttBroker="192.168.0.102"
client=mqtt.Client("Dolhamid")
client.connect(mqttBroker)
client.loop_start()
IR_RECEIVER=15
GPIO.setup(IR_RECEIVER,GPIO.IN)
GPIO.add_event_detect(IR_RECEIVER,GPIO.FALLING,callback=lambda x: InfraLib.getSignal(IR_RECEIVER,client),bouncetime=100)
client.subscribe("move"+tankID)
client.subscribe("servo"+tankID)
client.subscribe("led"+tankID)
client.subscribe("picture"+tankID)
client.subscribe("Dolhamid")
client.publish("init","INIT "+tankID)
client.publish("Dolhamid","Dolhamid "+tankID)
client.on_message=on_message


client.loop_forever()
