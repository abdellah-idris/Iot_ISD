import Adafruit_PCA9685 # Import the library used to communicate with PCA9685  

pwm = Adafruit_PCA9685.PCA9685()    # Instantiate the object used to control the PWM  

pwm.set_pwm_freq(50)    # Set the frequency of the PWM signal  
   
def move_brain(channel, angle):
    pwm.set_pwm(channel, 0, angle)
