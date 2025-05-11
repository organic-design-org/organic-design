from flask import Blueprint, render_template, url_for, request, session
from app import functions

div = Blueprint('div', __name__)

@div.route('/div', methods=['GET', 'POST'])
def divpage():
    # Default Values
    divWidth = '298px'
    divHeight = '486px'
    containerHeight = '536px'
    if request.method == 'POST':
        formValues = {}
        xs = 20 
        ys = 20
        width = request.form.get('divWidth')
        height = request.form.get('divHeight')
        xe = int(width) + xs
        ye = int(height) + ys
        divHeightInt = (int(height) + 20) 
        divHeight = str(divHeightInt) + 'px'
        divWidthInt = (int(width) + 20) 
        divWidth = str(divWidthInt) + 'px'
        containerHeight = str(int(height) + 70) + 'px'
        # functions.msg_modal(divHeight)

    return render_template('pages/div.html', title="Organic Design Divs", page="div", divHeight=divHeight, divWidth=divWidth, containerHeight=containerHeight)