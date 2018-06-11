from flask import Flask
from flask import render_template
from flask import request

from forms import FormVotacion

app = Flask(__name__)
votos_persona ={"W":1,"X":2,"Y":3,"Z":4}

@app.route('/', methods = ['GET', 'POST'])
def index():
	boton = request.args.get("submit",None)
	form_votacion = FormVotacion(request.form)
	if boton == "Enviar":
		total_votos = 0
		votoW = request.args.get("votoW",None)
		votoX = request.args.get("votoX",None)
		votoY = request.args.get("votoY",None)
		votoZ = request.args.get("votoZ",None)
		if votoW == "y":
			#LED["W"].write(True)
			total_votos += votos_persona["W"]
			form_votacion.votoW.data = True
		if votoX == "y":
			total_votos += votos_persona["X"]
			form_votacion.votoX.data = True
		if votoY == "y":
			total_votos += votos_persona["Y"]
			form_votacion.votoY.data = True
		if votoZ == "y":
			total_votos += votos_persona["Z"]
			form_votacion.votoZ.data = True
		print "Los votos totales son: ",total_votos
	return render_template('index.html', form = form_votacion)

if __name__ == '__main__':
    app.run(debug = True)

