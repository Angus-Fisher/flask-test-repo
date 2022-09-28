from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


#User model for use in login/session mgmt including setting and hashing passwords
class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(100), index=True, unique=True)
	email = db.Column(db.String(140), index=True, unique=True)
	#does this store unhashed pws? need to delete
	password = db.Column(db.String(100), index=False, unique=False)
	password_hash = db.Column(db.String(150), index=False, unique=False)
	expenses = db.relationship('Expense', backref='expenses', lazy='dynamic')

	def __repr__(self):
		return '<User {}>'.format(self.username)

	def set_password(self, password):
  		self.password_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)

	@login.user_loader
	def load_user(id):
		return User.query.get(int(id))

#Expense model stores expenses of users
class Expense(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(100),index=True, primary_key=False)
	amount = db.Column(db.Integer,index = True, primary_key = False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

	def __repr__(self):
		return '<{} expense>'.format(self.name)



