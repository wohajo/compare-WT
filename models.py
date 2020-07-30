from website_startup import db

class Countries(db.Model):
    country_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)

class PlaneClasses(db.Model):
    plane_class_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)

class Engines(db.Model):
    engine_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)

class CoolingSystems(db.Model):
    plane_class_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)

class Planes(db.Model):
    plane_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True, nullable=False)
    country_id = db.Column(db.relationship('Countries', backref='plane'))
    rank = db.Column(db.Integer, nullable=False)
    battle_rating = db.Column(db.Integer, nullable=False)
    # TODO download all modes BR?
    # plane_class = db.relationship('PlaneClasses', backref='plane', lazy=True)
    crew = db.Column(db.Integer, nullable=False)
    take_off_weight = db.Column(db.Integer, nullable=False)
    burst_mass = db.Column(db.Float)
    ceiling = db.Column(db.Integer, nullable=False)
    engine = db.Column(db.String(60), nullable=False)
    no_engines = db.Column(db.Integer)
    # engine_type = db.Column(db.relationship('Engines'), backref='plane', lazy=True)
    # cooling = db.Column(db.relationship('CoolingSystems', backref='plane', lazy=True))
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