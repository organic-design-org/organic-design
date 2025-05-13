from flask import Blueprint, render_template, url_for, request, session
from app import functions

div = Blueprint('div', __name__)

@div.route('/div', methods=['GET', 'POST'])
def divpage():
    formValues = functions.get_form_values()
    style = formValues['divStyle']
    if style in functions.style_map:
        functions.style_map[style](formValues)
    
    code = functions.show_code(formValues)
    return render_template('pages/div.html', title="Organic Design Divs", page="div", formValues=formValues, code=code)