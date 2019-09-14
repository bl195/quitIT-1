from flask import Blueprint
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

bp = Blueprint('devices', __name__, url_prefix="/device")
app = Flask(__name__, static_folder='./static')

db = SQLAlchemy(app)
migrate = Migrate(app, db)