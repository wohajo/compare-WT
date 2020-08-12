from website_startup import db
from constants import COUNTRIES
from models import Plane, PlaneClass, Engine, Country, CoolingSystem

def create_database():
    db.create_all()
    
    countries = [
        Country(name=COUNTRIES[0]),
        Country(name=COUNTRIES[1]),
        Country(name=COUNTRIES[2]),
        Country(name=COUNTRIES[3]),
        Country(name=COUNTRIES[4]),
        Country(name=COUNTRIES[5]),
        Country(name=COUNTRIES[6]),
        Country(name=COUNTRIES[7]),
        Country(name=COUNTRIES[8]),
    ]

    db.session.bulk_save_objects(countries)
    db.session.commit()

if __name__ == "__main__":
    create_database()