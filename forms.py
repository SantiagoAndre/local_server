from wtforms import Form, BooleanField
from wtforms import  BooleanField,SubmitField
from wtforms.validators import Required, Length, DataRequired

class FormVotacion(Form):
	votoW = BooleanField('vota W',default=False)
	votoX = BooleanField('vota X',default=False)
	votoY = BooleanField('vota Y',default=False)
	votoZ = BooleanField('vota Z',default=False)
	submit = SubmitField('Enviar')
