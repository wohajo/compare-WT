import os
from models import *
from website_startup import db
from constants import COUNTRIES

def create_database():
    if os.path.exists('temp_db.db'):
        print('Removing old database...')
        os.remove('temp_db.db')
    
    db.create_all()
    
    countries = [
        Country(name=COUNTRIES[0]),
        Country(name=COUNTRIES[1]),
        Country(name=COUNTRIES[2]),
        Country(name=COUNTRIES[3]),
        Country(name=COUNTRIES[4]),
        Country(name=COUNTRIES[5]),
        Country(name=COUNTRIES[6]),
        Country(name=COUNTRIES[7]),
        Country(name=COUNTRIES[8]),
    ]

    module_types = [
        ModuleType(name='Flight perfomance'),
        ModuleType(name='Survivability'),
        ModuleType(name='Weaponry')
    ]

    plane_classes = [
        PlaneClass(name='Fighter'),
        PlaneClass(name='Attacker'),
        PlaneClass(name='Bomber')
    ]

    cooling_systems = [
        CoolingSystem(name='air'),
        CoolingSystem(name='water'),
        CoolingSystem(name='oil'),
    ]

    engine_type = [
        EngineType(name='radial'),
        EngineType(name='inline'),
        EngineType(name='jet'),
    ]

    sus_arm_type = [
        SusArmType(name='radial'),
        SusArmType(name='inline'),
        SusArmType(name='jet'),
    ]

    db.session.bulk_save_objects(countries)
    db.session.bulk_save_objects(module_types)
    db.session.bulk_save_objects(plane_classes)
    db.session.bulk_save_objects(cooling_systems)
    db.session.bulk_save_objects(engine_type)
    db.session.bulk_save_objects(sus_arm_type)
    db.session.commit()

if __name__ == "__main__":
    create_database()