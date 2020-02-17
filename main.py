import os, network
station = network.WLAN(network.STA_IF)
station.active(True)
if not station.isconnected():
    print('connecting to network...')
    station.connect("mithu-G", "Mithu@1977")
    while not station.isconnected():
        pass
print('network config:', station.ifconfig())

from server import start