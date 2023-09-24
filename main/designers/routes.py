from flask import url_for, redirect, render_template, request, jsonify
from main import db
from main.designers import bp
from .models import Designers


@bp.route('/designerpage')
def designer_page():
    des = Designers.query.all()
    return render_template('dev/designer_page.html', title='All UI/UX Designers', des=des)


@bp.route('/adddesigner', methods=['POST', 'GET'])
def adddesigner():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        desc = request.form['desc']
        user = Designers(name=name, email=email, desc=desc)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('des.designer_page'))
    return render_template('dev/add_des.html', title='Add Designer')


@bp.route('/api/designer/<int:id>', methods=['GET'])
def designer(id):
    return jsonify(Designers.query.get_or_404(id).to_dictt())


@bp.route('/api/designer', methods=['POST'])
def postdesigner():
    data = request.get_json() or {}
    if 'name' not in data or 'email' not in data:
        return 
    if Designers.query.filter_by(name=data['name']).first():
        return 
    if Designers.query.filter_by(email=data['email']).first():
        return 
    designer = Designers()
    designer.from_dictt(data)
    db.session.add(designer)
    db.session.commit()
    response = jsonify(designer.to_dictt())
    response.status_code = 201
    return response