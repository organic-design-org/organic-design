from flask import Blueprint, render_template, url_for, request, session
from app import functions

div = Blueprint('div', __name__)

@div.route('/div', methods=['GET', 'POST'])
def divpage():
    style_map = {
        "rectJag": functions.rectJag,
        # "rectCurve": functions.rectCurve,
        # "circ": functions.circ,
        # "circJag": functions.circJag,
        "testing": lambda fv: fv  # no-op or a dedicated function
    }

    formValues = functions.get_form_values()
    style = formValues['divStyle']
    if style in style_map:
        style_map[style](formValues)

    # if request.method == 'POST':
    #     functions.msg_modal(request.form)
    
    form=request.form

    code = functions.show_code(formValues)
    return render_template('pages/div.html', title="Organic Design Divs", page="div", formValues=formValues, code=code, form=form)