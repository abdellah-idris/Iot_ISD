import paho.mqtt.client as mqtt
import time
import os
from server.move import *
import Adafruit_PCA9685

SERVO_POSITION = [300, 300, 300, 300, 300]


pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)

#def init():
#    for i in range (11,16):
#        pwm.set_pwm(i, 0, SERVO_POSITION)
    
#init()


def on_message(client, userdata,message):
    global SERVO_POSITION
    print("received message:"+message.topic + " "+str(message.payload.decode("utf-8")))

    if message.topic == 'servo':
        msg = message.payload.decode("utf-8")
        direction = int(msg[-1])
        servo = int(msg[0:2])
        
        if direction == 0: 
            SERVO_POSITION[servo-11] = (SERVO_POSITION[servo-11] - 20) if SERVO_POSITION[servo-11] >= 120 else 100
        else:
            SERVO_POSITION[servo-11] = (SERVO_POSITION[servo-11] + 20) if SERVO_POSITION[servo-11] <= 480 else 500
                
        pwm.set_pwm(servo, 0, SERVO_POSITION[servo-11])
            
    if message.topic == 'move':
        direction = str(message.payload.decode("utf-8")).split('_')
        tmp(direction[0], direction[1])
 

    if message.topic == 'led':
        pass
        
    if message.topic == 'picture':
        os.system('raspistill -t 3000 -o image.jpg')
    
    if message.topic == 'shot':
        pass

mqttBroker="mqtt.eclipseprojects.io"
client=mqtt.Client("dola")
client.connect(mqttBroker)
client.loop_start()
client.subscribe("move")
client.subscribe("servo")
client.subscribe("led")
client.subscribe("picture")

client.on_message=on_message


client.loop_forever()
