import re
import requests
from helpers import *
from time import sleep
from random import randint
from helpers_planes import *
from bs4 import BeautifulSoup
from constants import SCRAPE_LINKS

def get_vehicles_links(index):
    '''
    Downloads and returns links to vehicles from SCRAPE_LINKS const by index.
    '''

    link_to_remove = 'https://wiki.warthunder.com/User:U16170503'

    url = SCRAPE_LINKS[index]

    html_content = requests.get(url).text

    soup = BeautifulSoup(html_content, "lxml")

    links_list = []

    for link in soup.findAll("div", {"class": "mw-category-group"}):
        for ul in link.findAll("ul"):
            for li in ul.findAll("li"):
                link_to_plane = (li.a.get("href").replace('%27', '\''))
                links_list.append('https://wiki.warthunder.com' + link_to_plane)

    if link_to_remove in links_list: links_list.remove(link_to_remove)
    
    print(('Found {} vehicles!').format(len(links_list)))
    return(links_list)

def get_basic_stats(soup):
    '''
    Returns basic vehicle statistics included in table
    on the right of the webpage in form of a raw list.  
    '''
    tags = soup.select('span[class="ttx-country"], span[class="ttx-rank"], div[class="ttx-title"], span[class="ttx-value"], span[class="ttx-rb ttx-value"], span[class="ttx-value ttx-rb"], span[class="ttx-ab ttx-value"], span[class="ttx-value ttx-ab"], span[class="ttx-sb ttx-value"], span[class="ttx-value ttx-sb"], div[class="ttx-table-line ttx-table-head"]')

    for tag in tags:
        items = [item.text for item in tags if item.text.strip() != '']

    return items

def get_planes_tables(soup, url):
    '''
    Returns informations from plane's tables in form of a list of lists.
    '''

    tables = soup.find_all("table", {"class": "wikitable"})

    # tables[0] is for characteristics
    # these are inconsistent so there is a need for few cases

    # tables[1] is for features
    # features are in following order: ['Combat flaps', 'Take-off flaps', 'Landing flaps', 'Air brakes', 'Arrestor gear', 'Drogue chute']
    
    # tables[3] is for optimal velocities
    # velocities are in following order: ['Ailerons', 'Rudder', 'Elevators', 'Radiator']
    
    # tables[-1] is for modules
    # ['Tier[1]', 'Flight performance[2]', 'Survivability[1]', 'Weaponry[3?]']
    # module tables have 2 cols for weaponry if plane has offensive/suspended armament

    tables_lists = []

    characteristics_with_max_speed = html_table_to_list(tables[0])
    if(characteristics_with_max_speed[0][0] == 'Characteristics'):
        new_characteristics = remove_empty_lists(remove_unwanted_words(characteristics_with_max_speed))
        
        if re.match('(Max Speed.*)', new_characteristics[0][0]):
            del new_characteristics[0]
    else:
        print('Table \'characteristics\' not found! It propably has to be inserted manually')
        write_log(6, 'scrape_data.log', url)
        new_characteristics = []

    tables_lists.append(new_characteristics)
    
    features = html_table_to_list(tables[1])
    if(features[0][0] == 'Features'):
        new_features = remove_empty_lists(remove_unwanted_words(features))
    else:
        print('Table \'features\' not found! It propably has to be inserted manually')
        write_log(7, 'scrape_data.log', url)
        new_features = []

    tables_lists.append(flatten_list(new_features))
    
    velocities = html_table_to_list(tables[3])
    if(velocities[0][0] == 'Optimal velocities (km/h)'):
        new_velocities = remove_empty_lists(remove_unwanted_words(velocities))
    else:
        print('Table \'optimal velocities\' not found! It propably has to be inserted manually')
        write_log(8, 'scrape_data.log', url)
        new_velocities = []

    tables_lists.append(flatten_list(new_velocities))

    modules = html_table_to_list(tables[-1])
    if(modules[0][0] == 'Tier'):
        new_modules = remove_empty_lists(remove_unwanted_words(modules))
    else:
        print('Table \'modules\' not found! It propably has to be inserted manually')
        write_log(9, 'scrape_data.log', url)
        new_modules = []

    tables_lists.append(new_modules)

    return tables_lists

