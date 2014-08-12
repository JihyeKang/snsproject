from flask import request, render_template
from application import app
from application.models import user_manager
import re


@app.route('/signup')
def signup():	
	return render_template('signup.html')

@app.route('/join_submit', methods = ['GET', 'POST'])
def join_submit():
	if request.method == 'POST':
		user_manager.add_user(request.form)
		return render_template('login.html')
	else:
		return render_template('signup.html')