import os
from config import login_manager, app, db
from werkzeug.security import generate_password_hash, check_password_hash

# Modelo User
class User(db.Model):
	# Nome da tabela de usuários no banco
	__tablename__ = 'users'
	# Atributos do modelo
	id = db.Column('id', db.Integer, primary_key = True)
	username = db.Column('username', db.String(18), unique = True, index = True)
	password = db.Column('password', db.String(20))
	email = db.Column('email', db.String(100), unique = True, index = True)


	def __init__(self, username, password, email):
		self.username = username
		self.setPassword(password)
		self.email    = email

	def setPassword(self, password):
		self.password = generate_password_hash(password)

	def checkPassword(self, password):
		return check_password_hash(self.password, password)

	def is_authenticated(self):
		return True
	
	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def get_id(self):
		return unicode(self.id)

	def __repr__(self):
		return '<User $r>' % (self.username)
