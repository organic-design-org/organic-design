from flask import Blueprint, render_template, url_for, request, session
from app import functions

div = Blueprint('div', __name__)

@div.route('/div', methods=['GET', 'POST'])
def divpage():
    formValues = functions.get_form_values()
    if formValues['divStyle'] == 'rectJag':
        functions.rectJag(formValues)
    elif formValues['divStyle'] == 'rectCurve':
        functions.rectCurve(formValues)
    elif formValues['divStyle'] == 'circ':
        functions.circ(formValues)
    elif formValues['divStyle'] == 'circJag':
        functions.circJag(formValues)
    
    if request.method == 'POST':
        functions.msg_modal(request.form)
    
    form=request.form

    code = functions.show_code(formValues)
    return render_template('pages/div.html', title="Organic Design Divs", page="div", formValues=formValues, code=code, form=form)