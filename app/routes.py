from flask import render_template, redirect, url_for, abort

from . import app
from .forms import EmergencyLoginForm


@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html', title='Заготовка')


@app.route('/training/<string:prof>')
def trainings(prof):
    if prof == 'врач':
        context = {
            'img_url': 'https://i.ibb.co/HTmW0Yk/science.png',
            'img_title': 'Научные симуляторы',
            'title': 'Title'
        }
        return render_template('training.html', **context)
    elif prof == 'инженер':
        context = {
            'img_url': 'https://i.ibb.co/vJ3Y8sm/engineering.png',
            'img_title': 'Инженерные тренажеры',
        }
        return render_template('training.html', **context)
    elif 'врач' in prof:
        return redirect(url_for('trainings', prof='врач'))
    elif 'инженер' in prof:
        return redirect(url_for('trainings', prof='инженер'))
    abort(404)


@app.route('/list_prof/<string:list_type>')
def list_professions(list_type):
    if list_type not in ['ol', 'ul']:
        abort(404)
    context = {
        'list_type': list_type,
        'jobs': [
            'Product Manager',
            'Data Analyst',
            'Educator',
            'Financial Advisors',
            'Data Journalist',
        ]
    }
    return render_template('jobs_list.html', **context)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    context = {
        'title': '',
        'surname': 'Watny',
        'name': 'Mark',
        'education': 'выше среднего',
        'profession': 'штурман марсохода',
        'sex': 'm',
        'motivation': 'Всегда мечтал застрять на Марсе!',
        'ready': True
    }
    return render_template('auto_answer.html', **context)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = EmergencyLoginForm()
    context = {
        'form': form,
        'title': 'Аварийный доступ',
        'messages': []
    }
    if form.validate_on_submit():
        context['messages'].append('Вы успешно вошли!')
    return render_template('emergency_login.html', **context)
