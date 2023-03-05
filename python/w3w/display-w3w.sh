echo "Reading GPS..."
ubus call gps info | python3 w3w_addr.py > output.txt
oled-exp -c
oled-exp write $(cat output.txt)
