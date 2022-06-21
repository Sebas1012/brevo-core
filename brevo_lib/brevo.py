import network
from machine import Pin
from time import sleep

def wifi_connect(ssid, password):
  try:
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect(ssid, password)

    sleep(3)

    info = sta_if.ifconfig()
    info = {'Local IP':info[0],'Mask': info[1], 'Gateway': info[2]}
    
    pin = Pin(2, Pin.OUT)

    print(info)
    
    while True:
      pin.value(1)
      sleep(1)
      pin.value(0)
      sleep(1)
        
  except:
    print("Sorry, something went wrong")



