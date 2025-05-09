from flask import Blueprint, render_template, url_for

home = Blueprint('home', __name__)

@home.route('/')
@home.route('/home', methods=['GET', 'POST'])
def homepage():
    return render_template('pages/home.html', title="Organic Design Tutorial", page="home")