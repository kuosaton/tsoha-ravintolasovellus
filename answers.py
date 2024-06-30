from sqlalchemy.sql import text
from db import db

def get_list():
        sql = "SELECT id, question_id, creator_id, creator_name, content FROM answers WHERE visible = TRUE ORDER BY question_id, creator_id"
        result = db.session.execute(text(sql))
        return result.fetchall()

def create(question_id, creator_id, creator_name, content):
        sql = "INSERT INTO answers (question_id, creator_id, creator_name, content) VALUES (:question_id, :creator_id, :creator_name,  :content)"
        db.session.execute(text(sql), {"question_id":question_id, "creator_id":creator_id, "creator_name":creator_name, "content":content})
        db.session.commit()
        return True

def delete(id):
        sql = "UPDATE answers SET visible = FALSE WHERE id=:id"
        db.session.execute(text(sql), {"id":id})
        db.session.commit()
        return True

def delete_question_answers(question_id):
	sql = "UPDATE answers SET visible = FALSE WHERE question_id=:question_id"
	db.session.execute(text(sql), {"question_id":question_id})
	db.session.commit()
	return True

def restore(id):
        sql = "UPDATE answers SET visible = TRUE WHERE id=:id"
        db.session.execute(text(sql), {"id":id})
        db.session.commit()
        return True

def restore_question_answers(question_id):
	sql = "UPDATE answers SET visible = TRUE WHERE question_id=:question_id"
	db.session.execute(text(sql), {"question_id":question_id})
	db.session.commit()
	return True

def get_content(answer_id):
	sql = "SELECT question_id, creator_id, creator_name, content FROM answers WHERE id = :id"
	result = db.session.execute(text(sql), {"id":answer_id})
	return result.fetchall()

def get_question_answers(question_id):
        sql = "SELECT question_id, creator_id, creator_name, content FROM answers WHERE question_id = :question_id AND visible = TRUE ORDER BY creator_id"
        result = db.session.execute(text(sql), {"question_id":question_id})
        return result.fetchall()

def get_deleted_entries():
        sql = "SELECT id, question_id, creator_id, creator_name, content FROM answers WHERE visible = FALSE ORDER BY question_id, creator_id"
        result = db.session.execute(text(sql))
        return result.fetchall()

def get_user_answers(creator_id):
	sql = "SELECT question_id, content FROM answers  WHERE visible = TRUE AND creator_id = :creator_id ORDER BY question_id"
	result = db.session.execute(text(sql), {"creator_id":creator_id})
	return result.fetchall()
