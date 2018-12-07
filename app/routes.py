from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import LoginForm
from app.models import User
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

@app.route('/')
@app.route('/index')
@login_required
def index():
    events = [
        {
            'timestamp': '2018-11-27 16:55:34.123456',
            'type': 'carEntered',
            'description': 'Car started',
            'additional_data': '51.20308577,4.49374067'
        },
        {
            'timestamp': '2018-11-27 17:07:27.123406',
            'type': 'carLeft',
            'description': 'Car stopped',
            'additional_data': '51.50308577,4.43374067'
        }
    ]
    return render_template('index.html', title='Home', events=events)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated():
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
