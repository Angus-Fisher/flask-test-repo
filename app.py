from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from os import environ

# initalise flask app
app = Flask(__name__)

#configure app, handles local dev and environmental variables
app.config['SECRET_KEY'] = environ.get('SECRET_KEY') or 'dev'
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL') or 'sqlite:///my_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# intialise db and login module
db = SQLAlchemy(app)
login = LoginManager(app)
#sets route for unauthenticated users
login.login_view = 'login'

#imports route logic and db models from speerate files
import routes, models

if __name__ == "__main__":
	app.run()
	db.create_all()