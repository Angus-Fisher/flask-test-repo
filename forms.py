from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, validators

class ExpenseForm(FlaskForm):
	name = StringField("Name",[validators.DataRequired()])
	amount = IntegerField("Amount EUR",[validators.DataRequired()])
	submit = SubmitField("Add Expense")

class LoginForm(FlaskForm):
	username = StringField("Username", [validators.DataRequired()])
	password = StringField("Password", [validators.DataRequired()])
	submit = SubmitField("Login")

class SignupForm(FlaskForm):
	username = StringField("Username", [validators.DataRequired()])
	password = StringField("Password", [validators.DataRequired()])
	email = StringField("Email", [validators.DataRequired()])
	submit = SubmitField("Login")