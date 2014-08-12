#-*- coding:utf-8 -*-

from flask import request, render_template, session, redirect, url_for, flash
from application import app
from application.models.user_manager import *
# from application.models import data_manager
import re

@app.route('/wall')
def wall() :
	return render_template("wall.html")

@app.route('/timeline', defaults={'wall_id':0})
@app.route('/timeline/<int:wall_id>')
def timeline(wall_id):
	if not session['logged_in'] : 
		return redirect(url_for('login'))

	if wall_id == 0 : 
		session['wall_name'] = session['user_name']
		session['wall_id'] = session['user_id']
	else:
		session['wall_name'] = get_user(wall_id).username
		session['wall_id'] = get_user(wall_id).id
	user = get_user(session['wall_id'])
	return render_template('wall.html',posts=user.wall_posts)

	# context = {
	# 'posts' : get_wall_posts(wall_id,0),
	# 'BS' : BS
	# }
	# postList = render_template('post_list.html',context=context)
	# context = {
	# 'post_list':postList
	# }