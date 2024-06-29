from sqlalchemy.sql import text
from db import db

def get_all():
        sql = "SELECT id, restaurant_id, creator_id, content FROM questions WHERE visible = TRUE ORDER BY restaurant_id, creator_id"
        result = db.session.execute(text(sql))
        return result.fetchall()

def create(restaurant_id, creator_id, creator_name, content):
        sql = "INSERT INTO questions (restaurant_id, creator_id, creator_name, content) VALUES (:restaurant_id, :creator_id, :creator_name, :content)"
        db.session.execute(text(sql), {"restaurant_id":restaurant_id, "creator_id":creator_id, "creator_name":creator_name, "content":content})
        db.session.commit()
        return True

def delete(id):
        sql = "UPDATE questions SET visible = FALSE WHERE id=:id"
        db.session.execute(text(sql), {"id":id})
        db.session.commit()
        return True

def restore(id):
        sql = "UPDATE questions SET visible = TRUE WHERE id=:id"
        db.session.execute(text(sql), {"id":id})
        db.session.commit()
        return True

def get_content(question_id):
	sql = "SELECT restaurant_id, creator_id, creator_name, content FROM questions WHERE id = :id"
	result = db.session.execute(text(sql), {"id":question_id})
	return result.fetchall()

def get_restaurant_questions(restaurant_id):
        sql = "SELECT id, creator_id, creator_name, content FROM questions WHERE restaurant_id = :restaurant_id AND visible = TRUE ORDER BY creator_id"
        result = db.session.execute(text(sql), {"restaurant_id":restaurant_id})
        return result.fetchall()

def get_unanswered_restaurant_questions(restaurant_id):
	sql = "SELECT id, creator_id, creator_name, content FROM questions WHERE restaurant_id = :restaurant_id AND visible = TRUE AND answered = FALSE ORDER BY creator_id"
	result = db.session.execute(text(sql), {"restaurant_id":restaurant_id})
	return result.fetchall()

def mark_as_answered(question_id):
	sql = "UPDATE questions SET answered = TRUE WHERE id=:id"
	db.session.execute(text(sql), {"id":question_id})
	db.session.commit()
	return True

def get_deleted_entries():
        sql = "SELECT id, restaurant_id, creator_id, creator_name, content FROM questions WHERE visible = FALSE ORDER BY restaurant_id, creator_id"
        result = db.session.execute(text(sql))
        return result.fetchall()

def get_user_questions(creator_id):
	sql = "SELECT restaurant_id, content FROM questions WHERE visible = TRUE AND creator_id = :creator_id ORDER BY restaurant_id"
	result = db.session.execute(text(sql), {"creator_id":creator_id})
	return result.fetchall()
