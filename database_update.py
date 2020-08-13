from bs4 import BeautifulSoup
from constants import SCRAPE_LINKS
from helpers import crop_list, remove_weird_chars, html_table_to_list, remove_empty_lists, remove_unwanted_words
import requests

def get_vehicles_links(index):
    '''
    Downloads and prints links to vehicles from SCRAPE_LINKS const by index.
    '''

    # TODO: fix link not having "'"

    url = SCRAPE_LINKS[index]

    html_content = requests.get(url).text

    soup = BeautifulSoup(html_content, "lxml")

    counter = 0

    for link in soup.findAll("div", {"class": "mw-category-group"}):
        for ul in link.findAll("ul"):
            for li in ul.findAll("li"):
                print((li.a.get("href").replace('&27s', '\'')))
                counter = counter + 1
    
    print(counter)

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

    #TODO: cleanup tables

    html_content = requests.get(url).text

    soup = BeautifulSoup(html_content, "lxml")
    tables = soup.find_all("table", {"class": "wikitable"})

    # tables[0] is for characteristics
    # tables[1] is for features
    # tables[3] is for optimal velocities
    # tables[-1] is for modules

    # module tables have 2 cols for weaponry if plane has offensive/suspended armament  
    # additionaly premium planes have one row more, which should be dumped

    characteristics = html_table_to_list(tables[0])
    remove_empty_lists(remove_unwanted_words(characteristics))
    
    # features = html_table_to_list(tables[1])
    # remove_empty_lists(remove_unwanted_words(features))
    
    # characteristics = html_table_to_list(tables[0])
    # remove_empty_lists(remove_unwanted_words(characteristics))

    # characteristics = html_table_to_list(tables[0])
    # remove_empty_lists(remove_unwanted_words(characteristics))

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

    def_arm = []
    if 'Defensive armament' in items:
        if 'Offensive armament' in items:
            def_arm = crop_list(items, 'Defensive armament', 'Offensive armament')
        else:
            def_arm = crop_list(items, 'Defensive armament', 'Suspended armament')
    basic_stats_list.append(def_arm)
    
    off_arm = []
    if 'Offensive armament' in items:
        if 'Suspended armament' in items:
            off_arm = crop_list(items, 'Offensive armament', 'Suspended armament')
        else:
            off_arm = crop_list(items, 'Offensive armament', 'Economy')
    basic_stats_list.append(off_arm)
    
    sus_arm = []
    if 'Suspended armament' in items:
        sus_arm = crop_list(items, 'Suspended armament', 'Economy')
    basic_stats_list.append(sus_arm)

    economy_old = items[items.index('Economy') + 1:len(items)]
    economy_new = remove_weird_chars(economy_old)
    basic_stats_list.append(economy_new)

    return basic_stats_list #TODO cast to db 

if __name__ == "__main__":
    # print(basic_stats_to_list(get_basic_stats('https://wiki.warthunder.com/IL-2M_(1943)')), '\n')
    # print(basic_stats_to_list(get_basic_stats('https://wiki.warthunder.com/Pe-8')), '\n')
    # print(basic_stats_to_list(get_basic_stats('https://wiki.warthunder.com/J35D')), '\n')
    get_planes_tables('https://wiki.warthunder.com/J35D')
    # get_planes_tables('https://wiki.warthunder.com/XP-50')
    # get_vehicles_links(0)
