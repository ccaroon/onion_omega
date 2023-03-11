import lvgl as lv

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
