from website_startup import db
from models import Plane, PlaneClass, Engine, Country, CoolingSystem

def create_database():
    db.create_all()
    # initiate countires

if __name__ == "__main__":
    # create_database()
    # engine = Engine(name = 'Swiromsky 6B')
    # db.session.add(engine)
    # db.session.commit()
    # engines = Engine.query.all()
    # print(engines[2].name)