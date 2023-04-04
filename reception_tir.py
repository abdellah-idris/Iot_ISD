import Infralib
import RPi.GPIO as GPIO

IR_RECEIVER = 15

GPIO.setup(IR_RECEIVER, GPIO.IN)

GPIO.add_event_detect(IR_RECEIVER, GPIO.FAILLING, callback=lambda x : InfraLib.getSignal(IR_RECEIVER, client), bouncetime=100)
