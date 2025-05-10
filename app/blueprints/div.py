from flask import Blueprint, render_template, url_for, request, session
from app import functions

div = Blueprint('div', __name__)

@div.route('/div', methods=['GET', 'POST'])
def divpage():
    if request.method == 'POST':
        formValues = {}
        xs = 20 
        ys = 20
        width = request.form.get('divWidth')
        height = request.form.get('divHeight')
        xe = width + xs
        ye = height + ys
        divHeight = (height + 20) + 'px'
        divWidth = (width + 20) + 'px'
        

    return render_template('pages/div.html', title="Organic Design Divs", page="div")