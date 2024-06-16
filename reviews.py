from sqlalchemy.sql import text
from db import db

def get_list():
        sql = "SELECT id, restaurant_id, user_id, title, review, rating, recommendation FROM reviews WHERE visible = TRUE ORDER BY restaurant_id, rating, recommendation"
        result = db.session.execute(text(sql))
        return result.fetchall()

def create(restaurant_id, user_id, title, review, rating, recommendation):
        sql = "INSERT INTO reviews (restaurant_id, user_id, title, review, rating, recommendation) VALUES (:restaurant_id, :user_id, :title, :review, :rating, :recommendation)"
        db.session.execute(text(sql), {"restaurant_id":restaurant_id, "user_id":user_id, "title":title, "review":review, "rating":rating, "recommendation":recommendation})
        db.session.commit()
        return True

def delete(id):
        sql = "UPDATE reviews SET visible = FALSE WHERE id=:id"
        db.session.execute(text(sql), {"id":id})
        db.session.commit()
        return True

def restore(id):
        sql = "UPDATE reviews SET visible = TRUE WHERE id=:id"
        db.session.execute(text(sql), {"id":id})
        db.session.commit()
        return True

def get_review(id):
	sql = "SELECT restaurant_id, user_id, title, review, rating, recommendation FROM reviews WHERE id = :id"
	result = db.session.execute(text(sql), {"id":id})
	return result.fetchall()

def get_content(restaurant_id):
        sql = "SELECT restaurant_id, user_id, title, review, rating, recommendation FROM reviews WHERE restaurant_id = :restaurant_id AND visible = TRUE"
        result = db.session.execute(text(sql), {"restaurant_id":restaurant_id})
        return result.fetchall()

def get_deleted_entries():
        sql = "SELECT id, restaurant_id, user_id, title, review, rating, recommendation FROM reviews WHERE visible = FALSE"
        result = db.session.execute(text(sql))
        return result.fetchall()

def get_rating_average(id):
	sql = "SELECT ((COUNT (*))/(COALESCE(SUM(rating), 0))) FROM reviews WHERE restaurant_id = :restaurant_id AND visible = TRUE" 
	result = db.session.execute(text(sql), {"restaurant_id":restaurant_id})
	return result.fetchone()
