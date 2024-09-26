from repositories.database import drop_tables, create_tables
from models import Country, City, Location, TargetType, Industry, Target

if __name__ == '__main__':
    create_tables()
    #drop_tables()