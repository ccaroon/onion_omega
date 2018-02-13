import onionGpio as gpio
import time

##############################################
# illuminate() - button code - DOES NOT WORK
##############################################

WAIT = 0.5

led = gpio.OnionGpio(1)
led.setOutputDirection(0)

button = gpio.OnionGpio(0)
button.setInputDirection()

def illuminate():
    if button.getValue() == 0:
        print "Down"
    else:
        print "Up"

    time.sleep(0.1)

def blink():
    led.setValue(1)
    time.sleep(WAIT)

    led.setValue(0)
    time.sleep(WAIT)

while True:
    # blink()
    illuminate()
