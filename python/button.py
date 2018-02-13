import omega_gpio as gpio
import time

#########################
# DOES NOT WORK
#########################

LED_PIN = 7
gpio.initpin(LED_PIN,'out')
gpio.setoutput(LED_PIN,0)

BUTTON_PIN = 9
gpio.initpin(BUTTON_PIN,'in')

while True:

    if gpio.readinput(BUTTON_PIN):
        print "BUTTON PRESSED"
        gpio.setoutput(LED_PIN,1)
    else:
        gpio.setoutput(LED_PIN,0)

