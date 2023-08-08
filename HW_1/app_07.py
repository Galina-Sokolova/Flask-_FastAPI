# Создать базовый шаблон для всего сайта, содержащий
# общие элементы дизайна (шапка, меню, подвал), и
# дочерние шаблоны для каждой отдельной страницы.
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/base/')
def base():
    context = {'title': 'Главная'}
    return render_template('base.html', **context)


@app.route('/about/')
def about():
    context = {'title': 'О себе'}
    return render_template('base_about.html', **context)


@app.route('/contacts/')
def contacts():
    context = {'title': 'Контакты'}
    return render_template('base_contacts.html', **context)


if __name__ == '__main__':
    app.run()
