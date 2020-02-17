import os, network
from server.start import srv

print("=============================")
print("Connecting to the network ...")
station = network.WLAN(network.STA_IF)
station.active(True)
if not station.isconnected():
    station.connect("mithu-G", "Mithu@1977")
    while not station.isconnected():
        pass
stationConfig =  station.ifconfig()
print('Connected to the network. Network Configuration:', stationConfig)
print("=============================")
print("Starting server ...")
srv.Start()