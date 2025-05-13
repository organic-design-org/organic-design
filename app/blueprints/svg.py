from flask import Blueprint, render_template, url_for, request, session
from app import functions

svg = Blueprint('svg', __name__)

@svg.route('/svg', methods=['GET', 'POST'])
def svgpage():
    formValues = functions.get_form_values()
    style = formValues['divStyle']
    if style in functions.style_map:
        functions.style_map[style](formValues)
    
    code = functions.show_code(formValues)
    return render_template('pages/svg.html', title="Organic Design Divs", page="svg", formValues=formValues, code=code)