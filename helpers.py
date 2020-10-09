import os
from datetime import datetime
from constants import WORDS_TO_REMOVE, ROMAN_TO_INTEGER


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

def roman_to_int(roman):
    roman_list = list(roman)

    result = 0
    current_idx = None
    current_value = None
    next_idx = None
    next_value = None

    for i in range(0, len(roman_list)):
        current_idx = roman_list[i]
        current_value = ROMAN_TO_INTEGER[current_idx]

        if i == len(roman_list) - 1:
            result = result + current_value
            return result 

        next_idx = roman_list[i + 1]
        next_value = ROMAN_TO_INTEGER[next_idx]

        if current_value < next_value:
            result = result - current_value
        elif next_idx == None:
            return result
        else:
            result = result + current_value

    return result

def int_to_roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
        ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
        ]
    roman_num = ''
    i = 0
    while  num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num

def add_insert_log(url):
    with open('logs/inserted_planes.log', 'a') as file:
        file.write(url)

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
    8: Limits table \n
    9: Optimal velocities table \n
    10: Engine info table \n
    11: Modules table \n
    12: Adding plane \n
    '''

    if code == 6:
        code = 'characteristics_table'
    elif code == 7:
        code = 'features_table'
    elif code == 8:
        code = 'limits_table'
    elif code == 9:
        code = 'optimal_velocities_table'
    elif code == 10:
        code = 'engine_info_table'
    elif code == 11:
        code = 'modules_table'

    with open('logs/' + filename, 'a') as file:
            file.write(('{}, Error_codename:{}, vehicle:{} \n').format(datetime.now(), code, url))