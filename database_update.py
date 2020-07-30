from bs4 import BeautifulSoup
from flask_sqlalchemy import SQLAlchemy
import requests


scrape_links = [
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

def get_vehicles_links():

    url = scrape_links[0]

    html_content = requests.get(url).text

    soup = BeautifulSoup(html_content, "lxml")

    for link in soup.findAll("div", {"class": "mw-category-group"}):
        for li in link.findAll("li"):
            print(li.a.get("href"))

def get_basic_vehicle_stats(url):
    '''
    Returns basic vehicle statistics included in table
    on the right of the webpage in form of a raw list.  
    '''
    html_content = requests.get(url).text

    soup = BeautifulSoup(html_content, "lxml")
    tags = soup.select('span[class="ttx-country"], span[class="ttx-rank"], div[class="ttx-title"], span[class="ttx-value"], span[class="ttx-rb ttx-value"], span[class="ttx-value ttx-rb"], div[class="ttx-table-line ttx-table-head"]')

    for tag in tags:
        items = [item.text for item in tags if item.text.strip() != '']

    # print('\n'.join(items))
    print(items)

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
    [IN PROGRESS] Returns basic plane info in better form (object?).
    '''

if __name__ == "__main__":
    get_basic_vehicle_stats('https://wiki.warthunder.com/J35D')