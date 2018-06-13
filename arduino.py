import mraa
def init_led(pin):
	LED = mraa.Gpio(pin)
	LED.dir(mraa.DIR_OUT)
	return LED
def init_pul(pin):
	PUL = mraa.Gpio(pin)
	PUL.dir(mraa.DIR_IN)
	return PUL
def off_pin(pin):
	pin.write(False)
def init_leds(*pines):
	return [init_led(pin) for pin in pines] # lita intencional
def init_puls(*pines):
	return [init_pul(pin) for pin in pines] # lita intencional
def off_pines(*pines):
	for pin in pines:
		off_pin(pin)
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
		self.A.write(0)
		self.B.write(0)
		self.C.write(0)
		self.D.write(0)
		self.E.write(0)
		self.F.write(0)
		self.G.write(0)
	def uno(self):
		print "uno"
		self.A.write(0)
		self.B.write(1)
		self.C.write(1)
		self.D.write(0)
		self.E.write(0)
		self.F.write(0)
		self.G.write(0)
	def dos(self):
		print "dos"
		self.A.write(1)
		self.B.write(1)
		self.C.write(0)
		self.D.write(1)
		self.E.write(1)
		self.F.write(0)
		self.G.write(1)
	def tres(self):
		print "tres"
		self.A.write(1)
		self.B.write(1)
		self.C.write(1)
		self.D.write(1)
		self.E.write(0)
		self.F.write(0)
		self.G.write(1)
	def cuatro(self):
		print "cuatro"
		self.A.write(0)
		self.B.write(1)
		self.C.write(1)
		self.D.write(0)
		self.E.write(0)
		self.F.write(1)
		self.G.write(1)
	def cinco(self):
		print "cinco"
		self.A.write(1)
		self.B.write(0)
		self.C.write(1)
		self.D.write(1)
		self.E.write(0)
		self.F.write(1)
		self.G.write(1)
	def seis(self):
		print "seis"
		self.A.write(1)
		self.B.write(0)
		self.C.write(1)
		self.D.write(1)
		self.E.write(1)
		self.F.write(1)
		self.G.write(1)
	def siete(self):
		print "siete"
		self.A.write(1)
		self.B.write(1)
		self.C.write(1)
		self.D.write(0)
		self.E.write(0)
		self.F.write(0)
		self.G.write(0)
	def ocho(self):
		print "ocho"
		self.A.write(1)
		self.B.write(1)
		self.C.write(1)
		self.D.write(1)
		self.E.write(1)
		self.F.write(1)
		self.G.write(1)
	def nueve(self):
		print	 "nueve"
		self.A.write(1)
		self.B.write(1)
		self.C.write(1)
		self.D.write(1)
		self.E.write(0)
		self.F.write(1)
		self.G.write(1)
	def diez(self):
		print "diez"
		self.A.write(1)
		self.B.write(1)
		self.C.write(1)
		self.D.write(1)
		self.E.write(1)
		self.F.write(1)
		self.G.write(0)
