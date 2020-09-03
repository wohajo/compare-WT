import os
from models import *
from website_startup import db
from constants import COUNTRIES, FLIGHT_PERFOMANCE_MODULES, SURVIVABILITY_MODULES

def create_database():
    if os.path.exists('planes_database.db'):
        print('Removing old database...')
        os.remove('planes_database.db')
        print('Removed!')
    if os.path.exists('vehicles.txt'):
        print('Removing old vehicle links...')
        os.remove('vehicles.txt')
        print('Removed!')
    if os.path.exists('inserted.log'):
        print('Removing old insertion log...')
        os.remove('inserted.log')
        print('Removed!')
    if os.path.exists('db_adding.log'):
        print('Removing old db_adding log...')
        os.remove('db_adding.log')
        print('Removed!')
    if os.path.exists('processing.log'):
        print('Removing old processing log...')
        os.remove('processing.log')
        print('Removed!')
    if os.path.exists('scrape_data.log'):
        print('Removing old scraping log...')
        os.remove('scrape_data.log')
        print('Removed!')
    print('Creating new database...')
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
        SusArmType(name='bomb'),
        SusArmType(name='rocket'),
        SusArmType(name='torpedo'),
        SusArmType(name='gun pod'),
        SusArmType(name='air-to-air missile'),
        SusArmType(name='air-to-ground missile')
    ]

    flight_performance_modules = [PlaneModule(name=module_name, module_type_id=1) for module_name in FLIGHT_PERFOMANCE_MODULES]
    survivalibity_modules = [PlaneModule(name=module_name, module_type_id=2) for module_name in SURVIVABILITY_MODULES]

    db.session.bulk_save_objects(countries)
    db.session.bulk_save_objects(module_types)
    db.session.bulk_save_objects(plane_classes)
    db.session.bulk_save_objects(cooling_systems)
    db.session.bulk_save_objects(engine_type)
    db.session.bulk_save_objects(sus_arm_type)
    db.session.bulk_save_objects(flight_performance_modules)
    db.session.bulk_save_objects(survivalibity_modules)
    db.session.commit()

if __name__ == "__main__":
    create_database()