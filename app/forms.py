from flask_wtf import FlaskForm
from wtforms import StringField, DateField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class BusquedaForm(FlaskForm):
    origen = StringField('Origen', validators=[DataRequired()])
    destino = StringField('Destino', validators=[DataRequired()])
    fecha_salida = DateField('Fecha Salida', format='%Y-%m-%d')
    pasajeros = IntegerField('Pasajeros', default=1)
    buscar = SubmitField('Buscar Viajes')
