from app import app, db
from flask import render_template, request, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required
from models import Expense, User
from forms import ExpenseForm, LoginForm, SignupForm


@app.route("/signup", methods=["GET","POST"])
def signup():

	#checks if already authenticated, then sends to index
	if current_user.is_authenticated:
		flash("already signed in", "notice")
		return redirect(url_for("index"))

	form = SignupForm()

	if form.validate_on_submit():
		#initalise temp user and hash password
		user = User(username = form.username.data, email =  form.email.data)
		user.set_password(form.password.data)
		db.session.add(user)
		#try creating user in db
		try:
			db.session.commit()
		#if it fails, assume uniqueness error
		except:
			db.session.rollback()
			flash("Username or email already in use", "warning")
			return redirect(url_for('signup'))
		#login newly created user and redirect to index
		login_user(user)
		return redirect(url_for('index'))


	return render_template('signup.html', form = form)

@app.route('/', methods=["GET","POST"])
@login_required
def index():
	print('rendering')
	if request.method == 'POST':
		print('in the if')
		db.session.add(Expense(name = request.form['name'],amount = request.form['amount']))
		db.session.commit()
	return render_template('index.html',expenses=Expense.query.all(), template_form=ExpenseForm())


@app.route('/login', methods=["GET", "POST"])
def login():
	print('rendering login')

	#checks if already authenticated, then sends to index
	if current_user.is_authenticated:
		return redirect(url_for("index"))

	form = LoginForm()

	#On form submission, check if username in db, then check password matches and login
	if form.validate_on_submit():
		user = User.query.filter_by(username = form.username.data).first()
		if user is None:
			flash("Invalid email", "warning")
			return redirect(url_for("login"))
		if not user.check_password(form.password.data):
			flash("wrong password bebeh", "warning")
			return redirect(url_for("login"))
		else:
			login_user(user)
			return redirect(url_for("index"))

	return render_template('login.html', form = form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("login"))

