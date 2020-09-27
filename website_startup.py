from models import *
from crypt import methods
from __init__ import app, db
from wtforms.form import Form
from flask.json import jsonify
from flask_wtf import FlaskForm
from wtforms import SelectField
from helpers import int_to_roman
from flask import render_template, request

@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.route('/compare-planes', methods=['GET'])
def compare_planes():
    planes_first_country = Plane.query.filter_by(country_id=1).all()
    countries = Country.query.all()

    comparsion_form_1 = PlaneCountryForm()
    comparsion_form_1.country.choices = [(country.country_id, country.name) for country in countries]
    comparsion_form_1.plane.choices = [(plane.plane_id, plane.name + ' [' + str(int_to_roman(plane.rank)) + ']') for plane in planes_first_country]

    comparsion_form_2 = PlaneCountryForm()
    comparsion_form_2.country.choices = [(country.country_id, country.name) for country in countries]
    comparsion_form_2.plane.choices = [(plane.plane_id, plane.name + ' [' + str(int_to_roman(plane.rank)) + ']') for plane in planes_first_country]

    comparsion_form_3 = PlaneCountryForm()
    comparsion_form_3.country.choices = [(country.country_id, country.name) for country in countries]
    comparsion_form_3.plane.choices = [(plane.plane_id, plane.name + ' [' + str(int_to_roman(plane.rank)) + ']') for plane in planes_first_country]

    comparsion_form_4 = PlaneCountryForm()
    comparsion_form_4.country.choices = [(country.country_id, country.name) for country in countries]
    comparsion_form_4.plane.choices = [(plane.plane_id, plane.name + ' [' + str(int_to_roman(plane.rank)) + ']') for plane in planes_first_country]

    return render_template('compare_planes.html', title='Compare planes', 
    comparsion_form_1=comparsion_form_1, comparsion_form_2=comparsion_form_2, comparsion_form_3=comparsion_form_3, comparsion_form_4=comparsion_form_4, planes=planes_first_country, countries=countries)

@app.route('/co+pl/<country_id>')
def get_planes_by_country(country_id):
    planes = Plane.query.filter_by(country_id=country_id).all()
    planes_list = []

    for plane in planes:
        plane_object = {}
        plane_object['id'] = plane.plane_id
        plane_object['name'] = plane.name + ' [' + str(int_to_roman(plane.rank)) + ']'
        planes_list.append(plane_object)

    return jsonify({'planes' : planes_list})

