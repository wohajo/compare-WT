# constants

SCRAPE_LINKS = [
    'https://wiki.warthunder.com/Category:First_rank_aircraft', 
    'https://wiki.warthunder.com/Category:Second_rank_aircraft', 
    'https://wiki.warthunder.com/Category:Third_rank_aircraft', 
    'https://wiki.warthunder.com/Category:Fourth_rank_aircraft', 
    'https://wiki.warthunder.com/Category:Fifth_rank_aircraft', 
    'https://wiki.warthunder.com/Category:Sixth_rank_aircraft',
    'https://wiki.warthunder.com/Category:First_rank_ground_vehicles',
    'https://wiki.warthunder.com/Category:Second_rank_ground_vehicles',
    'https://wiki.warthunder.com/Category:Third_rank_ground_vehicles',
    'https://wiki.warthunder.com/Category:Fourth_rank_ground_vehicles',
    'https://wiki.warthunder.com/Category:Fifth_rank_ground_vehicles',
    'https://wiki.warthunder.com/Category:Sixth_rank_ground_vehicles',
    'https://wiki.warthunder.com/Category:Seventh_rank_ground_vehicles',
    'https://wiki.warthunder.com/Category:First_rank_ships',
    'https://wiki.warthunder.com/Category:Second_rank_ships',
    'https://wiki.warthunder.com/Category:Third_rank_ships',
    'https://wiki.warthunder.com/Category:Fourth_rank_ships',
    'https://wiki.warthunder.com/Category:Fifth_rank_ships',
    'https://wiki.warthunder.com/Category:Fifth_rank_helicopters',
    'https://wiki.warthunder.com/Category:Sixth_rank_helicopters',
    'https://wiki.warthunder.com/Category:Seventh_rank_helicopters'
    ]

COUNTRIES = ['Great Britain', 'China', 'France', 'Germany', 'Italy',
            'Japan', 'Sweden', 'USA', 'USSR']

WORDS_TO_REMOVE = ['Characteristics', 'Stock', 'Max Speed(km/h at 0 m - sea level)', 
    'Max altitude(metres)', 'Turn time(seconds)', 'Rate of climb(metres/second)', 
    'Take-off run(metres)', 'AB', 'RB', 'Features', 'Combat flaps', 'Take-off flaps', 
    'Landing flaps', 'Air brakes', 'Arrestor gear', 'Drogue chute', 'Optimal velocities (km/h)',
    'Ailerons', 'Rudder', 'Elevators', 'Radiator', 'Tier', 'Flight performance', 'Survivability', 
    'Weaponry']

WORD_TO_REMOVE_PROCESSING =['General characteristics' , 'Offensive armament', 'Flight characteristics',
'Defensive armament', 'Suspended armament', 'Economy']

ROMAN_TO_INTEGER = {"I": 1, "II": 2, "III": 3, "IV": 4, "V": 5, "VI": 6, "VII": 7}

FLIGHT_PERFOMANCE_MODULES = ['Fuselage repair', 'Radiator', 'Compressor', 'Wings repair', 'Engine'
    'Engine injection', 'G-suit', 'New boosters', '95 octane fuel usage']

SURVIVABILITY_MODULES = ['Airframe', 'Cover', 'Protective vest', 'Rear armor plate']

FIGHTER_TYPES = ['Fighter', 'Air Defence fighter', 'Interceptors', 'Jet fighter', 'Naval fighter',
    'Strike fighter']

BOMBER_TYPES = ['Dive bomber', 'Frontline bomber', 'Heavy bomber', 'Jet bombers', 'Light bomber'
    'Long Range bomber', 'Medium bomber', 'Naval bomber', 'Torpedo bomber']