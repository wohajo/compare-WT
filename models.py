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
    name = db.Column(db.String(60), unique=True, nullable=False)
    country_id = db.Column(db.Integer, ForeignKey('countries.country_id'))
    country = db.relationship('Country', backref='plane')
    rank = db.Column(db.Integer, nullable=False)
    battle_rating_ab = db.Column(db.Float, nullable=False)
    battle_rating_rb = db.Column(db.Float, nullable=False)
    battle_rating_sb = db.Column(db.Float, nullable=False)
    plane_class_id = db.Column(db.Integer, ForeignKey('plane_classes.plane_class_id'))
    plane_class = db.relationship('PlaneClass', backref='plane', lazy=True)
    crew = db.Column(db.Integer, nullable=False)
    
    # flight
    take_off_weight = db.Column(db.Integer, nullable=False)
    burst_mass = db.Column(db.Float)
    ceiling = db.Column(db.Integer, nullable=False)
    engine = db.Column(db.String(60), nullable=False)
    no_engines = db.Column(db.Integer)
    engine_type_id = db.Column(db.Integer, ForeignKey('engines.engine_id'))
    engine_type = db.relationship('Engine', backref='plane', lazy=True)
    cooling_id = db.Column(db.Integer, ForeignKey('cooling_systems.cooling_sys_id'))
    cooling = db.relationship('CoolingSystem', backref='plane', lazy=True)
    sod_structural = db.Column(db.Integer, nullable=False)
    sod_gear = db.Column(db.Integer, nullable=False)
    # TODO next 3 fields are ought to be many to many
    # offensive_armt = db.Column()
    # defensive_arm = db.Column()
    # suspended_arm = db.Column()
    
    # economy
    research = db.Column(db.Integer, nullable=False)
    purchase = db.Column(db.Integer, nullable=False)
    repair_min = db.Column(db.Integer, nullable=False)
    repair_max = db.Column(db.Integer, nullable=False)
    crew_training = db.Column(db.Integer, nullable=False)
    experts = db.Column(db.Integer, nullable=False)
    aces = db.Column(db.Integer, nullable=False)
    reward_rp = db.Column(db.Integer, nullable=False)
    reward_sl = db.Column(db.Integer, nullable=False)
    # TODO: add advanced tables
    # modules = db.Column() many to many
    
    # characteristics 
    chr_stock_ab = db.Column(db.Integer, nullable=True)
    chr_upgraded_ab = db.Column(db.Integer, nullable=True)
    chr_stock_rb = db.Column(db.Integer, nullable=True)
    chr_upgraded_rb = db.Column(db.Integer, nullable=True)
    max_alt = db.Column(db.Integer, nullable=True)
    turn_stock_ab = db.Column(db.Integer, nullable=True)
    turn_upgraded_ab = db.Column(db.Integer, nullable=True)
    turn_stock_rb = db.Column(db.Integer, nullable=True)
    turn_upgraded_rb = db.Column(db.Integer, nullable=True)
    roc_stock_ab = db.Column(db.Integer, nullable=True)
    roc_upgraded_ab = db.Column(db.Integer, nullable=True)
    roc_stock_rb = db.Column(db.Integer, nullable=True)
    roc_upgraded_rb = db.Column(db.Integer, nullable=True)
    take_off_run = db.Column(db.Integer, nullable=True)
    
    # features
    combat_flaps = db.Column(db.Boolean, nullable=True)
    take_off_flaps = db.Column(db.Boolean, nullable=True)
    landing_flaps = db.Column(db.Boolean, nullable=True)
    air_brakes = db.Column(db.Boolean, nullable=True)
    arrestor_gear = db.Column(db.Boolean, nullable=True)
    drogue_chute = db.Column(db.Boolean, nullable=True)

    # optimal velocities
    ailerons = db.Column(db.Integer, nullable=True)
    rudder = db.Column(db.Integer, nullable=True)
    elevators = db.Column(db.Integer, nullable=True)
    radiator = db.Column(db.Integer, nullable=True)