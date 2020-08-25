import re
from helpers import write_log, remove_weird_chars
from constants import WORD_TO_REMOVE_PROCESSING, ROMAN_TO_INTEGER

def filter_characteristics(n):
    if '.' in n:
        try:
            return float(n)
        except ValueError:
            return None
    try:
        return int(n)
    except ValueError:
        return None

def separate_quantity_weapon(lst):
    new_list = []
    for word in lst:
        if isinstance(word, int):
            new_list.append(int(word))
        elif 'x' in word:
            words = word.split(' x ')
            new_list.append(int(words[0]))
            new_list.append(words[1])
        else:
            new_list.append(1)
            new_list.append(word)
    return new_list

def process_general_characteristics(lst, url):
    if any(word in WORD_TO_REMOVE_PROCESSING for word in lst) or len(lst) == 0:
        write_log(0, 'processing.log', url)
        lst = []
        return lst
    lst[0] = lst[0].replace('\xa0', ' ')
    lst[2] = lst[2].replace(' Rank', '')
    lst[2] = ROMAN_TO_INTEGER[lst[2]]
    lst[3] = float(lst[3])
    lst[4] = float(lst[4])
    lst[5] = float(lst[5])
    if 'Fighter' in lst[6] or 'fighter' in lst[6]:
        lst[6] = 'fighter'
    if 'Bomber' in lst[6] or 'bomber' in lst[6]:
        lst[6] = 'bomber'
    if 'Attacker' in lst[6] or 'attacker' in lst[6]:
        lst[6] = 'attacker'
    lst[7] = int(lst[7].replace(' people', '').replace(' person', ''))
    lst[8] = float(lst[8].replace(' t', ''))

    if len(lst) == 10:
        lst[9] = float(lst[9].replace(' kg/s', ''))

    return lst

def process_flight_characteristics(lst, url):
    
    if any(word in WORD_TO_REMOVE_PROCESSING for word in lst) or len(lst) != 6:
        write_log(1, 'processing.log', url)
        lst = []
        return lst
    else:
        engines = lst[1].split(' х ')
        lst[0] = int(lst[0].replace(' m', '').replace(' ', ''))
        lst[4] = int(lst[4].replace(' km/h', '').replace(' ', '')) 
        lst[5] = int(lst[5].replace(' km/h', '').replace(' ', ''))
        if len(engines) == 1:
            lst[1] = 1
            lst.insert(2, engines[0])
        else:
            lst[1] = int(engines[0])
            lst.insert(2, engines[1])
        return lst

def process_defensive_armament(lst, url):
    if any(word in WORD_TO_REMOVE_PROCESSING for word in lst):
        write_log(2, 'processing.log', url)
        lst = []
        return lst
    else:
        lst = [word.replace(' rounds', '').replace(' shots/min', '') for word in lst]
        lst = [int(word.replace(' ', '')) if re.match('[0-9 ]+$', word) else word for word in lst]
        
        return separate_quantity_weapon(lst)

def process_offensive_armament(lst, url):
    if any(word in WORD_TO_REMOVE_PROCESSING for word in lst):
        write_log(3, 'processing.log', url)
        lst = []
        return lst
    else:
        lst = [word.replace(' rounds', '').replace(' shots/min', '') for word in lst]
        lst = [int(word.replace(' ', '')) if re.match('[0-9 ]+$', word) else word for word in lst]
        
        return separate_quantity_weapon(lst)

def process_suspended_armament(lst, url):
    #TODO process suspended armament as in defensive armament and modules?
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
        new_list = [word.replace(' %', '').replace(' ', '') for word in lst]
        if 'free' not in lst:
            repair_sb = new_list[2].partition('/')
            repair_rb = new_list[3].partition('/')
            repair_ab = new_list[4].partition('/')
            new_list[2] = repair_sb[0] 
            new_list[3] = repair_rb[0]
            new_list[4] = repair_ab[0]
            new_list.insert(3, repair_sb[2])
            new_list.insert(5, repair_rb[2])
            new_list.insert(7, repair_ab[2])
        else:
            new_list = [word.replace('free', '0') for word in new_list]
            for i in range(3, 9):
                new_list.insert(i, '0')

        new_list = [int(word) for word in new_list]
        return new_list

def process_characteristics_table(lst, url):
    if any(word in WORD_TO_REMOVE_PROCESSING for word in lst) or len(lst[0]) != 8 or len(lst[1]) not in [6, 8]:
        write_log(5, 'processing.log', url)
        lst = []
        return lst
    
    elif len(lst[1]) == 6:
        lst[1].insert(2, lst[0][2])
        lst[1].insert(7, lst[0][7])

    for i in range(0, 2):
        lst[i] = [filter_characteristics(n) for n in lst[i]]

    return lst

def process_features_table(lst, url):
    if len(lst) == 0:
        return lst
    else:
        new_list = [False if word == 'X' else True for word in lst]
        if len(new_list) == 5:
            new_list.append(False)
        return new_list

def process_optimal_velocities_table(lst, url):
    if len(lst) == 0:
        return lst
    else:
        new_list = []

        for word in lst:
            new_list.append(word.replace('< ', '').replace('N/A', '0').replace('> ', ''))

        new_list = [None if word == '0' else int(word) for word in new_list]

        return new_list

def process_modules(lst, url):
    # ['Tier[1]', 'Flight performance[2]', 'Survivability[1]', 'Weaponry[1-4]']
    new_list = [_list[1::] for _list in lst]
    
    if len(new_list[0]) == 4:
        if len(new_list[0]) + len(new_list[1]) + len(new_list[2]) + len(new_list[3]) == 16:
            print('short')
            # TODO for every module check if there is one already in the db
        else:
            write_log(9, 'processing.log', url)
            return []

    elif len(new_list[0]) == 5:
        if len(new_list[0]) + len(new_list[1]) + len(new_list[2]) + len(new_list[3]) == 20:
            print('medium')
            # for every module check if there is one already in the db
        else:
            write_log(9, 'processing.log', url)
            return []

    elif len(new_list[0]) == 6:
        if len(new_list[0]) + len(new_list[1]) + len(new_list[2]) + len(new_list[3]) == 24:
            print('long')
            # for every module check if there is one already in the db
        else:
            write_log(9, 'processing.log', url)
            return []

    elif len(new_list[0]) == 7:
        if len(new_list[0]) + len(new_list[1]) + len(new_list[2]) + len(new_list[3]) == 28:
            print('longest')
            # for every module check if there is one already in the db
        else:
            write_log(9, 'processing.log', url)
            return []
    else:
        write_log(9, 'processing.log', url)
        return []

    return new_list
