import onionGpio as gpio
import time

WAIT = 0.5

led = gpio.OnionGpio(7)
led.setOutputDirection(0)

while True:

    led.setValue(1)
    time.sleep(WAIT)

    led.setValue(0)
    time.sleep(WAIT)
