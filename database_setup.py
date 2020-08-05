from website_startup import db
from models import Plane, PlaneClass, Engine, Country, CoolingSystem

def create_database():
    db.create_all()

if __name__ == "__main__":
    create_database()