from helpers import write_log
from constants import WORD_TO_REMOVE_PROCESSING

def process_general_characteristics(lst, url):
    if any(word in WORD_TO_REMOVE_PROCESSING for word in lst) or len(lst) == 0:
        write_log(0, 'processing.log', url)
        lst = []
        return lst

    if len(lst) == 8:
        lst[2] = lst[2].replace(' Rank', '')
        lst[4] = lst[4].replace('FighterJet fighter', 'jet_fighter')
        lst[5] = lst[5].replace(' people', '').replace(' person', '')
        lst[6] = lst[6].replace(' t', '')
        lst[7] = lst[7].replace(' kg/s', '')
    else:
        lst[2] = lst[2].replace(' Rank', '')
        lst[4] = lst[4].replace('FighterJet fighter', 'jet_fighter') #TODO: this needs to be more specific, there will propably be 3 categories
        lst[5] = lst[5].replace('people', '').replace('person', '')
        lst[6] = lst[6].replace(' t', '')

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
        new_list = []

        for word in lst:
            new_list.append(word.replace(' rounds', '').replace(' shots/min', ''))

        return new_list

def process_offensive_armament(lst, url):
    if any(word in WORD_TO_REMOVE_PROCESSING for word in lst):
        write_log(3, 'processing.log', url)
        lst = []
        return lst
    else:
        new_list = []

        for word in lst:
            new_list.append(word.replace(' rounds', '').replace(' shots/min', ''))

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
        #TODO: Divide min-max repair
        for word in lst:
            new_list.append(word.replace(' %', ''))

        return new_list

def process_characteristics_table(lst, url):
    #TODO: need for few cases
    pass

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
            new_list.append(word.replace('< ', '').replace('N/A', ''))

        return new_list

def process_modules(lst, url):
    pass
