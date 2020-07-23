# libraries
from bs4 import BeautifulSoup
import requests

#TODO make dict with every type of vehicle and write it to a file

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

    html_content = requests.get(url).text

    soup = BeautifulSoup(html_content, "lxml")

    # for link in soup.find("div", {"class": "ttx-title"}):
    #     print(link.text, end = print('=' * 10))

    # for link in soup.find("span", {"class": "ttx-rank"}):
    #     print(link.text, end = print('=' * 10))

    # for link in soup.find_all("span", {"class": "ttx-name"}):
    #     print(link.text, end = print('=' * 10))

    # for link in soup.find_all("span", {"class": "ttx-value"}):
    #     print(link.text, end = print('=' * 10))

    for link in soup.select('span[class="ttx-value"], span[class="ttx-rb ttx-value"], span[class="ttx-value ttx-rb"], span[class^="ttx-name"]'):
        print(link.text, end = print('=' * 10))

    # for link in soup.find_all("div", {"class": "ttx-table-line"}):
    #     print(link.text, end = print('=' * 10 + '\n'))

if __name__ == "__main__":
    # get_vehicles_links()
    get_basic_vehicle_stats('https://wiki.warthunder.com/J35D')