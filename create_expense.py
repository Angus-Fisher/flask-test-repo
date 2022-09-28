from app import db
from models import Expense, User
from werkzeug.security import generate_password_hash

db.create_all()

user1 = User(username = 'superuser',email = 'test@test.com', password = '', password_hash = generate_password_hash('test123'))
db.session.add(user1)
user1 = User.query.filter_by(username = 'superuser').first()
expense1 = Expense(name = 'test expense',amount = '1234', user_id = user1.id)
db.session.add(expense1)
db.session.commit()


