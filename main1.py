from flask import Flask
from flask import render_template
from flask import request

from forms import FormVotacion

app = Flask(__name__)
votos_persona ={"W":1,"X":2,"Y":3,"Z":4}

@app.route('/', methods = ['GET', 'POST'])
def index():
	form_votacion = FormVotacion(request.form)
	if request.method == "POST":
		total_votos = 0
		print request.form
		if "cbxW" in request.form:
			#LED["W"].write(True)
			total_votos += votos_persona["W"]
			#form_votacion.votoW.data = True
		if "cbxX" in request.form:
			total_votos += votos_persona["X"]
			#form_votacion.votoX.data = True
		if "cbxY" in request.form:
			total_votos += votos_persona["Y"]
			#form_votacion.votoY.data = True
		if "cbxZ" in request.form:
			total_votos += votos_persona["Z"]
			#form_votacion.votoZ.data = True
		print "Los votos totales son: ",total_votos
	return render_template('design.html', form = form_votacion)
def submit():
	print "submit"
if __name__ == '__main__':
    app.run(debug = True)

