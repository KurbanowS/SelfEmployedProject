from flask import url_for, redirect, render_template, request, jsonify, current_app
from main import db
from main.designers import bp
from .models import Designers


@bp.route('/designerpage')
def designer_page():
    page = request.args.get('page', 1, type=int)
    des = Designers.query.filter(Designers.id > 0).order_by(Designers.id.desc()).paginate(page=page, per_page=current_app.config['POST_PER_PAGE'])
    next_url = url_for('des.designer_page', page=des.next_num) if des.has_next else None
    prev_url = url_for('des.designer_page', page=des.prev_num) if des.has_prev else None
    return render_template('dev/index.html', title='All UI/UX Designers', des=des, next_url=next_url, prev_url=prev_url)


@bp.route('/designer/<int:id>')
def single_pag(id):
    designer = Designers.query.get_or_404(id)
    return render_template('dev/single_page.html', designer=designer)


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