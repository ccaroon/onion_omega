#!/usr/bin/micropython
import time
import lvgl as lv

from lib.weather_station import WeatherStation
from lib.screen import Screen
from lib.widgets.bar import Bar
from lib.widgets.led import LED
from lib.widgets.gauge import Gauge
from lib.widgets.label import Label

import lib.utils as utils
# -----------------------------------------------------------------------------
UPDATE_INTERVAL = 1 * 60

if __name__ == "__main__":
    # **Must** happen __before__ any widgets can be created
    Screen.init()

    station = WeatherStation()

    gauge = Gauge(
        200, 200, 0, 0,
        count = 3,
        colors = [
            lv.color_make(0x0, 0x0, 0xff), # low
            lv.color_make(0xff, 0x0, 0x0), # high
            lv.color_make(0x0, 0x0, 0x0)   # current
        ]
    )

    humidity = Bar(20, 175, 130, 0)
    low_label = Label(-100,100)
    curr_label = Label(0,100)
    high_label = Label(100,100)
    when_label = Label(-17,-110)

    led = LED(0, 0, lv.color_make(0x0, 0x0, 0x0))
    led.on()

    last_update = 0
    while True:
        now = time.time()

        if now - last_update > UPDATE_INTERVAL:
            last_update = now

            try:
                temp_info = station.get_temp_info()
                humd = station.get_humidity()
                print("Low [%d] | Current [%d] | High [%d] | Humidity [%d%%]" % (
                    temp_info[0],
                    temp_info[2],
                    temp_info[1],
                    humd
                ))

                gauge.update(temp_info)

                humidity.value = humd

                led.color(utils.temp_to_color(temp_info[1]))

                low_label.text(temp_info[0], "0000ff")
                high_label.text(temp_info[1], "ff0000")
                curr_label.text(temp_info[2], "000000")
                when_label.text(time.strftime("%H:%M:%S"))
            except Exception as err:
                msg = str(err)
                print(msg)
                when_label.text(msg, "ff0000")






# EOF
