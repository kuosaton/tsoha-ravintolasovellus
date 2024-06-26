import os
from db import db
from flask import abort, request, session
from sqlalchemy.sql import text
from werkzeug.security import check_password_hash, generate_password_hash

def login(username, password):
	sql = "SELECT password, id, seclevel FROM users WHERE username=:username"
	result = db.session.execute(text(sql), {"username":username})
	user = result.fetchone()

	if not user:
		return False
	if not check_password_hash(user[0], password):
		return False

	session["user_id"] = user[1]
	session["user_name"] = username
	session["user_seclevel"] = user[2]
	session["csrf_token"] = os.urandom(16).hex()

	return True

def logout():
	del session["user_id"]
	del session["user_name"]
	del session["user_seclevel"]

def register(username, password, seclevel):
	hash = generate_password_hash(password)

	try:
		sql = "INSERT INTO users (username, password, seclevel) VALUES (:username, :password, :seclevel)"
		db.session.execute(text(sql), {"username":username, "password":hash, "seclevel":seclevel})
		db.session.commit()
	except:
		return False

	return login(username, password)

def check_seclevel(seclevel):
	if seclevel > session.get("user_seclevel", 0):
		abort(403)

def check_csrf():
	if session["csrf_token"] != request.form["csrf_token"]:
		abort(403)

def get_id():
	return session.get("user_id")

def get_name():
	return session.get("user_name")
