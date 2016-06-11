import OmegaExpansion.pwmExp as pwm
import sys

status = pwm.driverInit()

if pwm.checkInit() == 0:
    print("PWM Init failed")
    exit

lr = float(sys.argv[1])
ud = float(sys.argv[2])

pwm.setFrequency(50)
pwm.setupDriver( 0, lr, 0)
pwm.setupDriver(15, ud, 0)
