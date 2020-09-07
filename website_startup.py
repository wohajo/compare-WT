from crypt import methods
from __init__ import app, db
from wtforms.form import Form
from flask.json import jsonify
from flask_wtf import FlaskForm
from wtforms import SelectField
from models import Country, Plane
from flask import render_template, request

@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.route('/compare-planes', methods=['GET', 'POST'])
def compare_planes():
    planes = Plane.query.all()
    countries = Country.query.all()
    comparsion_form_1 = PlaneCountryForm()
    comparsion_form_1.country.choices = [(country.country_id, country.name) for country in Country.query.all()]
    comparsion_form_1.plane.choices = [(plane.plane_id, plane.name) for plane in Plane.query.all()]

    if request.method == 'POST':

        return '<h1>Country: {}, Plane: {}</h1>'.format(comparsion_form_1.country.data, comparsion_form_1.plane.data)

    return render_template('compare_planes.html', title='Compare planes', comparsion_form_1=comparsion_form_1, planes=planes, countries=countries)

@app.route('/planes/<country_id>')
def plane(country_id):
    planes = Plane.query.filter_by(country_id=country_id).all()
    planes_list = []

    for plane in planes:
        plane_object = {}
        plane_object['id'] = plane.plane_id
        plane_object['name'] = plane.name
        planes_list.append(plane_object)

    return jsonify({'planes' : planes_list})

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

class PlaneCountryForm(FlaskForm):
    country = SelectField('Country', choices=[])
    plane = SelectField('Plane', choices=[])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
