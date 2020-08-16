def process_general_characteristics(lst):
    if len(lst) == 8:
        lst[2] = lst[2].replace(' Rank', '')
        lst[4] = lst[4].replace('FighterJet fighter', 'jet_fighter')
        lst[5] = lst[5].replace(' people', '').replace(' person', '')
        lst[6] = lst[6].replace(' t', '')
        lst[7] = lst[7].replace(' kg/s', '')
    else:
        lst[2] = lst[2].replace(' Rank', '')
        lst[4] = lst[4].replace('FighterJet fighter', 'jet_fighter') #TODO: this needs to be more specific
        lst[5] = lst[5].replace('people', '').replace('person', '')
        lst[6] = lst[6].replace(' t', '')

    return lst


def process_flight_characteristics(lst):
    pass

def process_defensive_armament(lst):
    pass

def process_offensive_armament(lst):
    pass

def process_suspended_armament(lst):
    pass

def process_economy(lst):
    pass

def process_characteristics_table(lst):
    pass

def process_features_table(lst):
    pass

def process_optimal_velocities_table(lst):
    pass

def process_modules(lst):
    pass
