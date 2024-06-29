from sqlalchemy.sql import text
from db import db

def get_list():
        sql = "SELECT id, restaurant_id, creator_id, creator_name, title, description, rating, recommendation FROM reviews WHERE visible = TRUE ORDER BY restaurant_id, rating, recommendation"
        result = db.session.execute(text(sql))
        return result.fetchall()

def create(restaurant_id, creator_id, creator_name, title, description, rating, recommendation):
        sql = "INSERT INTO reviews (restaurant_id, creator_id, creator_name, title, description, rating, recommendation) VALUES (:restaurant_id, :creator_id, :creator_name, :title, :description, :rating, :recommendation)"
        db.session.execute(text(sql), {"restaurant_id":restaurant_id, "creator_id":creator_id, "creator_name": creator_name, "title":title, "description":description, "rating":rating, "recommendation":recommendation})
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

def get_content(review_id):
	sql = "SELECT restaurant_id, creator_id, creator_name, title, description, rating, recommendation FROM reviews WHERE id = :id"
	result = db.session.execute(text(sql), {"id":review_id})
	return result.fetchall()

def get_restaurant_reviews(restaurant_id):
        sql = "SELECT restaurant_id, creator_id, creator_name, title, description, rating, recommendation FROM reviews WHERE restaurant_id = :restaurant_id AND visible = TRUE ORDER BY rating DESC, recommendation"
        result = db.session.execute(text(sql), {"restaurant_id":restaurant_id})
        return result.fetchall()

def get_deleted_entries():
        sql = "SELECT id, restaurant_id, creator_id, creator_name, title, description, rating, recommendation FROM reviews WHERE visible = FALSE ORDER BY creator_id"
        result = db.session.execute(text(sql))
        return result.fetchall()

def get_rating_average(restaurant_id):
	sql = "SELECT SUM(rating) / COUNT (*) FROM reviews WHERE restaurant_id = :restaurant_id AND visible = TRUE" 
	result = db.session.execute(text(sql), {"restaurant_id":restaurant_id})
	return result.fetchone()[0]

def get_reviews_made_by_user(creator_id):
	sql = "SELECT restaurant_id, creator_name, title, description, rating, recommendation FROM reviews WHERE visible = TRUE AND creator_id = :creator_id ORDER BY rating DESC, recommendation"
	result = db.session.execute(text(sql), {"creator_id":creator_id})
	return result.fetchall()
