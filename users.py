import os
from db import db
from flask import abort, request, session
from werkzeug.security import check_password_hash, generate_password_hash

def login(name, password):
	sql = "SELECT password, id, seclevel FROM users WHERE name = :name"
	result = db.session.execute(text(sql), {"name":name})
	user = result.fetchone()

	if not user:
		return False
	if not check_password_hash(user[0], password):
		return False

	session["user_id"] = user[1]
	session["user_name"] = name
	session["user_seclevel"] = user[2]
	session["csrf_token"] = os.urandom(16).hex()

	return True

def logout():
	del session["user_id"]
	del session["user_name"]
	del session["user_seclevel"]

def register(name, password, seclevel):
	hashVal = generate_password_hash(password)
	try:
		sql = """INSERT INTO users (name, password, seclevel) VALUES (:name, :password, :seclevel)"""
		db.session.execute(sql, {"name":name, "password":hashVal, "seclevel":seclevel})
		db.session.commit()
	except:
		return False

	return login(name, password)

def get_user_id():
	return session.get("user_id", 0)

def verify_seclevel(seclevel):
	if seclevel > session.get("user_seclevel", 0):
		abort(403)

def verify_csrf():
	if session["csrf_token"] != request.form["csrf_token"]:
		abort(403)
