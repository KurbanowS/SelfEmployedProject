from flask import render_template, url_for, redirect, request
from main import app
from .models import Me

@app.route('/')
@app.route('/index')
def index():
    me = Me.query.all()
    return render_template('index.html', title='About me', me=me)