@app.route('/ple/<plane_id>')
def plane(plane_id):
    plane = Plane.query.filter_by(plane_id = plane_id).first()

    plane_object = {}
    plane_object['img_link'] = plane.img_link
    plane_object['name'] = plane.name
    plane_object['tier'] = int_to_roman(plane.rank)
    plane_object['battle_rating_ab'] = plane.battle_rating_ab
    plane_object['battle_rating_rb'] = plane.battle_rating_rb
    plane_object['battle_rating_sb'] = plane.battle_rating_sb
    plane_object['class'] = PlaneClass.query.filter_by(plane_class_id=plane.plane_class_id).first().name
    plane_object['crew'] = plane.crew
    plane_object['take_off_weight'] = plane.take_off_weight
    plane_object['burst_mass'] = plane.burst_mass
    plane_object['no_engines'] = plane.no_engines

    if plane.engine is not None:
        plane_object['engine_name'] = plane.engine.name
        plane_object['engine_type'] = plane.engine.engine_type.name
        plane_object['engine_cooling_type'] = plane.engine.cooling_system.name
        plane_object['base_power'] = plane.engine.base_power
        plane_object['wep_power'] = plane.engine.wep_power
    else:
        plane_object['engine_name'] = None
        plane_object['engine_type'] = None
        plane_object['engine_cooling_type'] = None 
        plane_object['base_power'] = None
        plane_object['wep_power'] = None

    plane_object['is_premium'] = plane.is_premium
    plane_object['research'] = plane.research
    plane_object['purchase'] = plane.purchase
    plane_object['repair_min_ab'] = plane.repair_min_ab
    plane_object['repair_max_ab'] = plane.repair_max_ab
    plane_object['repair_min_rb'] = plane.repair_min_rb
    plane_object['repair_max_rb'] = plane.repair_max_rb
    plane_object['repair_min_sb'] = plane.repair_min_sb
    plane_object['repair_max_sb'] = plane.repair_max_sb
    plane_object['crew_training'] = plane.crew_training
    plane_object['experts'] = plane.experts
    plane_object['aces'] = plane.aces
    plane_object['reward_rp'] = plane.reward_rp
    plane_object['reward_sl_sb'] = plane.reward_sl_sb
    plane_object['reward_sl_rb'] = plane.reward_sl_rb
    plane_object['reward_sl_ab'] = plane.reward_sl_ab

    plane_object['max_speed_stock_ab'] = plane.max_speed_stock_ab
    plane_object['max_speed_upgraded_ab'] = plane.max_speed_upgraded_ab
    plane_object['max_speed_stock_rb'] = plane.max_speed_stock_rb
    plane_object['max_speed_upgraded_rb'] = plane.max_speed_upgraded_rb
    plane_object['max_alt'] = plane.max_alt
    plane_object['turn_stock_ab'] = plane.turn_stock_ab
    plane_object['turn_upgraded_ab'] = plane.turn_upgraded_ab
    plane_object['turn_stock_rb'] = plane.turn_stock_rb
    plane_object['turn_upgraded_rb'] = plane.turn_upgraded_rb
    plane_object['roc_stock_ab'] = plane.roc_stock_ab
    plane_object['roc_upgraded_ab'] = plane.roc_upgraded_ab
    plane_object['roc_stock_rb'] = plane.roc_stock_rb
    plane_object['roc_upgraded_rb'] = plane.roc_upgraded_rb
    plane_object['take_off_run'] = plane.take_off_run

    plane_object['combat_flaps'] = plane.combat_flaps
    plane_object['take_off_flaps'] = plane.take_off_flaps
    plane_object['landing_flaps'] = plane.landing_flaps
    plane_object['air_brakes'] = plane.air_brakes
    plane_object['arrestor_gear'] = plane.arrestor_gear
    plane_object['drogue_chute'] = plane.drogue_chute
    plane_object['radar_warning_receiver'] = plane.radar_warning_receiver
    plane_object['ballistic_computer'] = plane.ballistic_computer
    
    plane_object['sod_structural'] = plane.sod_structural
    plane_object['sod_gear'] = plane.sod_gear
    plane_object['sod_combat_flaps'] = plane.sod_combat_flaps
    plane_object['sod_takeoff_flaps'] = plane.sod_takeoff_flaps
    plane_object['sod_landing_flaps'] = plane.sod_landing_flaps

    plane_object['ailerons'] = plane.ailerons
    plane_object['rudder'] = plane.rudder
    plane_object['elevators'] = plane.elevators
    plane_object['radiator'] = plane.radiator
    plane_object['modules'] = [module.name + ' (' + module.module_type.name + ') \n' for module in plane.plane_modules]

    plane_object['offensive_armament'] = []
    plane_object['defensive_armament'] = []
    plane_object['suspended_armament'] = [sus_arm.name + ' (' + sus_arm.sus_arm_type.name + ') \n' if sus_arm.sus_arm_type is not None else {'name': sus_arm.name, 'type': None} for sus_arm in plane.plane_sus_arm]

    for weapon, plane_weapon in db.session.query(Weapon, PlaneOffensiveWeapon).filter(PlaneOffensiveWeapon.plane_id == plane_id).filter(Weapon.weapon_id == PlaneOffensiveWeapon.weapon_id).all():
        plane_object['offensive_armament'].append(str(plane_weapon.quantity) + 'x ' + weapon.name + ' (' + str(plane_weapon.rounds) + ') | (' + str(weapon.rounds_min) + '/min)')

    for weapon, plane_weapon in db.session.query(Weapon, PlaneDefensiveWeapon).filter(PlaneDefensiveWeapon.plane_id == plane_id).filter(Weapon.weapon_id == PlaneDefensiveWeapon.weapon_id).all():
        plane_object['defensive_armament'].append(str(plane_weapon.quantity) + 'x ' + weapon.name + ' (' + str(plane_weapon.rounds) + ') | (' + str(weapon.rounds_min) + '/min)')

    return jsonify({'plane' : plane_object})

@app.route('/compare-tanks')
def compare_tanks():
    return render_template('in_progress.html', title='Compare tanks')

@app.route('/compare-helicopters')
def compare_helicopters():
    return render_template('in_progress.html', title='Compare helicopters')

@app.route('/compare-fleet')
def compare_fleet():
    return render_template('in_progress.html', title='Compare fleet')

@app.route('/planes')
def planes():
    return render_template('planes.html', title='Planes')

@app.route('/tanks')
def tanks():
    return render_template('in_progress.html', title='Tanks')

@app.route('/helicopters')
def helicopters():
    return render_template('in_progress.html', title='Helicopters')

@app.route('/fleet')
def fleet():
    return render_template('in_progress.html', title='Fleet')

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
