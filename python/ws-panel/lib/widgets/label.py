import lvgl as lv

from lib.widgets.base import Base

class Label(Base):
    def __init__(self, x,y):
        label = lv.label(lv.scr_act())

        label.set_recolor(True)
        label.align(lv.scr_act(), lv.ALIGN.CENTER, x, y)

        self.__widget = label

    def text(self, new_text, color="000000"):
        self.__widget.set_text("#%s %s#" % (color, new_text))
