from .microWebSrv import MicroWebSrv

def _getDHT():
	data = ''
	try:
		import dht
		from machine import Pin
		sensor_pin = Pin(14, Pin.IN, Pin.PULL_UP)
		sensor = dht.DHT11(sensor_pin)
		sensor.measure()
		t, h = sensor.temperature(), sensor.humidity()
		data = 'Temp : {0:.1f} &deg;C | RH : {1:.1f} %'.format(t, h)
	except:
		data = 'Attempting to read sensor ...'
	finally:
		return data

# ----------------------------------------------------------------------------

@MicroWebSrv.route('/dht')
def _httpHandlerDHTGet(httpClient, httpResponse):
	data = _getDHT()
	httpResponse.WriteResponseOk(
		headers = ({'Cache-Control': 'no-cache'}),
		contentType = 'text/event-stream',
		contentCharset = 'UTF-8',
		content = 'data: {0}\n\n'.format(data))

# ----------------------------------------------------------------------------

def _acceptWebSocketCallback(webSocket, httpClient) :
	print("WS ACCEPT")
	webSocket.RecvTextCallback   = _recvTextCallback
	webSocket.RecvBinaryCallback = _recvBinaryCallback
	webSocket.ClosedCallback 	 = _closedCallback

def _recvTextCallback(webSocket, msg) :
	print("WS RECV TEXT : %s" % msg)
	webSocket.SendText("Reply for %s" % msg)

def _recvBinaryCallback(webSocket, data) :
	print("WS RECV DATA : %s" % data)

def _closedCallback(webSocket) :
	print("WS CLOSED")

# ----------------------------------------------------------------------------

srv = MicroWebSrv(webPath='server/www/')
srv.MaxWebSocketRecvLen     = 256
srv.WebSocketThreaded		= False
srv.AcceptWebSocketCallback = _acceptWebSocketCallback

# ----------------------------------------------------------------------------