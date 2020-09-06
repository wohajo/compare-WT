import re
import time
import random
import requests
from models import *
from helpers import *
from sqlalchemy import exc
from random import randint
from list_modifiers import *
from bs4 import BeautifulSoup
from planes_db_handlers import *
from planes_processing_functions import *
from constants import SCRAPE_LINKS, COUNTRIES


def ask_if_update_links():
    print('Do you want to update links?')
    value = input('y(es)/n(o): \n')

    if value == 'y' or value == 'yes':
        if os.path.exists('planes.txt'):
            print('Removing old vehicle links...')
            os.remove('planes.txt')
            print('Removed!')
        vehicles_links = flatten_list(get_all_vehicles_links_interval(0, 6))
        for vehicle in vehicles_links:
            with open('planes.txt', 'a') as file:
                file.write(vehicle + '\n')
    
    else:
        if os.path.exists('planes.txt'):
            vehicles_links = [line.strip() for line in open('planes.txt', 'r')]
        else:
            print('Vehicle links not found! Downloading new links...')
            vehicles_links = flatten_list(get_all_vehicles_links_interval(0, 6))
            for vehicle in vehicles_links:
                with open('planes.txt', 'a') as file:
                    file.write(vehicle + '\n')
    
    return vehicles_links

def ask_if_start_over():
    vehicles_links = ask_if_update_links()
    
    print('Do you want to start where you left over? \nIf you just updated links it is probably better to start from the beginning.')
    value = input('y(es)/n(o): \n')

    if value == 'y' or value == 'yes':
        if os.path.exists('logs/inserted_planes.log') and os.path.exists('planes.txt'):
            last_line = None

            with open('logs/inserted_planes.log', 'r') as f:
                lines = f.read().splitlines()
                last_line = lines[-1]

            vehicles_links = [line.strip() for line in open('planes.txt', 'r')]
            vehicle_index = vehicles_links.index(last_line)
            return vehicles_links[vehicle_index + 1:]
        else:
            print('No inserted_planes.log or planes.txt file found! Starting from first vehicle...')
            return vehicles_links

    else:
        if os.path.exists('logs/inserted_planes.log'):
            print('Removing old inserted log...')
            os.remove('logs/inserted_planes.log')
            print('Removed!')
        return vehicles_links

def get_vehicles_links(index):
    '''
    Downloads and returns links to vehicles from SCRAPE_LINKS const by index.
    '''

    link_to_remove = 'https://wiki.warthunder.com/User:U16170503'

    url = SCRAPE_LINKS[index]

    try:
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
    except ConnectionError:
        print('Connection error!')
        return []

def get_all_vehicles_links_interval(start, stop):
    '''
    Downloads and returns in form of a list of lists
    links to vehicles from start to stop, based on list SCRAPE_LINKS.
    '''

    vehicles_links_list_tier = []

    for i in range (start, stop):
        time.sleep(random.randint(1, 3))
        vehicles_links_list_tier.append(get_vehicles_links(i))

    return vehicles_links_list_tier

def insert_all_planes_to_database():
    '''
    Adds vehicles from SCRAPE_LINKS (planes). 
    '''
    vehicles_links = ask_if_start_over()
    length = len(vehicles_links)

    current = 0
    start = time.time()
    for vehicle in vehicles_links:
        add_plane_to_db(vehicle)
        current = current + 1
        add_insert_log(vehicle + '\n')
        print(('Added {}/{}').format(current, length))
        sleeping_time = random.randint(1, 3)
        print(('Sleeping for {}s').format(sleeping_time))
        time.sleep(sleeping_time)
        print('-' * 50)

    end = time.time()
    print(('elapsed {}s').format(end - start))

