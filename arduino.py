#import mraa
def init_leds(*pines):
	return pines # copia la funcion pines
def off_pines(*pines):
	pass
class Display():
	def __init__(self,A,B,C,D,E,F,G):
		[self.A,self.B,self.C,self.D,self.E,self.F,self.G]= init_leds(A,B,C,D,E,F,G)
		self.numero = {0:self.cero,
							1:self.uno,
							2:self.dos,
							3:self.tres,
							4:self.cuatro,
							5:self.cinco,
							6:self.seis,
							7:self.siete,
							8:self.ocho,
							9:self.nueve,
							10:self.diez
		}
	def off(self):
		off_pines(self.A,self.B,self.C,self.D,self.E,self.F,self.G)
	def write(self,numero):#dibujar numero
		self.numero[numero]()
	def cero(self):
		print "cero"
	def uno(self):
		print "uno"
		#aqui tenes que hacer el numero uno en el display, solo que ahora no es A sino que self.A
	def dos(self):
		print "dos"
	def tres(self):
		print "tres"
	def cuatro(self):
		print "cuatro"
	def cinco(self):
		print "cinco"
	def seis(self):
		print "seis"
	def siete(self):
		print "siete"
	def ocho(self):
		print "ocho"
	def nueve(self):
		print	 "nueve"
	def diez(self):
		print "diez"
