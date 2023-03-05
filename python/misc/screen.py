import OmegaExpansion.oledExp as oled

oled.driverInit()
oled.setDisplayPower(1)
oled.setDisplayMode(0)
oled.clear()

oled.setCursor(0, 0)
oled.write("Hello")
oled.setCursor(2,0)
oled.write("World!")
