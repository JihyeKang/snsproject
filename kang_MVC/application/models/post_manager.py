from application import db
from schema import *

def add_post(body,user_id,wall_id):
	post = Post(
		is_secret = 1,
		body = body,
		user_id = user_id,
		wall_id = wall_id
	)
	db.session.add(post)
	db.session.commit()

def add_comment(body,user_id,post_id): 
	comment = Comment(
		body = body,
		user_id = user_id,
		post_id = post_id
		)
	db.session.add(comment)
	db.session.commit()

def get_post_del(post_id):
	post = Post.query.get(post_id)
	db.session.delete(post)
	db.session.commit()

def edit_post(edited_body,post_id):
	post = Post.query.get(post_id)
	post.body = edited_body
	db.session.commit()

def get_comment_del(comment_id):
	comment = Comment.query.get(comment_id)
	db.session.delete(comment)
	db.session.commit()
