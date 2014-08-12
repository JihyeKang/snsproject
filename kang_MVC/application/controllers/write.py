#-*- coding:utf-8 -*-

from flask import request, render_template, session, redirect, url_for, flash
from application import app
from application.models import user_manager
from application.models import post_manager

@app.route('/write', methods=['POST','GET'])
def write() :
	if request.method == 'POST' : 
		# if secret_post not in request.form : 
		# 	is_secret = 0
		# else : 
		# is_secret =  1 
		body = request.form['body_post']
		user_id = session['user_id']
		wall_id = session['wall_id']
		post_manager.add_post(body,user_id,wall_id)
		return redirect(url_for('timeline',wall_id=session['wall_id']))
	else:
		return render_template("write.html")

@app.route('/write_comment/<int:post_id>',methods=['POST','GET'])
def write_comment(post_id) : 
	if request.method == 'POST' : 
		body = request.form['comment']
		post_id = post_id
		user_id = session['user_id']
		post_manager.add_comment(body,user_id,post_id)
		return redirect(url_for('timeline',wall_id=session['wall_id']))
	else : 
		return render_template('wall.html')

@app.route('/delete', methods=['POST']) 
def delete_post():
	post_manager.get_post_del(request.form['post_id'])
	return redirect(url_for('timeline',wall_id=session['wall_id']))

@app.route('/edit', methods=['POST','GET'])
def edit():
	if request.method == 'POST' : 
		post_id = request.form['post_id']
		post_body = request.form['post_body']
		return render_template('edit_post.html', post_id=post_id, post_body=post_body)
	else: 
		return redirect(url_for('timeline',wall_id=session['wall_id']))
	# else: 
		# return redirect(url_for('timeline',wall_id=session['wall_id']))

@app.route('/edit_post_db',methods=['POST'])
def edit_post_db():
	if request.method == 'POST': 
		post_manager.edit_post(request.form['body_post'],request.form['post_id'])
		return redirect(url_for('timeline',wall_id=session['wall_id']))

@app.route('/delete_comment',methods=['POST'])
def delete_comment():
	post_manager.get_comment_del(request.form['comment_id'])
	return redirect(url_for('timeline',wall_id=session['wall_id']))




 