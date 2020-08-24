import os
from datetime import datetime
from constants import WORDS_TO_REMOVE

def crop_list(list, start, end):
    '''
    Returns list containing items cropped from starting string to ending string. 
    '''

    start = list.index(start) + 1
    end = list.index(end)

    return list[start:end]

def remove_weird_chars(lst):
    '''
    Returns list without trailing spaces and unnecessary characters.
    '''

    new_list = []

    for item in lst:
        new_list.append(item.strip().replace(u'\xa0', ' '))

    return new_list

def html_table_to_list(table):
    '''
    Converts given HTML table with header and sub-header to a list of lists and returns it.
    '''       
    
    rows = []
    trs = table.find_all('tr')
    header_row = [td.get_text(strip = True) for td in trs[0].find_all('th')]
    sub_header_row = ([td.get_text(strip = True) for td in trs[1].find_all('th')])
    
    if header_row:
        rows.append(header_row)
        rows.append(sub_header_row)
        trs = trs[0:]

    for tr in trs:
        rows.append([td.get_text(strip = True) for td in tr.find_all('td')])

    return rows

def remove_empty_lists(lst):
    '''
    Removes empty lists from list and returns a cleaned up copy.
    '''
    
    new_list = list(filter(lambda x: x, lst))

    return new_list

def remove_unwanted_words(lst):
    '''
    Removes unwanted words from list and returns a new copy.
    '''

    new_list = [list(filter(lambda w: w not in WORDS_TO_REMOVE, sublist)) for sublist in lst]

    return new_list

def flatten_list(lst):
    '''
    Flattens 2D list to 1D and returns it.
    '''

    flattened_list = [y for x in lst for y in x]

    return flattened_list

def write_log(code, filename, url):

    '''
    Error codes: \n
    0: General characteristics \n
    1: Flight characteristics \n
    2: Defensive armament \n
    3: Offensive armament \n
    4: Suspended armament \n
    5: Economy \n
    6: Characteristics table \n
    7: Features table \n
    8: Optimal velocities table \n
    9: Modules table \n
    '''

    if code == 6:
        code = 'characteristics_table'
    elif code == 7:
        code = 'features_table'
    elif code == 8:
        code = 'optimal_velocities_table'
    elif code == 9:
        code = 'modules_table'

    with open(filename, 'a') as file:
            file.write(('{}, Error_codename:{}, vehicle:{} \n').format(datetime.now(), code, url))