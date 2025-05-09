from flask import Blueprint, render_template
from app.forms import BusquedaForm

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    form = BusquedaForm()
    return render_template('index.html', form=form)
