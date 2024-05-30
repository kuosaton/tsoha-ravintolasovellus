from sqlalchemy.sql import text
from db import db

def get_list():
	sql = "SELECT * FROM Restaurants"
	result = db.session.execute(text(sql))
	return result.fetchall()

def create(name, description):
	sql = "INSERT INTO Restaurants (name, description) VALUES (:name, :description)"
	db.session.execute(text(sql), {"name":name, "description":description})
	db.session.commit()
	return True
