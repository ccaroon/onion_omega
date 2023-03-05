# Omega2 Dash
https://onion.io/omega2-dash-guide/


## MicroPython
1. `opkg update`
2. `opkg install lv_micropython`
3. `vi /etc/opkg/distfeeds.conf`
   - Uncomment "openwrt_packages" line
4. `okpg update`
5. `opkg install micropython-lib --nodeps`

### Graphics
* https://github.com/OnionIoT/lv_micropython/tree/master/examples/onion
* https://docs.lvgl.io/7.11/intro/index.html
* https://github.com/uraich/lv_mpy_examples_v8
