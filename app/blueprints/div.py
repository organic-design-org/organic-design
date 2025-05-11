from flask import Blueprint, render_template, url_for, request, session
from app import functions

div = Blueprint('div', __name__)

@div.route('/div', methods=['GET', 'POST'])
def divpage():
    if request.method == 'POST':
        if 'testing' in request.form:
            functions.msg_modal('Testing')
        formValues = functions.get_form_values()
        
        xs = 20 
        ys = 20

        xe = int(formValues['divWidth']) + xs
        ye = int(formValues['divHeight']) + ys
        # divHeightInt = (int(height) + 20) 
        # divHeight = str(divHeightInt) + 'px'
        # divWidthInt = (int(width) + 20) 
        # divWidth = str(divWidthInt) + 'px'
        # containerHeight = str(int(height) + 70) + 'px'

        functions.msg_modal(request.form)
    else:
        # Default Values
        formValues = {}
        formValues['divWidth'] = 410
        formValues['divHeight'] = 410
        formValues['containerHeight'] = 480

    return render_template('pages/div.html', title="Organic Design Divs", page="div", formValues=formValues)