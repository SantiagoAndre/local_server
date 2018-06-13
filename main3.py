import SimpleHTTPServer
import SocketServer
import cgi
import arduino
#variables globales
PORT = 8001
votos_persona ={"W":1,"X":2,"Y":3,"Z":4}
LEDS= {"W":arduino.init_led(6),"X":arduino.init_led(65),"Y":arduino.init_led(4),"Z":arduino.init_led(3)}
DISPLAY = arduino.Display(13,12,11,10,9,8,7)#pines del display
class MyHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
	def do_GET(self):
		if self.path == '/':
			self.path = '/templates/design.html'
			return SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)

	def do_POST(self):
		total_votos = 0
		form = cgi.FieldStorage(
            fp=self.rfile,
            headers=self.headers,
            environ={'REQUEST_METHOD':'POST',
                     'CONTENT_TYPE':self.headers['Content-Type'],
                     })
		if "cbxW" in form:
			LEDS["W"].write(True)
			total_votos += votos_persona["W"]
		else:
			LEDS["W"].write(False)
		if "cbxX" in form:
			LEDS["X"].write(True)
			total_votos += votos_persona["X"]
		else:
			LEDS["X"].write(False)

		if "cbxY" in form:
			LEDS["Y"].write(True)
			total_votos += votos_persona["Y"]
		else:
			LEDS["Y"].write(False)
		if "cbxZ" in form:
			LEDS["Z"].write(True)
			total_votos += votos_persona["Z"]
		else:
			LEDS["Z"].write(False)
		DISPLAY.write(total_votos)
		return self.do_GET()

try:
	Handler = MyHandler
	httpd = SocketServer.TCPServer(("", PORT), Handler)
	print "serving at port", PORT
	httpd.serve_forever()
except KeyboardInterrupt:
	for persona in LEDS.keys():
		arduino.off_pin(LEDS[persona])
	Display.off()
	print "adios"
