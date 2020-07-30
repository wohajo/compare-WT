from website_startup import db
from models import Planes, PlaneClasses, Engines, Countries, CoolingSystems

def create_database():
    db.create_all()

if __name__ == "__main__":
    create_database()