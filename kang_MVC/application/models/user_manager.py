from application import db
from schema import *

def add_user(data):
	user = User(
		email = data['email'],
		username = data['username'],
		gender = data['gender'],
		password = db.func.md5(data['password']),
		phone = data['phone'],
		birthday = data['birthday']
	)
	db.session.add(user)
	db.session.commit()

def check_user(email, password):
	return User.query.filter(User.email == email, User.password == db.func.md5(password)).count() != 0

def get_user_filter(email):
	return User.query.filter(User.email == email).all()

def get_user(id):
	return User.query.get(id)
