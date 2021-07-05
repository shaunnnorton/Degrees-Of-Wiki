from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

load_dotenv()

app = Flask(__name__)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["SQLALCHEMY_DATABASE_URI"]
app.secret_key = os.urandom(24)


db = SQLAlchemy(app)

from src.main.routes import main
app.register_blueprint(main)

with app.app_context():
    db.create_all()
