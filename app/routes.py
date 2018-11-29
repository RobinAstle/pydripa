from flask import render_template
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
            'additionalData': '51.20308577,4.49374067'
        },
        {
            'timestamp': '2018-11-27 17:07:27.123406',
            'type': 'carLeft',
            'description': 'Car stopped',
            'additionalData': '51.50308577,4.43374067'
        }
    ]
    return render_template('index.html', title='Home', user=user, events=events)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign in', form=form)

