import lvgl as lv

from lib.widgets.base import Base

class Bar(Base):
    def __init__(self, w, h, x, y, **kwargs):
        anim_time = kwargs.get('anim_time', 500)

        bar = lv.bar(lv.scr_act())
        bar.set_size(w, h)
        bar.align(None, lv.ALIGN.CENTER, x, y)
        bar.set_anim_time(anim_time)

        self.__widget = bar

    @property
    def value(self):
        self.__widget.get_value()

    @value.setter
    def value(self, new_value):
        self.__widget.set_value(new_value, lv.ANIM.ON)
