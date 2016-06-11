import omega_gpio as gpio
import time

while True:

    gpio.initpin(13,'out')
    gpio.setoutput(13,1)
    time.sleep(5)
    gpio.setoutput(13,0)

