from flask import Blueprint, render_template, url_for

div = Blueprint('div', __name__)

@div.route('/div', methods=['GET', 'POST'])
def divpage():
    return render_template('pages/div.html', title="Organic Design Divs", page="div")