from sqlalchemy.sql import text
from db import db

def get_list():
	sql = "SELECT id, name, description, category, address, business_hours, entry_type FROM restaurants WHERE visible = TRUE ORDER BY entry_type, name"
	result = db.session.execute(text(sql))
	return result.fetchall()

def create(name, description, category, address, business_hours, entry_type):
	sql = "INSERT INTO restaurants (name, description, category, address, business_hours, entry_type) VALUES (:name, :description, :category, :address, :business_hours, :entry_type) RETURNING id"
	restaurant_id = db.session.execute(text(sql), {"name":name, "description":description, "category":category, "address":address, "business_hours":business_hours, "entry_type":entry_type}).fetchone()[0]
	db.session.commit()
	return restaurant_id

def delete(id):
	sql = "UPDATE restaurants SET visible = FALSE WHERE id=:id"
	db.session.execute(text(sql), {"id":id})
	db.session.commit()
	return True

def restore(id):
	sql = "UPDATE restaurants SET visible = TRUE WHERE id=:id"
	db.session.execute(text(sql), {"id":id})
	db.session.commit()
	return True

def get_content(id):
	sql = "SELECT name, description, category, address, business_hours, entry_type FROM restaurants WHERE id = :id"
	result = db.session.execute(text(sql), {"id":id})
	return result.fetchall()

def get_deleted_entries():
	sql = "SELECT id, name, description, category, address, business_hours, entry_type FROM restaurants WHERE visible = FALSE"
	result = db.session.execute(text(sql))
	return result.fetchall()

def search(query):
	sql = """
	SELECT
		id, name, description, category, address, business_hours, entry_type
 	FROM
		restaurants
	WHERE
		visible = TRUE
	AND
		(
		lower(name) LIKE lower(:query)
	OR
		lower(description) LIKE lower(:query)
	OR
		lower(category) LIKE lower(:query)
		)
	"""
	result = db.session.execute(text(sql), {"query":"%"+query+"%"})
	return result.fetchall()

