import lvgl as lv
from lib.widgets.base import Base

class LED(Base):

    def __init__(self, x,y, main_color, grad_color = None):
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

        self.__widget = led

    def color(self, main_color, grad_color=None):
        style = self.__widget.get_style(lv.led.STYLE.MAIN)
        style.body.main_color = main_color
        style.body.grad_color = grad_color or main_color

        self.__widget.set_style(lv.led.STYLE.MAIN, style)

    def on(self):
        self.__widget.on()

    def off(self):
        self.__widget.off()

    def brightness(self, value):
        self.__widget.set_bright(value)
