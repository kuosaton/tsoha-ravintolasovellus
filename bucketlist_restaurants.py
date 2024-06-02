from sqlalchemy.sql import text
from db import db

def get_list():
        sql = "SELECT * FROM bucketlist_restaurants"
        result = db.session.execute(text(sql))
        return result.fetchall()

def create(name, description, category, address):
        sql = "INSERT INTO bucketlist_restaurants (name, description, category, address) VALUES (:name, :description, :category, :address)"
        db.session.execute(text(sql), {"name":name, "description":description, "category":category, "address":address})
        db.session.commit()
        return True

def get_content(id):
       sql = "SELECT * FROM bucketlist_restaurants WHERE id = :id"
       result = db.session.execute(text(sql), {"id":id})
       return result.fetchall()

def search(query):
        sql = """
	SELECT
		* FROM bucketlist_restaurants
	WHERE
		lower(name) LIKE :query
	OR
		lower(description) LIKE :query
	OR
		lower(category) LIKE :query
	OR
		lower(address) LIKE :query
	"""
        result = db.session.execute(text(sql), {"query":"%"+query+"%"})
        return result.fetchall()
