from bs4 import BeautifulSoup
from flask_sqlalchemy import SQLAlchemy
from constants import SCRAPE_LINKS
from helpers import crop_list, remove_weird_chars
import requests

def get_vehicles_links(index):
    '''
    Downloads and prints links to vehicles from SCRAPE_LINKS const by index.
    '''

    url = SCRAPE_LINKS[index]

    html_content = requests.get(url).text

    soup = BeautifulSoup(html_content, "lxml")

    for link in soup.findAll("div", {"class": "mw-category-group"}):
        for li in link.findAll("li"):
            print(li.a.get("href"))

def get_basic_stats(url):
    '''
    Returns basic vehicle statistics included in table
    on the right of the webpage in form of a raw list.  
    '''
    
    html_content = requests.get(url).text

    soup = BeautifulSoup(html_content, "lxml")
    tags = soup.select('span[class="ttx-country"], span[class="ttx-rank"], div[class="ttx-title"], span[class="ttx-value"], span[class="ttx-rb ttx-value"], span[class="ttx-value ttx-rb"], div[class="ttx-table-line ttx-table-head"]')

    for tag in tags:
        items = [item.text for item in tags if item.text.strip() != '']

    return items

def get_planes_tables(url):
    '''
    [IN PROGRESS] Prints all tables from the webpage.
    '''

    html_content = requests.get(url).text

    soup = BeautifulSoup(html_content, "lxml")
    tables = soup.find_all("table", {"class": "wikitable"})

    # tables[0] is for characteristics
    # tables[1] is for features
    # tables[3] is for optimal velocities
    # tables[-1] is for modules

    print(tables[1].text)

def basic_stats_to_list(items):
    '''
    Downloads basic informations and checks what basic 
    statistics plane has (e.g. defensive or offensive armament). \n 
    Returns a list of correspondingly named lists.
    '''

    basic_stats_list = []

    # burst mass isn't listed in plnaes without offensive armament
    general = items[0:items.index('Flight characteristics')] #TODO: 8th place is here only if the plane have offensive armament
    general.remove('General characteristics')
    basic_stats_list.append(general)
    
    flight = items[items.index('Flight characteristics') + 1:items.index('Flight characteristics') + 7]
    basic_stats_list.append(flight)

    if 'Defensive armament' in items:
        if 'Offensive armament' in items:
            def_arm = crop_list(items, 'Defensive armament', 'Offensive armament')
        else:
            def_arm = crop_list(items, 'Defensive armament', 'Suspended armament')
        basic_stats_list.append(def_arm)
    if 'Offensive armament' in items:
        if 'Suspended armament' in items:
            off_arm = crop_list(items, 'Offensive armament', 'Suspended armament')
        else:
            off_arm = crop_list(items, 'Offensive armament', 'Economy')
        basic_stats_list.append(off_arm)
    if 'Suspended armament' in items:
        sus_arm = crop_list(items, 'Suspended armament', 'Economy')
        basic_stats_list.append(sus_arm)

    economy_old = items[items.index('Economy') + 1:len(items)]
    economy_new = remove_weird_chars(economy_old)
    basic_stats_list.append(economy_new)

    return basic_stats_list #TODO cast to db 

if __name__ == "__main__":
    items = get_basic_stats('https://wiki.warthunder.com/IL-2M_(1943)')
    print(basic_stats_to_list(items))
    # get_basic_vehicle_stats('https://wiki.warthunder.com/IL-2_(1942)')
    #g et_basic_vehicle_stats('https://wiki.warthunder.com/Pe-8')
