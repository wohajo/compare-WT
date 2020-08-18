from helpers import write_log
from constants import WORD_TO_REMOVE_PROCESSING

def process_general_characteristics(lst, url):
    if any(word in WORD_TO_REMOVE_PROCESSING for word in lst) or len(lst) == 0:
        write_log(0, 'processing.log', url)
        lst = []
        return lst
    
    lst[2] = lst[2].replace(' Rank', '')
    if 'Fighter' in lst[6] or 'fighter' in lst[6]:
        lst[6] = 'fighter'
    if 'Bomber' in lst[6] or 'bomber' in lst[6]:
        lst[6] = 'bomber'
    if 'Attacker' in lst[6] or 'attacker' in lst[6]:
        lst[6] = 'attacker'
    lst[7] = lst[7].replace('people', '').replace('person', '')
    lst[8] = lst[8].replace(' t', '')

    if len(lst) == 10:
        lst[9] = lst[9].replace(' kg/s', '')

    return lst

def process_flight_characteristics(lst, url):
    
    if any(word in WORD_TO_REMOVE_PROCESSING for word in lst) or len(lst) != 6:
        write_log(1, 'processing.log', url)
        lst = []
        return lst
    else:
        lst[0] = lst[0].replace(' m', '')
        lst[4] = lst[4].replace(' km/h', '') 
        lst[5] = lst[4].replace(' km/h', '') 
        return lst

def process_defensive_armament(lst, url):
    if any(word in WORD_TO_REMOVE_PROCESSING for word in lst):
        write_log(2, 'processing.log', url)
        lst = []
        return lst
    else:
        new_list = [word.replace(' rounds', '').replace(' shots/min', '') for word in lst]

        return new_list

def process_offensive_armament(lst, url):
    if any(word in WORD_TO_REMOVE_PROCESSING for word in lst):
        write_log(3, 'processing.log', url)
        lst = []
        return lst
    else:
        new_list = [word.replace(' rounds', '').replace(' shots/min', '') for word in lst]

        return new_list

def process_suspended_armament(lst, url):
    if any(word in WORD_TO_REMOVE_PROCESSING for word in lst):
        write_log(4, 'processing.log', url)
        lst = []
        return lst
    return lst

def process_economy(lst, url):
    if any(word in WORD_TO_REMOVE_PROCESSING for word in lst) or len(lst) == 0:
        write_log(5, 'processing.log', url)
        lst = []
        return lst
    else:
        new_list = []
        #TODO: Divide min-max repair for SB/RB/AB
        for word in lst:
            new_list.append(word.replace(' %', ''))

        return new_list

def process_characteristics_table(lst, url):
    if any(word in WORD_TO_REMOVE_PROCESSING for word in lst) or len(lst[0]) != 8 or len(lst[1]) not in [6, 8]:
        write_log(5, 'processing.log', url)
        lst = []
        return lst
    
    elif len(lst[1]) == 6:
        lst[1].insert(2, lst[0][2])
        lst[1].insert(7, lst[0][7])

    return lst

def process_features_table(lst, url):
    if len(lst) == 0:
        return lst
    else:
        new_list = []

        for word in lst:
            if word == 'X':
                new_list.append('false')
            else:
                new_list.append('true')

        return new_list

def process_optimal_velocities_table(lst, url):
    if len(lst) == 0:
        return lst
    else:
        new_list = []

        for word in lst:
            new_list.append(word.replace('< ', '').replace('N/A', '').replace('> ', ''))

        return new_list

def process_modules(lst, url):
    pass
