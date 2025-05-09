from flask import Blueprint, render_template, url_for

nav = Blueprint('nav', __name__)

@nav.route('/nav', methods=['GET', 'POST'])
def navpage():
    return render_template('pages/nav.html', title="Organic Design Navs", page="nav")