#!/usr/bin/micropython
import time
import lvgl as lv

from lib.weather_station import WeatherStation
from lib.screen import Screen
import lib.widgets as widgets
# -----------------------------------------------------------------------------
def update_bar(bar, value):
    bar.set_value(value, lv.ANIM.ON)

def update_label(label, value, color="000000"):
    label.set_text("#%s %s#" % (color, value))

def update_led_color(led, main_color, grad_color=None):
    style = led.get_style(lv.led.STYLE.MAIN)
    style.body.main_color = main_color
    style.body.grad_color = grad_color or main_color

def update_gauge(gauge, data):
    gauge.set_value(0, data[0])
    gauge.set_value(1, data[2])
    gauge.set_value(2, data[1])

def temp_to_color(temp):
    color = lv.color_make(0xff, 0xff, 0xff)

    if temp <= 25:
        # white
        color = lv.color_make(0xff, 0xff, 0xff)
    elif temp > 25 and temp <= 32:
        # bluish/white
        color = lv.color_make(0xe4,0xf0,0xfb)
    elif temp > 32 and temp <= 55:
        # blue
        color = lv.color_make(0x04,0x7f,0xfb)
    elif temp > 55 and temp <= 64:
        # cyan
        color = lv.color_make(0x04,0xfb,0xe8)
    elif temp > 64 and temp <= 75:
        # green
        color = lv.color_make(0x33,0xe1,0x08)
    elif temp > 75 and temp <= 85:
        # yellow
        color = lv.color_make(0xf9,0xf5,0x04)
    elif temp > 85 and temp <= 95:
        # orange
        color = lv.color_make(0xf9,0x73,0x04)
    else:
        # red
        color = lv.color_make(0xff,0x00,0x00)

    return color

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
UPDATE_INTERVAL = 3 * 60

if __name__ == "__main__":
    Screen.init()
    station = WeatherStation()

    gauge = widgets.new_gauge()
    humidity = widgets.new_bar(30,200,130,0)
    low_label =  widgets.new_label(-100,100)
    curr_label = widgets.new_label(0,100)
    high_label = widgets.new_label(100,100)
    when_label = widgets.new_label(-17,-110)

    led = widgets.new_led(0,0, lv.color_make(0,0,0))
    led.on()

    last_update = 0
    while True:
        now = time.time()

        if now - last_update > UPDATE_INTERVAL:
            last_update = now
            temp_info = station.get_temp_info()
            humd = station.get_humidity()

            print(temp_info, humd)

            update_gauge(gauge, temp_info)
            update_bar(humidity, humd)

            update_led_color(led, temp_to_color(temp_info[1]))

            update_label(low_label, temp_info[0], "0000ff")
            update_label(curr_label, temp_info[1], "000000")
            update_label(high_label, temp_info[2], "ff0000")

            update_label(when_label, time.strftime("%H:%M:%S"))












# EOF
