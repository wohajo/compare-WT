from models import *
from __init__ import db
from helpers import write_log

def get_or_create_plane_engine(engine_info, url):
    '''
    Converts info given about a plane's engine to a db object, checks if it exists, and returns it. 
    '''
    engine = db.session.query(Engine).filter_by(name=engine_info[2]).scalar()
    engine_type_id = None
    cooling_id = None

    if engine is None:
        if engine_info[3] == 'Radial':
            engine_type_id = 1
        elif engine_info[3] == 'Inline':
            engine_type_id = 2
        elif engine_info[3] == 'Jet':
            engine_type_id = 3
        else:
            write_log('engine_adding_type', 'db_adding.log', url)
        
        if engine_info[4] == 'air':
            cooling_id = 1
        elif engine_info[4] == 'water':
            cooling_id = 2
        elif engine_info[4] == 'oil':
            cooling_id = 3
        else:
            write_log('engine_adding_cooling', 'db_adding.log', url)

        engine = Engine(name=engine_info[2], cooling_id=cooling_id, engine_type_id=engine_type_id)
        db.session.add(engine)
        db.session.flush()

    return engine.engine_id

def get_plane_country(country, url):
    '''
    Checks which country should plane be appended to.
    '''

    country_id = db.session.query(Country.country_id).filter_by(name=country).scalar()

    if country is not None:
        return country_id
    else:
        write_log('country_adding', 'db_adding.log', url)
        return None

def add_economy_to_plane(plane, economy, url):
    if len(economy) != 0:
            plane.research = economy[0] 
            plane.purchase = economy[1]
            plane.repair_min_sb = economy[2]
            plane.repair_max_sb = economy[3]
            plane.repair_min_rb = economy[4]
            plane.repair_max_rb = economy[5]
            plane.repair_min_ab = economy[6]
            plane.repair_max_ab = economy[7]
            plane.crew_training = economy[8]
            plane.experts = economy[9]
            plane.aces = economy[10]
            plane.reward_rp = economy[11]
            plane.reward_sl_sb = economy[12]
            plane.reward_sl_rb = economy[13]
            plane.reward_sl_ab = economy[14]
    else:
        write_log('economy_insert', 'db_adding.log', url)

def add_engine_and_sod_to_plane(plane, lst, url):
    if len(lst) != 0:
            if lst[0] is not None:
                plane.max_alt = lst[0]
            plane.no_engines = lst[1]
            plane.sod_structural = lst[5]
            plane.sod_gear = lst[6]
            engine_id = get_or_create_plane_engine(lst, url)
    else:
            engine_id = None
            write_log('engine/ceiling/sod_addding', 'db_adding.log', url)

    plane.engine_id = engine_id

def add_general_characteristics(plane, lst, url):
    if len(lst) != 0:
        plane.rank = lst[2]
        plane.battle_rating_sb = lst[3]
        plane.battle_rating_rb = lst[4]
        plane.battle_rating_ab = lst[5]
        plane.plane_class_id = None
        plane.crew=lst[7]
        plane.take_off_weight=lst[8]

        if len(lst) == 10:
            plane.burst_mass = lst[9]

        country_id = get_plane_country(lst[1], url)
        plane.country_id = country_id
    else:
        write_log('general_characteristics_adding', 'db_adding.log', url)

def add_characteristics_to_plane(plane, characteristics, url):
    if len(characteristics) != 0:
        plane.max_speed_stock_ab = characteristics[0][0]
        plane.max_speed_upgraded_ab = characteristics[1][0]
        plane.max_speed_stock_rb = characteristics[0][1]
        plane.max_speed_upgraded_rb = characteristics[1][1]

        if characteristics[0][2] == characteristics[1][2] and characteristics[0][2] is not None:
            if plane.max_alt is None:
                plane.max_alt = characteristics[0][2] 
        else:
            write_log('max_alt_adding', 'db_adding.log', url)

        plane.turn_stock_ab = characteristics[0][3]
        plane.turn_upgraded_ab = characteristics[1][3]
        plane.turn_stock_rb = characteristics[0][4]
        plane.turn_upgraded_rb = characteristics[1][4]
        plane.roc_stock_ab = characteristics[0][5]
        plane.roc_upgraded_ab = characteristics[1][5]
        plane.roc_stock_rb = characteristics[0][6]
        plane.roc_upgraded_rb = characteristics[1][6]

        if characteristics[0][7] == characteristics[1][7] and characteristics[0][7] is not None:
            plane.take_off_run = characteristics[0][7]
        else:
            plane.take_off_run = None
            write_log('take_off_run_adding', 'db_adding.log', url)
    else:
            write_log('characteristics_adding', 'db_adding.log', url)

def add_features_to_plane(plane, features, url):
    if len(features) != 0:
        if None in features:
            write_log('features_adding', 'db_adding.log', url)
        plane.combat_flaps = features[0]
        plane.take_off_flaps = features[1]
        plane.landing_flaps = features[2]
        plane.air_brakes = features[3]
        plane.arrestor_gear = features[4]
        plane.drogue_chute = features[5]
        plane.radar_warning_receiver = False
        plane.ballistic_computer = False
    else:
        write_log('features_adding', 'db_adding.log', url)

def add_flaps_sods_to_plane(plane, sods, url):
    if len(sods) != 0:
        if None in sods:
            write_log('flaps_sods_adding', 'db_adding.log', url)
        plane.sod_combat_flaps = sods[0]
        plane.sod_takeoff_flaps = sods[1]
        plane.sod_landing_flaps = sods[2]
    else:
        write_log('flaps_sods_adding', 'db_adding.log', url)

def add_optimal_velocities_to_plane(plane, optimal_vel, url):
    if len(optimal_vel) != 0:
        if None in optimal_vel:
            write_log('optimal_velocities_adding', 'db_adding.log', url)
        plane.ailerons = optimal_vel[0]
        plane.rudder = optimal_vel[1]
        plane.elevators = optimal_vel[2]
        plane.radiator = optimal_vel[3]
    else:
        write_log('optimal_velocities_adding', 'db_adding.log', url)
