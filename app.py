from repositories.database import drop_tables, create_tables
from models import Country, City, Location, TargetType, Industry, Target
from flask import Flask
from controllers.target_controller import target_bp


app = Flask(__name__)


if __name__ == '__main__':
    #create_tables()
    # drop_tables()
    app.register_blueprint(target_bp, url_prefix="/api/targets")
    app.run(debug=True)
