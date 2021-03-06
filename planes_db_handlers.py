from models import *
from __init__ import db
from helpers import write_log
from list_modifiers import list_to_chunks

def get_id_or_create_plane_engine(engine_info, detailed_engine_info, url):
    '''
    Converts info given about a plane's engine to a db object, checks if it exists, and returns it's id. 
    '''
    engine = db.session.query(Engine).filter_by(name=engine_info[2]).scalar()
    engine_type_id = None
    cooling_id = None
    base_power = None
    wep_power = None

    if engine is None:
        if engine_info[3] == 'Radial':
            engine_type_id = 1
        elif engine_info[3] == 'Inline':
            engine_type_id = 2
        elif engine_info[3] == 'Jet':
            engine_type_id = 3
        else:
            write_log('engine_adding_type', 'db_adding_planes.log', url)
        
        if engine_info[4] == 'air':
            cooling_id = 1
        elif engine_info[4] == 'water':
            cooling_id = 2
        elif engine_info[4] == 'oil':
            cooling_id = 3
        else:
            write_log('engine_adding_cooling', 'db_adding_planes.log', url)

        if len(detailed_engine_info) == 2:
            base_power = detailed_engine_info[0]
            wep_power = detailed_engine_info[1]
        else:
            write_log('engine_adding_details', 'db_adding_planes.log', url)

        engine = Engine(name=engine_info[2], base_power=base_power, wep_power=wep_power, cooling_id=cooling_id, engine_type_id=engine_type_id)
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
        write_log('country_adding', 'db_adding_planes.log', url)
        return None

def add_economy_to_plane(plane, economy, url):
    if len(economy) != 0:
        plane.research = economy[0] 
        plane.purchase = economy[1]

        if economy[0] == 0 and len(economy) == 12:
            plane.is_premium = True
            plane.repair_min_sb = economy[2]
            plane.repair_min_rb = economy[3]
            plane.repair_min_ab = economy[4]
            plane.crew_training = economy[5]
            plane.experts = economy[6]
            plane.aces = economy[7]
            plane.reward_rp = economy[8]
            plane.reward_sl_sb = economy[9]
            plane.reward_sl_rb = economy[10]
            plane.reward_sl_ab = economy[11]
        else:
            plane.is_premium = False
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
        write_log('economy_insert', 'db_adding_planes.log', url)

def add_engine_and_sod_to_plane(plane, lst, detailed_info, url):
    if len(lst) != 0:
            if lst[0] is not None:
                plane.max_alt = lst[0]
            plane.no_engines = lst[1]
            plane.sod_structural = lst[5]
            plane.sod_gear = lst[6]
            engine_id = get_id_or_create_plane_engine(lst, detailed_info, url)
    else:
            engine_id = None
            write_log('engine/ceiling/sod_addding', 'db_adding_planes.log', url)

    plane.engine_id = engine_id

def add_general_characteristics(plane, lst, url):
    if len(lst) != 0:
        plane.rank = lst[2]
        plane.battle_rating_sb = lst[3]
        plane.battle_rating_rb = lst[4]
        plane.battle_rating_ab = lst[5]

        if lst[6] == 'fighter':
            plane.plane_class_id = 1
        elif lst[6] == 'attacker':
            plane.plane_class_id = 2
        elif lst[6] == 'bomber':
            plane.plane_class_id = 3
        else:
            plane.plane_class_id = None

        plane.crew=lst[7]
        plane.take_off_weight=lst[8]

        if len(lst) == 10:
            plane.burst_mass = lst[9]

        country_id = get_plane_country(lst[1], url)
        plane.country_id = country_id
    else:
        write_log('general_characteristics_adding', 'db_adding_planes.log', url)

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
            write_log('max_alt_adding', 'db_adding_planes.log', url)

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
            write_log('take_off_run_adding', 'db_adding_planes.log', url)
    else:
            write_log('characteristics_adding', 'db_adding_planes.log', url)

def add_features_to_plane(plane, features, url):
    if len(features) != 0:
        if None in features:
            write_log('features_adding', 'db_adding_planes.log', url)
        plane.combat_flaps = features[0]
        plane.take_off_flaps = features[1]
        plane.landing_flaps = features[2]
        plane.air_brakes = features[3]
        plane.arrestor_gear = features[4]
        plane.drogue_chute = features[5]
        plane.radar_warning_receiver = False
        plane.ballistic_computer = False
    else:
        write_log('features_adding', 'db_adding_planes.log', url)

def add_flaps_sods_to_plane(plane, sods, url):
    if len(sods) != 0:
        if None in sods:
            write_log('flaps_sods_adding', 'db_adding_planes.log', url)
        plane.sod_combat_flaps = sods[0]
        plane.sod_takeoff_flaps = sods[1]
        plane.sod_landing_flaps = sods[2]
    else:
        write_log('flaps_sods_adding', 'db_adding_planes.log', url)

