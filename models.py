import sqlalchemy
from website_startup import db
from sqlalchemy.orm import backref
from sqlalchemy.sql.schema import ForeignKey

_planes_modules = db.Table('_planes_modules',
    db.Column('plane_id', db.Integer, db.ForeignKey('planes.plane_id')),
    db.Column('module_id', db.Integer, db.ForeignKey('planes_modules.plane_module_id'))
    )

_planes_sus_arm = db.Table('_planes_sus_arm',
    db.Column('plane_id', db.Integer, db.ForeignKey('planes.plane_id')),
    db.Column('sus_arm_id', db.Integer, db.ForeignKey('suspended_armaments.sus_arm_id')),
)

class Country(db.Model):
    __tablename__ = "countries"

    country_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    planes = db.relationship('Plane', backref='country') 

class PlaneClass(db.Model):
    __tablename__ = "plane_classes"

    plane_class_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    planes = db.relationship('Plane', backref='plane_class') 
    
class PlaneModule(db.Model):
    __tablename__ = "planes_modules"

    plane_module_id = db.Column(db.Integer, primary_key=True)
    tier = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(30), nullable=False, unique=True)
    module_type_id = db.Column(db.Integer, ForeignKey('modules_types.module_type_id'))

class ModuleType(db.Model):
    __tablename__ = "modules_types"

    module_type_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False, unique=True)
    plane_modules = db.relationship('PlaneModule', backref='module_type')

class Engine(db.Model):
    '''
    Engine class.
    (name)
    '''
    __tablename__ = "engines"

    engine_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False, unique=True)
    engine_type_id = db.Column(db.Integer, ForeignKey('engine_types.engine_type_id'))
    cooling_id = db.Column(db.Integer, ForeignKey('cooling_systems.cooling_sys_id'))
    planes = db.relationship('Plane', backref='engine')

class EngineType(db.Model):
    '''
    Engine class.
    (name)
    '''
    __tablename__ = "engine_types"

    engine_type_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False, unique=True)
    engines = db.relationship('Engine', backref='engine_type')

class CoolingSystem(db.Model):
    __tablename__ = "cooling_systems" 

    cooling_sys_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    engines = db.relationship('Engine', backref='cooling_system')

class Plane(db.Model):
    '''
    Plane class.
    (name, country, rank, BR, plane class [...])
    '''
    __tablename__ = "planes"

    # general
    plane_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    img_link = db.Column(db.String(300))
    country_id = db.Column(db.Integer, ForeignKey('countries.country_id'))
    rank = db.Column(db.Integer)
    battle_rating_sb = db.Column(db.Float)
    battle_rating_rb = db.Column(db.Float)
    battle_rating_ab = db.Column(db.Float)
    plane_class_id = db.Column(db.Integer, ForeignKey('plane_classes.plane_class_id'))
    crew = db.Column(db.Integer)
    
    # flight
    take_off_weight = db.Column(db.Integer)
    burst_mass = db.Column(db.Float)
    ceiling = db.Column(db.Integer)
    no_engines = db.Column(db.Integer)
    engine_id = db.Column(db.Integer, ForeignKey('engines.engine_id'))
    # weaponry
    offensive_weapons = db.relationship('PlaneOffensiveWeapon', backref='plane')
    defensive_weapons = db.relationship('PlaneDefensiveWeapon', backref='plane')
    plane_sus_arm_setups = db.relationship('SuspendedArmament', secondary=_planes_sus_arm, backref=backref('planes_sus_arm', lazy='dynamic'))
    
    # economy
    research = db.Column(db.Integer)
    purchase = db.Column(db.Integer)
    repair_min_ab = db.Column(db.Integer)
    repair_max_ab = db.Column(db.Integer)
    repair_min_rb = db.Column(db.Integer)
    repair_max_rb = db.Column(db.Integer)
    repair_min_sb = db.Column(db.Integer)
    repair_max_sb = db.Column(db.Integer)
    crew_training = db.Column(db.Integer)
    experts = db.Column(db.Integer)
    aces = db.Column(db.Integer)
    reward_rp = db.Column(db.Integer)
    reward_sl_sb = db.Column(db.Integer)
    reward_sl_rb = db.Column(db.Integer)
    reward_sl_ab = db.Column(db.Integer)
    
    # characteristics 
    chr_stock_ab = db.Column(db.Integer)
    chr_upgraded_ab = db.Column(db.Integer)
    chr_stock_rb = db.Column(db.Integer)
    chr_upgraded_rb = db.Column(db.Integer)
    max_alt = db.Column(db.Integer)
    turn_stock_ab = db.Column(db.Integer)
    turn_upgraded_ab = db.Column(db.Integer)
    turn_stock_rb = db.Column(db.Integer)
    turn_upgraded_rb = db.Column(db.Integer)
    roc_stock_ab = db.Column(db.Integer)
    roc_upgraded_ab = db.Column(db.Integer)
    roc_stock_rb = db.Column(db.Integer)
    roc_upgraded_rb = db.Column(db.Integer)
    take_off_run = db.Column(db.Integer)
    
    # features
    plane_modules = db.relationship('PlaneModule', secondary=_planes_modules, backref=backref('planes_modules', lazy='dynamic'))
    combat_flaps = db.Column(db.Boolean)
    take_off_flaps = db.Column(db.Boolean)
    landing_flaps = db.Column(db.Boolean)
    air_brakes = db.Column(db.Boolean)
    arrestor_gear = db.Column(db.Boolean)
    drogue_chute = db.Column(db.Boolean)
    radar_warning_receiver = db.Column(db.Boolean)
    ballistic_computer = db.Column(db.Boolean)

    # limits
    sod_structural = db.Column(db.Integer)
    sod_gear = db.Column(db.Integer)
    sod_combat_flaps = db.Column(db.Integer)
    sod_takeoff_flaps = db.Column(db.Integer)
    sod_landing_flaps = db.Column(db.Integer)

    # optimal velocities
    ailerons = db.Column(db.Integer)
    rudder = db.Column(db.Integer)
    elevators = db.Column(db.Integer)
    radiator = db.Column(db.Integer)

class Weapon(db.Model):
    __tablename__ = "weapons" 

    weapon_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)
    rounds_min = db.Column(db.Integer)
    planes_offensive_weapons = db.relationship('PlaneOffensiveWeapon', backref='plane_off_weapon')
    planes_offensive_weapons = db.relationship('PlaneDefensiveWeapon', backref='plane_def_weapon')

class PlaneOffensiveWeapon(db.Model):
    __tablename__ = "plane_offensive_weapons"

    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer)
    rounds = db.Column(db.Integer)
    weapon_id = db.Column(db.Integer, db.ForeignKey('weapons.weapon_id'))
    plane_id = db.Column(db.Integer, db.ForeignKey('planes.plane_id'))

class PlaneDefensiveWeapon(db.Model):
    __tablename__ = "plane_defensive_weapons"

    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer)
    rounds = db.Column(db.Integer)
    weapon_id = db.Column(db.Integer, db.ForeignKey('weapons.weapon_id'))
    plane_id = db.Column(db.Integer, db.ForeignKey('planes.plane_id'))

class SusArmType(db.Model):
    __tablename__ = "sus_arm_types"

    sus_arm_type_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    suspended_armaments = db.relationship('SuspendedArmament', backref='sus_arm_type')

class SuspendedArmament(db.Model):
    __tablename__ = "suspended_armaments"

    sus_arm_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    arm_type = db.Column(db.Integer, ForeignKey('sus_arm_types.sus_arm_type_id'))
