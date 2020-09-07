from models import Country, Plane
from __init__ import app, db
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import SelectField

@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.route('/compare-planes')
def compare_planes():
    planes = Plane.query.all()
    countries = Country.query.all()
    return render_template('compare_planes.html', title='Compare planes', planes=planes, countries=countries)

@app.route('/compare-tanks')
def compare_tanks():
    return render_template('compare_tanks.html', title='Compare tanks')

@app.route('/compare-helicopters')
def compare_helicopters():
    return render_template('compare_helicopters.html', title='Compare helicopters')

@app.route('/compare-fleet')
def compare_fleet():
    return render_template('compare_fleet.html', title='Compare fleet')

@app.route('/planes')
def planes():
    return render_template('planes.html', title='Planes')

@app.route('/tanks')
def tanks():
    return render_template('tanks.html', title='Tanks')

@app.route('/helicopters')
def helicopters():
    return render_template('helicopters.html', title='Helicopters')

@app.route('/fleet')
def fleet():
    return render_template('fleet.html', title='Fleet')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('index.html'), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
