from sqlalchemy.sql import text
from db import db

def get_list():
        sql = "SELECT id, restaurant_id, user_id, user_name, title, description, rating, recommendation FROM reviews WHERE visible = TRUE ORDER BY restaurant_id, rating, recommendation"
        result = db.session.execute(text(sql))
        return result.fetchall()

def create(restaurant_id, user_id, user_name, title, description, rating, recommendation):
        sql = "INSERT INTO reviews (restaurant_id, user_id, user_name, title, description, rating, recommendation) VALUES (:restaurant_id, :user_id, :user_name, :title, :description, :rating, :recommendation)"
        db.session.execute(text(sql), {"restaurant_id":restaurant_id, "user_id":user_id, "user_name": user_name, "title":title, "description":description, "rating":rating, "recommendation":recommendation})
        db.session.commit()
        return True

def delete(review_id):
        sql = "UPDATE reviews SET visible = FALSE WHERE id=:id"
        db.session.execute(text(sql), {"id":review_id})
        db.session.commit()
        return True

def restore(review_id):
        sql = "UPDATE reviews SET visible = TRUE WHERE id=:id"
        db.session.execute(text(sql), {"id":review_id})
        db.session.commit()
        return True

def get_review(review_id):
	sql = "SELECT restaurant_id, user_id, user_name, title, description, rating, recommendation FROM reviews WHERE id = :id"
	result = db.session.execute(text(sql), {"id":review_id})
	return result.fetchall()

def get_content(restaurant_id):
        sql = "SELECT restaurant_id, user_id, user_name, title, description, rating, recommendation FROM reviews WHERE restaurant_id = :restaurant_id AND visible = TRUE ORDER BY rating DESC, recommendation"
        result = db.session.execute(text(sql), {"restaurant_id":restaurant_id})
        return result.fetchall()

def get_deleted_entries():
        sql = "SELECT id, restaurant_id, user_id, user_name, title, description, rating, recommendation FROM reviews WHERE visible = FALSE ORDER BY user_id"
        result = db.session.execute(text(sql))
        return result.fetchall()

def get_rating_average(restaurant_id):
	sql = "SELECT SUM(rating) / COUNT (*) FROM reviews WHERE restaurant_id = :restaurant_id AND visible = TRUE" 
	result = db.session.execute(text(sql), {"restaurant_id":restaurant_id})
	return result.fetchone()[0]
