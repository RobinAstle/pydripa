from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Pierre'}
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
    return render_template('index.html', title='Home', user=user, events=events)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
