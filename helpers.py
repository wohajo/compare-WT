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

def write_scrape_log(table, url):
    with open("scrape_data.log", 'a') as file:
            file.write(('Table_error:{}, vehicle:{} \n').format(table, url))