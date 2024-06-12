from sqlalchemy.sql import text
from db import db

def get_list():
        sql = "SELECT * FROM bucketlist_restaurants WHERE visible = TRUE"
        result = db.session.execute(text(sql))
        return result.fetchall()

def create(name, description, category, address):
        sql = "INSERT INTO bucketlist_restaurants (name, description, category, address) VALUES (:name, :description, :category, :address)"
        db.session.execute(text(sql), {"name":name, "description":description, "category":category, "address":address})
        db.session.commit()
        return True

def delete(id):
	sql = "UPDATE bucketlist_restaurants SET visible=FALSE WHERE id = :id"
	db.session.execute(text(sql), {"id":id})
	db.session.commit()
	return True

def restore(id):
	sql = "UPDATE bucketlist_restaurants SET visible=TRUE WHERE id = :id"
	db.session.execute(text(sql), {"id":id})
	db.session.commit()
	return True

def get_content(id):
	sql = "SELECT * FROM bucketlist_restaurants WHERE id = :id"
	result = db.session.execute(text(sql), {"id":id})
	return result.fetchall()

def get_deleted_entries():
        sql = "SELECT * FROM bucketlist_restaurants WHERE visible=FALSE"
        result = db.session.execute(text(sql))
        return result.fetchall()

def search(query):
        sql = """
	SELECT
		* FROM bucketlist_restaurants
	WHERE
		visible = TRUE
	AND 
		(
		lower(name) LIKE lower(:query)
	OR
		lower(description) LIKE lower(:query)
	OR
		lower(category) LIKE lower(:query)
	OR
		lower(address) LIKE lower(:query)
		)
	"""
        result = db.session.execute(text(sql), {"query":"%"+query+"%"})
        return result.fetchall()
