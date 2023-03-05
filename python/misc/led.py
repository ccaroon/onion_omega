import omega_gpio as gpio
import time

PIN = 7
WAIT = 1
gpio.initpin(PIN,'out')
gpio.setoutput(PIN,0)

while True:
    gpio.setoutput(PIN,1)
    time.sleep(WAIT)

    gpio.setoutput(PIN,0)
    time.sleep(WAIT)

