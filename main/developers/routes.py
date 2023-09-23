from flask import render_template, url_for, redirect, request, jsonify, flash
from main import db
from main.developers import bp
from .models import Developers


@bp.route('/')
@bp.route('/index')
def index():
    dev = Developers.query.all()
    return render_template('dev/index.html', title='All developers', dev=dev)


@bp.route('/addeveloper', methods=['POST'])
def addeveloper():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        desc = request.form['desc']
        user = Developers(name=name, email=email, desc=desc)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('dev.index'))
    return render_template('dev/add_user.html', title='Add Developer')


@bp.route('/api/developer/<int:id>', methods=['GET'])
def developer(id):
    return jsonify(Developers.query.get_or_404(id).to_dict())


@bp.route('/api/developer', methods=['POST'])
def postdeveloper():
    data = request.get_json() or {}
    if 'name' not in data or 'email' not in data:
        return 
    if Developers.query.filter_by(name=data['name']).first():
        return 
    if Developers.query.filter_by(email=data['email']).first():
        return 
    developer = Developers()
    developer.from_dict(data)
    db.session.add(developer)
    db.session.commit()
    response = jsonify(developer.to_dict())
    response.status_code = 201
    return response
    
    
    