def add_optimal_velocities_to_plane(plane, optimal_vel, url):
    if len(optimal_vel) != 0:
        if None in optimal_vel:
            write_log('optimal_velocities_adding', 'db_adding_planes.log', url)
        plane.ailerons = optimal_vel[0]
        plane.rudder = optimal_vel[1]
        plane.elevators = optimal_vel[2]
        plane.radiator = optimal_vel[3]
    else:
        write_log('optimal_velocities_adding', 'db_adding_planes.log', url)

def add_weapons_to_plane(plane, is_defensive, weapons, url):
    '''
    Adds defensive and offensive weapons to plane, based on is_defensive variable.
    '''
    if len(weapons) % 4 != 0:
        write_log('weapons_adding', 'db_adding_planes.log', url)
    else:
        lst = (list_to_chunks(weapons, 4))
        for weapon_list in lst:
            weapon_id = get_id_or_create_weapon(weapon_list)
            if is_defensive:
                plane_weapon = PlaneDefensiveWeapon(quantity=weapon_list[0], rounds=weapon_list[2], weapon_id=weapon_id, plane_id=plane.plane_id)
            else:
                plane_weapon = PlaneOffensiveWeapon(quantity=weapon_list[0], rounds=weapon_list[2], weapon_id=weapon_id, plane_id=plane.plane_id)
            db.session.add(plane_weapon)

def get_id_or_create_weapon(weapon_info):
    '''
    Converts info given about a weapon to a db object, checks if it exists, and returns it's id. 
    '''
    weapon = db.session.query(Weapon).filter_by(name=weapon_info[1]).scalar()

    if weapon is None:

        weapon = Weapon(name=weapon_info[1], rounds_min=weapon_info[3])
        db.session.add(weapon)
        db.session.flush()

    return weapon.weapon_id

def add_modules_to_plane(plane, modules, url):
    for module_name in modules:
        module = get_or_create_plane_module(module_name)
        plane.plane_modules.append(module)

def get_or_create_plane_module(module_name):
    '''
    Converts info given about a module to a db object, checks if it exists, and returns it. 
    '''
    module = db.session.query(PlaneModule).filter_by(name=module_name).scalar()

    if module is None:

        module = PlaneModule(name=module_name, module_type_id=3)
        db.session.add(module)
        db.session.flush()

    return module

def add_suspended_armament_to_plane(plane, suspended_armament, url):
    for arm_name in suspended_armament:
        arm = get_or_create_sus_arm(arm_name)
        plane.plane_sus_arm.append(arm)
        
def get_or_create_sus_arm(arm_name):
    '''
    Converts info given about suspended weapon to a db object, checks if it exists, and returns it's id. 
    '''
    new_arm_name = arm_name
    new_arm_name = new_arm_name.replace('bombs', '').replace('bomb', '').replace('rockets', '').replace('torpedo', '')
    new_arm_name = new_arm_name.replace('secondary', '').replace('air-to-air missiles', '').replace('air-to-air missile', '')
    new_arm_name = new_arm_name.replace('air-to-ground missiles', '').replace('air-to-ground missile', '').replace('rocket', '')
    new_arm_name = new_arm_name.replace('mines', '').replace('mine', '')
    new_arm_name = new_arm_name.replace('Bullpup', '').rstrip()

    arm = db.session.query(SuspendedArmament).filter_by(name=new_arm_name).scalar()

    if arm is None:
        if 'bomb' in arm_name or 'bombs' in arm_name:
            arm_type_id = 1
            arm_name = arm_name.replace('bombs', '').replace('bomb', '').rstrip()

        elif 'torpedo' in arm_name:
            arm_type_id = 3
            arm_name = arm_name.replace('torpedos', '').replace('torpedo', '').rstrip()

        elif 'secondary' in arm_name:
            arm_type_id = 4
            arm_name = arm_name.replace('secondary', '').rstrip()

        elif 'air-to-air' in arm_name:
            arm_type_id = 5
            arm_name = arm_name.replace('air-to-air missiles', '').replace('air-to-air missile', '').rstrip()

        elif 'AGM' in arm_name or 'Bullpup' or 'ATGM' or'air-to-ground' in arm_name in arm_name:
            arm_type_id = 6
            arm_name = arm_name.replace('air-to-ground missiles', '').replace('air-to-ground missile', '').replace('Bullpup', '').replace('rockets', '').replace('rocket', '').rstrip()

        elif 'rocket' in arm_name or 'rockets' in arm_name:
            arm_type_id = 2
            arm_name = arm_name.replace('rockets', '').replace('rocket', '').rstrip()

        elif 'mine' in arm_name:
            arm_type_id = 7
            arm_name = arm_name.replace('mines', '').replace('mine', '').rstrip()

        else:
            arm_type_id = None

        arm = SuspendedArmament(name=arm_name, arm_type=arm_type_id)
        db.session.add(arm)
        db.session.flush()

    return arm