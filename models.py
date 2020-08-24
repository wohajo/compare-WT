import sqlalchemy
from website_startup import db
from sqlalchemy.sql.schema import ForeignKey

class Country(db.Model):
    __tablename__ = "countries"

    country_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)

class PlaneClass(db.Model):
    __tablename__ = "plane_classes"

    plane_class_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    
class PlaneModule(db.Model):
    __tablename__ = "plane_modules"

    plane_module_id = db.Column(db.Integer, primary_key=True)
    tier = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(30), nullable=False)
    module_type_id = db.Column(db.Integer, ForeignKey('modules_types.module_type_id'))
    module_type = db.relationship('ModuleType', backref='module')

class ModuleType(db.Model):
    __tablename__ = "modules_types"

    module_type_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)

class Engine(db.Model):
    '''
    Engine class.
    (name)
    '''
    __tablename__ = "engines"

    engine_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)

class CoolingSystem(db.Model):
    __tablename__ = "cooling_systems" 

    cooling_sys_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)

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
    country = db.relationship('Country', backref='plane')
    rank = db.Column(db.Integer)
    battle_rating_ab = db.Column(db.Float)
    battle_rating_rb = db.Column(db.Float)
    battle_rating_sb = db.Column(db.Float)
    plane_class_id = db.Column(db.Integer, ForeignKey('plane_classes.plane_class_id'))
    plane_class = db.relationship('PlaneClass', backref='plane', lazy=True)
    crew = db.Column(db.Integer)
    
    # flight
    take_off_weight = db.Column(db.Integer)
    burst_mass = db.Column(db.Float)
    ceiling = db.Column(db.Integer)
    no_engines = db.Column(db.Integer)
    engine = db.Column(db.String(60))
    engine_type_id = db.Column(db.Integer, ForeignKey('engines.engine_id'))
    engine_type = db.relationship('Engine', backref='plane', lazy=True)
    cooling_id = db.Column(db.Integer, ForeignKey('cooling_systems.cooling_sys_id'))
    cooling = db.relationship('CoolingSystem', backref='plane', lazy=True)
    sod_structural = db.Column(db.Integer)
    sod_gear = db.Column(db.Integer)
    # TODO next 3 fields are ought to be many to many
    # offensive_armt = db.Column()
    # defensive_arm = db.Column()
    # suspended_arm = db.Column()
    
    # economy
    research = db.Column(db.Integer)
    purchase = db.Column(db.Integer)
    repair_min = db.Column(db.Integer)
    repair_max = db.Column(db.Integer)
    crew_training = db.Column(db.Integer)
    experts = db.Column(db.Integer)
    aces = db.Column(db.Integer)
    reward_rp = db.Column(db.Integer)
    reward_sl = db.Column(db.Integer)
    # TODO: add advanced tables
    # modules = db.Column() many to many
    
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
    combat_flaps = db.Column(db.Boolean)
    take_off_flaps = db.Column(db.Boolean)
    landing_flaps = db.Column(db.Boolean)
    air_brakes = db.Column(db.Boolean)
    arrestor_gear = db.Column(db.Boolean)
    drogue_chute = db.Column(db.Boolean)

    # optimal velocities
    ailerons = db.Column(db.Integer)
    rudder = db.Column(db.Integer)
    elevators = db.Column(db.Integer)
    radiator = db.Column(db.Integer)
