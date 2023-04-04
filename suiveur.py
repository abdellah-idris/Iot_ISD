import uuid
import RPi.GPIO as GPIO

tankID = uuid.getnode()

LINE_PIN_MIDDLE = 36

GPIO.setup(LINE_PIN_MIDDLE, GPIO.IN)

GPIO.add_event_detect(LINE_PIN_MIDDLE, GPIO.BOTH, callback=enterFlagArea, bouncetime=100)

def enterFlagArea(channel1):
	if GPIO.input(LINE_PIN_MIDLLE) == GPIO.LOW:
		client.publish('tanks/'+hex(tankID)+'/flag', 'ENTER_FLAG_AREA')
	else :
		client.publish('tanks/'+hex(tankID)+'/flag', 'EXIT_FLAG_AREA')
