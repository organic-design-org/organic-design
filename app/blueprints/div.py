from flask import Blueprint, render_template, url_for, request, session
from app import functions

div = Blueprint('div', __name__)

@div.route('/div', methods=['GET', 'POST'])
def divpage():
    formValues = functions.get_form_values()
    return render_template('pages/div.html', title="Organic Design Divs", page="div", formValues=formValues)