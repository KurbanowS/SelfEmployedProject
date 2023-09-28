from flask import render_template, url_for, redirect, request, jsonify, flash, current_app
from main import db
from main.developers import bp
from .models import Developers, Banners

@bp.route('/')
@bp.route('/index')
def index():
    page = request.args.get('page', 1, type=int)
    dev = Developers.query.filter(Developers.id > 0).order_by(Developers.id.desc()).paginate(page=page, per_page=current_app.config['POST_PER_PAGE'])
    banners = Banners.query.all()
    next_url = url_for('dev.index', page=dev.next_num) if dev.has_next else None
    prev_url = url_for('dev.index', page=dev.prev_num) if dev.has_prev else None
    return render_template('dev/index.html', title='All developers', dev=dev, next_url=next_url, prev_url=prev_url, banners=banners)


@bp.route('/developer/<int:id>')
def single_page(id):
    developer = Developers.query.get_or_404(id)
    return render_template('dev/single_page.html', developer=developer)


@bp.route('/adddeveloper', methods=['POST', 'GET'])
def adddeveloper():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        desc = request.form['desc']
        user = Developers(name=name, email=email, desc=desc)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('dev.index'))
    return render_template('dev/add_dev.html', title='Add Developer')


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
    
    
# @bp.route('/search')
# def s_dev():
#     keyword = request.args.get('q')
#     results = Developers.query.msearch(keyword, fields=['name','email'], limit=30)
#     return render_template('dev/search.html', results=results)

