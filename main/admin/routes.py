from flask import render_template, url_for, redirect, request, jsonify, flash, current_app
from flask_login import login_user, current_user, logout_user, login_required
from main import db
from main.admin import bp
from .forms import LoginForm, RegisterForm
from .models import Me
from main.designers.models import Designers
from main.developers.models import Developers
from werkzeug.urls import url_parse


@bp.route('/admin/developer', methods=['POST', 'GET'])
@login_required
def dev_page():
    dev = Developers.query.all()
    return render_template('admin/admin_page.html', title='Developer page', dev=dev)


@bp.route('/admin/designer', methods=['POST', 'GET'])
@login_required
def des_page():
    des = Designers.query.all()    
    return render_template('admin/admin_page.html', title='Designer page', des=des)


@bp.route('/admin/register', methods=['POST', 'GET'])
def admin_register():
    form = RegisterForm()
    if form.validate_on_submit():
        admin = Me(name=form.name.data, email=form.email.data)
        admin.set_password(form.password.data)
        db.session.add(admin)
        db.session.commit()
        return redirect(url_for('AD.admin_login'))
    return render_template('admin/register.html', title='Sign up', form=form)


@bp.route('/admin/login', methods=['POST', 'GET'])
def admin_login():
    if current_user.is_authenticated:
        return redirect(url_for('AD.dev_page'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Me.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Ivalid username or password')
            return redirect(url_for('AD.admin_login'))
        login_user(user)
        next_page = request.args.get('next').split()
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('AD.dev_page')
        return redirect(next_page)
    return render_template('admin/login.html', title='Sign in', form=form)


@bp.route('/admin/logout')
def admin_logout():
    logout_user()
    return redirect(url_for('AD.admin_login'))


@bp.route('/admin/deletedev/<int:id>', methods=['POST'])
@login_required
def delete_dev(id):
    deleteuser = Developers.query.get_or_404(id)
    if request.method == 'POST':
        db.session.delete(deleteuser)
        db.session.commit()
        return redirect(url_for('AD.dev_page'))
    flash("User can't be deleted")


@bp.route('/admin/deletedes/<int:id>', methods=['POST'])
@login_required
def delete_des(id):
    deleteuser = Designers.query.get_or_404(id)
    if request.method == 'POST':
        db.session.delete(deleteuser)
        db.session.commit()
        return redirect(url_for('AD.des_page'))
    flash("User can't be deleted")
    
