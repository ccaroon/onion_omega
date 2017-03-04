# Sensor Stuff

## Dallas Temp (1-Wire)

### Omega 1
* echo "w1-gpio-custom bus0=0,XX,0" > /etc/modules.d/55-w1-gpio-custom
    - XX = GPIO Pin Number

### Omega 2
* `insmod w1-gpio-custom bus0=0,XX,0`
    - XX = GPIO Pin Number
* See files in: `/sys/devices/w1_bus_master1`
    - cat /sys/devices/w1_bus_master1/<SENSOR_UID>/w1_slave
