from models import *
from helpers import write_log

def add_plane_engine(engine_info, url):
    '''
    Converts info given about a plane's engine to a db object and returns it. 
    '''
    engine = None
    engine_type_id = None
    cooling_id = None

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

    if engine_type_id is None and cooling_id is not None:
        engine = Engine(name=engine_info[2], cooling_id=cooling_id)

    elif engine_type_id is not None and cooling_id is None:
        engine = Engine(name=engine_info[2], engine_type_id=engine_type_id)

    elif engine_type_id is None and cooling_id is None:
        engine = Engine(name=engine_info[2])

    else:
        engine = Engine(name=engine_info[2], cooling_id=cooling_id, engine_type_id=engine_type_id)
    
    return engine