def basic_stats_to_list(items):
    '''
    Downloads basic informations and checks what basic 
    statistics plane has (e.g. defensive or offensive armament). \n 
    Returns a list of correspondingly named lists.
    '''

    basic_stats_list = []

    # burst mass isn't listed in plnaes without offensive armament
    general = items[0:items.index('Flight characteristics')]
    general.remove('General characteristics')
    basic_stats_list.append(general)
    
    flight = items[items.index('Flight characteristics') + 1:items.index('Flight characteristics') + 7]
    basic_stats_list.append(flight)

    off_arm = []
    def_arm = []
    sus_arm = []

    if 'Offensive armament' in items:
        if 'Defensive armament' in items:
            off_arm = crop_list(items, 'Offensive armament', 'Defensive armament')
        elif 'Suspended armament' in items:
            off_arm = crop_list(items, 'Offensive armament', 'Suspended armament')
        else:
            off_arm = crop_list(items, 'Offensive armament', 'Economy')

    if 'Defensive armament' in items:
        if 'Suspended armament' in items:
            def_arm = crop_list(items, 'Defensive armament', 'Suspended armament')
        else:
            def_arm = crop_list(items, 'Defensive armament', 'Economy')
    
    if 'Suspended armament' in items:
        sus_arm = crop_list(items, 'Suspended armament', 'Economy')

    economy_old = items[items.index('Economy') + 1:len(items)]
    economy_new = remove_weird_chars(economy_old)
    
    basic_stats_list.append(off_arm)
    basic_stats_list.append(def_arm)
    basic_stats_list.append(sus_arm)
    basic_stats_list.append(economy_new)

    return basic_stats_list 

def get_plane_full_info(url):
    '''
    Gets plane's info including tables and returns it in a list. \n
    CONTENTS: \n
    1. General characteristics. \n
    2. Flight characteristics. \n
    3. Defensive armament. \n
    4. Offensive armament. \n
    5. Suspended armament. \n
    6. Economy. \n
    7. Characteristics table. \n
    8. Features table. \n
    9. Optimal velocities table. \n
    10. Modules table. \n
    '''
    
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "lxml")

    
    # sleep_time = randint(1,5)
    # print(('Sleeping for {}s').format(sleep_time))
    # sleep(sleep_time)
    basic_stats_list = basic_stats_to_list(get_basic_stats(soup))
    table_stats_list = get_planes_tables(soup, url)
    new_list = basic_stats_list + table_stats_list

    return new_list

def process_plane_full_info(url):
    '''
    Processes plane's full informations to a list ready to be insterted into database.
    '''

    lst = get_plane_full_info(url)

    new_list = []

    new_list.append(process_general_characteristics(lst[0], url))
    new_list.append(process_flight_characteristics(lst[1], url))
    new_list.append(process_defensive_armament(lst[2], url))
    new_list.append(process_offensive_armament(lst[3], url))
    new_list.append(process_suspended_armament(lst[4], url))
    new_list.append(process_economy(lst[5], url))
    new_list.append(process_characteristics_table(lst[6], url))
    new_list.append(process_features_table(lst[7], url))
    new_list.append(process_optimal_velocities_table(lst[8], url))
    new_list.append(process_modules(lst[9], url))

    return new_list

if __name__ == "__main__":
    # process_plane_full_info('https://wiki.warthunder.com/F-4EJ_Phantom_II')
    # process_plane_full_info('https://wiki.warthunder.com/IL-4')
    # process_plane_full_info('https://wiki.warthunder.com/J35D')
    # process_plane_full_info('https://wiki.warthunder.com/IL-2M_(1943)')
    # process_plane_full_info('https://wiki.warthunder.com/B18A')
    # process_plane_full_info('https://wiki.warthunder.com/A6M3')
    process_plane_full_info('https://wiki.warthunder.com/Fury_Mk_II')