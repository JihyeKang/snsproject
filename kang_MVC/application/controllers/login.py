#-*- coding:utf-8 -*-
from application import app
from flask import Flask, request, render_template, session, redirect, url_for, flash, abort
from application.models.user_manager import *
# from application.models import data_manager
import re

@app.route('/login')
def login() :
	return render_template("login.html")

@app.route('/login_check', methods=['GET','POST'])
def login_check():
	if request.method == 'POST' : 
		email = request.form['email']
		password = request.form['password']
		if check_user(email, password) == True : 
			session['logged_in'] = True 
			session['email'] = request.form['email']
			session['user_id'] = get_user_filter(email)[0].id
			session['user_name'] = get_user_filter(email)[0].username
			return redirect(url_for('timeline'))
		else : 
			return render_template("login.html")
	else : 
		return render_template('login.html')

@app.route('/logout')
def logout():
	session.pop('logged_in',None)
	return render_template('login.html')






