import lvgl as lv

def new_led(x,y, main_color, grad_color = None):
    # Create a style for the LED
    style_led = lv.style_t()
    lv.style_copy(style_led, lv.style_pretty_color)
    style_led.body.radius = 400 # large enough to draw a circle
    style_led.body.main_color = main_color
    style_led.body.grad_color = grad_color or main_color
    style_led.body.border.color = lv.color_make(0x0, 0x0, 0x0)
    style_led.body.border.width = 2
    style_led.body.border.opa = lv.OPA._30
    # style_led.body.shadow.color = lv.color_make(0x0, 0x0, 0x0)
    # style_led.body.shadow.width = 5

    # Create a LED
    led  = lv.led(lv.scr_act())
    led.set_style(lv.led.STYLE.MAIN, style_led)
    led.align(None, lv.ALIGN.CENTER, x, y)
    led.off()
    # led.set_bright(0)

    return led

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

def new_bar(w, h, x, y, **kwargs):
    anim_time = kwargs.get('anim_time', 500)

    bar = lv.bar(lv.scr_act())
    bar.set_size(w, h)
    bar.align(None, lv.ALIGN.CENTER, x, y)
    bar.set_anim_time(anim_time)

    return bar
