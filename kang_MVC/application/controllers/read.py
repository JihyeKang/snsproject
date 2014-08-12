#-*- coding:utf-8 -*-

from flask import request, render_template, session, redirect, url_for, flash
from application import app
# from application.models import data_manager
import re

@app.route('/read')
def read() :
	return render_template("read.html")