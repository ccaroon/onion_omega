import time
import lvgl as lv
import fb
# from lv_colors import lv_colors

from lib.weather_station import WeatherStation

# TODO: move to a Class
def init_screen():
    lv.init()
    fb.init()

    disp_buf1 = lv.disp_buf_t()
    buf1_1 = bytearray(320*10)
    lv.disp_buf_init(disp_buf1, buf1_1, None, len(buf1_1)//4)

    disp_drv = lv.disp_drv_t()
    lv.disp_drv_init(disp_drv)
    disp_drv.buffer = disp_buf1
    disp_drv.flush_cb = fb.flush
    lv.disp_drv_register(disp_drv)

    scr = lv.obj()

    return scr
# -----------------------------------------------------------------------------
def new_gauge():
    # needle colors
    needle_colors=[
        lv.color_make(0x0, 0x0, 0xff),
        lv.color_make(0xff, 0x0, 0x0),
        lv.color_make(0x0, 0x0, 0x0)
    ]

    # create the gauge
    gauge = lv.gauge(lv.scr_act(), None)
    gauge.set_needle_count(3, needle_colors)
    gauge.set_size(200,200)
    gauge.set_range(0,110)
    gauge.set_scale(260, 12, 12)
    # gauge.set_critical_value(90)
    gauge.align(None,lv.ALIGN.CENTER,0,0)

    return gauge

def new_label(x,y):
    label = lv.label(lv.scr_act())

    label.set_recolor(True)
    label.align(lv.scr_act(), lv.ALIGN.CENTER, x, y)

    return label

def update_label(label, value, color="000000"):
    label.set_text("#%s %s#" % (color, value))

def update_gauge(gauge, data):
    gauge.set_value(0, data[0])
    gauge.set_value(1, data[2])
    gauge.set_value(2, data[1])

# -----------------------------------------------------------------------------
UPDATE_INTERVAL = 3 * 60

if __name__ == "__main__":
    station = WeatherStation()
    screen = init_screen()

    # Load the screen
    lv.scr_load(screen)

    gauge = new_gauge()
    low_label = new_label(-100,100)
    curr_label = new_label(0,100)
    high_label = new_label(100,100)
    when_label = new_label(-17,-110)

    last_update = 0
    while True:
        now = time.time()

        if now - last_update > UPDATE_INTERVAL:
            last_update = now
            temp_info = station.get_temp_info()

            print(temp_info)

            update_gauge(gauge, temp_info)

            update_label(low_label, temp_info[0], "0000ff")
            update_label(curr_label, temp_info[1], "000000")
            update_label(high_label, temp_info[2], "ff0000")

            update_label(when_label, time.strftime("%H:%M:%S"))












# EOF
