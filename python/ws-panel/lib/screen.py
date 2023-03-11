import lvgl as lv
import fb

class Screen:

    __SCREEN_OBJ = None

    @classmethod
    def init(cls):
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

        cls.__SCREEN_OBJ = lv.obj()

        lv.scr_load(cls.__SCREEN_OBJ)
