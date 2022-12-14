from apppi import app
from flask import render_template
from random import choice

menu = [{"name": 'Главная', "url": 'index'}, {"name": 'О программе', "url": 'about'},
{"name": 'Помощь', "url": 'help'}, {"name": 'я', "url": 'nikita'}]

@app.route('/')
@app.route('/index')
def index():
    best_pi = {'username': 'Никита'}

    return render_template('index.html', title='2022 Forever', user=best_pi, menu=menu)


@app.route('/help')
def help():
    sp = ['PI', '2014', '']
    return render_template('help.html', title=choice(sp), menu=menu)


@app.route('/about')
def about():
    return render_template('about.html', menu=menu)


@app.route('/nikita')
def nikita():
    return render_template('nikita5023.html', menu=menu)