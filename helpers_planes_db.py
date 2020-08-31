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