import SimpleHTTPServer
import SocketServer
import cgi
PORT = 8000
votos_persona ={"W":1,"X":2,"Y":3,"Z":4}
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
		for i in form.keys():
			print i
			print form[i].value
		if "cbxW" in form:
			#LED["W"].write(True)
			total_votos += votos_persona["W"]
			#form_votacion.votoW.data = True
		if "cbxX" in form:
			total_votos += votos_persona["X"]
			#form_votacion.votoX.data = True
		if "cbxY" in form:
			total_votos += votos_persona["Y"]
			#form_votacion.votoY.data = True
		if "cbxZ" in form:
			total_votos += votos_persona["Z"]
			#form_votacion.votoZ.data = True
		print "el total de votos es: ",total_votos
		return self.do_GET()


Handler = MyHandler
httpd = SocketServer.TCPServer(("", PORT), Handler)
print "serving at port", PORT
httpd.serve_forever()

