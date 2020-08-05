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
    


class Engine(db.Model):
    __tablename__ = "engines"

    engine_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)



class CoolingSystem(db.Model):
    __tablename__ = "cooling_systems" 

    cooling_sys_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)



class Plane(db.Model):
    __tablename__ = "planes"

    plane_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True, nullable=False)
    country_id = db.Column(db.Integer, ForeignKey('countries.country_id'))
    country = db.relationship('Country', backref='plane')
    rank = db.Column(db.Integer, nullable=False)
    battle_rating = db.Column(db.Integer, nullable=False)
    # TODO download all modes BR?
    plane_class_id = db.Column(db.Integer, ForeignKey('plane_classes.plane_class_id'))
    plane_class = db.relationship('PlaneClass', backref='plane', lazy=True)
    crew = db.Column(db.Integer, nullable=False)
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
    research = db.Column(db.Integer, nullable=False)
    purchase = db.Column(db.Integer, nullable=False)
    repair_min = db.Column(db.Integer, nullable=False)
    repair_max = db.Column(db.Integer, nullable=False)
    crew_training = db.Column(db.Integer, nullable=False)
    experts = db.Column(db.Integer, nullable=False)
    aces = db.Column(db.Integer, nullable=False)
    reward_rp = db.Column(db.Integer, nullable=False)
    reward_sl = db.Column(db.Integer, nullable=False)