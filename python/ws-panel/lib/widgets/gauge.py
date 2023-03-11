import lvgl as lv
from lib.widgets.base import Base

class Gauge(Base):
    def __init__(self, w, h, x, y, **kwargs):
        needle_count = kwargs.get('count', 1)
        needle_colors = kwargs.get('colors', [lv.color_make(0x0,0x0,0x0)])

        gauge = lv.gauge(lv.scr_act(), None)
        gauge.set_needle_count(needle_count, needle_colors)
        gauge.set_size(w, h)
        gauge.set_range(0,110)
        gauge.set_scale(260, 12, 12)
        gauge.align(None,lv.ALIGN.CENTER, x, y)

        self.__widget = gauge

    def update(self, values):
        for idx, value in enumerate(values):
            self.__widget.set_value(idx, value)
            self.__widget.set_value(idx, value)
            self.__widget.set_value(idx, value)
