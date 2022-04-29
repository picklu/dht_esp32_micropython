import os, network
import credentials as creds
from server.start import srv

print("=============================")
print("Connecting to the network ...")
station = network.WLAN(network.STA_IF)
station.active(True)
if not station.isconnected():
    station.connect(creds.ssid, creds.password)
    while not station.isconnected():
        pass
stationConfig =  station.ifconfig()
print('Connected to the network. Network Configuration:', stationConfig)
print("=============================")
print("Starting server ...")
srv.Start()