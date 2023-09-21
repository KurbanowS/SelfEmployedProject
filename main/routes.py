from flask import render_template, url_for, redirect, request, jsonify, flash
from main import app, db
from .models import Me



@app.route('/')
@app.route('/index')
def index():
    me = Me.query.all()
    return render_template('index.html', title='About Me', me=me)


@app.route('/adduser', methods=['POST'])
def adduser():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        desc = request.form['desc']
        user = Me(name=name, email=email, desc=desc)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_user.html', title='Add User')


@app.route('/api/developers', methods=['GET'])
def developers():
    return jsonify(Me.query.all().to_dict())


@app.route('/api/developers', methods=['POST'])
def adddeveloper():
    data = request.get_json() or {}
    if 'name' not in data or 'email' not in data:
        return 
    if Me.query.filter_by(name=data['name']).first():
        return 
    if Me.query.filter_by(email=data['email']).first():
        return 
    developer = Me()
    developer.from_dict(data)
    db.session.add(developer)
    db.session.commit()
    response = jsonify(developer.to_dict())
    response.status_code = 201
    return response
    
    
    