# planes

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
    
    # tables[2] is for limits
    # ['Wings (km/h)', 'Gear (km/h)', 'Flaps (km/h)', 'Max Static G']

    # tables[3] is for optimal velocities
    # velocities are in following order: ['Ailerons', 'Rudder', 'Elevators', 'Radiator']
    
    # tables[-1] is for modules
    # ['Tier[1]', 'Flight performance[2]', 'Survivability[1]', 'Weaponry[3?]']
    # module tables have 2 cols for weaponry if plane has offensive/suspended armament

    tables_lists = []

    if len(tables) == 0:
        return [[], [], [], [], []]

    try:
        characteristics_with_max_speed = html_table_to_list(tables[0])
    except IndexError:
        print('Table \'characteristics\' not found! It propably has to be inserted manually')
        write_log(6, 'scrape_data_planes.log', url)
        new_characteristics = []
    else:
        if(characteristics_with_max_speed[0][0] == 'Characteristics'):
            new_characteristics = remove_empty_lists(remove_unwanted_words(characteristics_with_max_speed))
            
            if re.match('(Max Speed.*)', new_characteristics[0][0]):
                del new_characteristics[0]
        else:
            print('Table \'characteristics\' not found! It propably has to be inserted manually')
            write_log(6, 'scrape_data_planes.log', url)
            new_characteristics = []

    tables_lists.append(new_characteristics)
    
    try:
        features = html_table_to_list(tables[1])
    except IndexError:
        print('Table \'features\' not found! It propably has to be inserted manually')
        write_log(7, 'scrape_data_planes.log', url)
        new_features = []
    else:
        if(features[0][0] == 'Features'):
            new_features = remove_empty_lists(remove_unwanted_words(features))
        else:
            print('Table \'features\' not found! It propably has to be inserted manually')
            write_log(7, 'scrape_data_planes.log', url)
            new_features = []

    tables_lists.append(flatten_list(new_features))

    try:
        limits = html_table_to_list(tables[2])
    except IndexError:
        print('Table \'limits\' not found! It propably has to be inserted manually')
        write_log(8, 'scrape_data_planes.log', url)
        new_limits = []
    else:
        if(limits[0][0] == 'Limits' and len(limits[-1]) == 7):
            new_limits = flatten_list(remove_empty_lists(remove_unwanted_words(limits)))
            new_limits.remove('Limits')
        else:
            print('Table \'limits\' not found! It propably has to be inserted manually')
            write_log(8, 'scrape_data_planes.log', url)
            new_limits = []

    tables_lists.append(new_limits)
    
    try:
        velocities = html_table_to_list(tables[3])
    except IndexError:
        print('Table \'optimal velocities\' not found! It propably has to be inserted manually')
        write_log(9, 'scrape_data_planes.log', url)
        new_velocities = []
    else:
        if(velocities[0][0] == 'Optimal velocities (km/h)'):
            new_velocities = remove_empty_lists(remove_unwanted_words(velocities))
        else:
            print('Table \'optimal velocities\' not found! It propably has to be inserted manually')
            write_log(9, 'scrape_data_planes.log', url)
            new_velocities = []

    tables_lists.append(flatten_list(new_velocities))

    try:
        modules = html_table_to_list(tables[-1])
    except IndexError:
        print('Table \'modules\' not found! It propably has to be inserted manually')
        write_log(10, 'scrape_data_planes.log', url)
        new_modules = []
    else:
        if(modules[0][0] == 'Tier'):
            new_modules = remove_empty_lists(remove_unwanted_words(modules))
        else:
            print('Table \'modules\' not found! It propably has to be inserted manually')
            write_log(10, 'scrape_data_planes.log', url)
            new_modules = []

    tables_lists.append(new_modules)

    return tables_lists

def get_vehicle_img_link(soup):
    '''
    Returns vehicle\'s title image link.
    ''' 
    div_tag = soup.find('div', {'class': 'ttx-image'})
    text = []

    img_tag = div_tag.find("img", recursive=False)

    if img_tag is None:
        text.append('')
    else:
        print((img_tag['src']))
        text.append(img_tag['src'])

    return text

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
    9. Limits table. \n
    10. Optimal velocities table. \n
    11. Modules table. \n
    12. Title image.
    '''
    
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "lxml")

    basic_stats_list = basic_stats_to_list(get_basic_stats(soup))
    table_stats_list = get_planes_tables(soup, url)
    title_image = get_vehicle_img_link(soup)
    new_list = basic_stats_list + table_stats_list + title_image

    return new_list

def process_plane_full_info(url):
    '''
    Processes plane's full informations to a list ready to be insterted into database.
    '''

    lst = get_plane_full_info(url)

    new_list = []

    new_list.append(process_general_characteristics(lst[0], url))
    new_list.append(process_flight_characteristics(lst[1], url))
    new_list.append(process_offensive_armament(lst[2], url))
    new_list.append(process_defensive_armament(lst[3], url))
    new_list.append(process_suspended_armament(lst[4], url))
    new_list.append(process_economy(lst[5], url))
    new_list.append(process_characteristics_table(lst[6], url))
    new_list.append(process_features_table(lst[7], url))
    new_list.append(process_limits_table(lst[8], url))
    new_list.append(process_optimal_velocities_table(lst[9], url))
    new_list.append(process_modules(lst[10], url))
    new_list.append(lst[11])

    return new_list

def add_plane_to_db(url):
    try:
        plane_list = process_plane_full_info(url)

        country_in_link = [country for country in COUNTRIES if country in url]

        if len(country_in_link) != 0:
            plane_list[0][0] = plane_list[0][0][1:] + ' (' + country_in_link[0] + ')' 

        if plane_list[0][1] == 'Britain':
            plane_list[0][1] = 'Great_Britain'

        plane = None
        # 1st row

        if len(plane_list[0]) == 0:
            write_log('plane_adding', 'db_adding_planes.log', url)
            return None
        else:
            plane = Plane(name=plane_list[0][0], img_link=plane_list[11])
            add_general_characteristics(plane, plane_list[0], url)

        # 2nd row
        add_engine_and_sod_to_plane(plane, plane_list[1], url)
        # 3rd row
        db.session.add(plane)
        db.session.flush()
        # to get plane's id
        add_weapons_to_plane(plane, False, plane_list[2], url)
        # 4th row
        add_weapons_to_plane(plane, True, plane_list[3], url)
        # 5th row
        add_suspended_armament_to_plane(plane, plane_list[4], url)
        # 6th row
        add_economy_to_plane(plane, plane_list[5], url)
        # 7th row
        add_characteristics_to_plane(plane, plane_list[6], url)
        # 8th row
        add_features_to_plane(plane, plane_list[7], url)
        # 9th row
        add_flaps_sods_to_plane(plane, plane_list[8], url)
        # 10th row
        add_optimal_velocities_to_plane(plane, plane_list[9], url)
        # 11st row
        add_modules_to_plane(plane, plane_list[10], url)
        # end of rows
        db.session.commit()
        print('added ' + url)

    except exc.IntegrityError:
        print('Error: object already in database! ' + url)
        print('-' * 50)
        db.session.rollback()

if __name__ == "__main__":
    insert_all_planes_to_database()