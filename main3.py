import SimpleHTTPServer
import SocketServer
import cgi
# tenes que crear otro archivo arduino.py en donde tengas todas las funciones que ya habiamos hecho
import arduino
#variables globales
PORT = 8002
personas = {"W","X","Y","Z"}
votos_persona ={"W":1,"X":2,"Y":3,"Z":4}
LEDS = arduino.init_leds(13,14,15,16)#13,14,15,16 pines de los leds
LEDS =  dict(zip(personas,LEDS))
DISPLAY = arduino.Display(0,1,2,3,4,5,6)#pines del display
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
			#LED["W"].write(True)
			total_votos += votos_persona["W"]
		else:
			pass ##bora el pass y descomenta la sieguiente linea
			#LED["W"].write(False)
		if "cbxX" in form:
			#LED["X"].write(True)
			total_votos += votos_persona["X"]
		else:
			pass ##bora el pass y descomenta la sieguiente linea
			#LED["X"].write(False)

		if "cbxY" in form:
			#LED["Y"].write(True)
			total_votos += votos_persona["Y"]
		else:
			pass ##bora el pass y descomenta la sieguiente linea
			#LED["Y"].write(False)
		if "cbxZ" in form:
			#LED["Z"].write(True)
			total_votos += votos_persona["Z"]
		else:
			pass ##bora el pass y descomenta la sieguiente linea
			#LED["Z"].write(False)
		DISPLAY.write(total_votos)
		return self.do_GET()

try:
	Handler = MyHandler
	httpd = SocketServer.TCPServer(("", PORT), Handler)
	print "serving at port", PORT
	httpd.serve_forever()
except KeyboardInterrupt:
	pines = [LEDS[persona] for persona in LEDS.keys()]
	arduino.off_pines(pines)
	print "adios"
