# Создать форму для регистрации пользователей на сайте. Форма должна содержать поля "Имя", "Фамилия",
# "Email", "Пароль" и кнопку "Зарегистрироваться". При отправке формы данные должны сохраняться
#  в базе данных, а пароль должен быть зашифрован.
from flask import Flask, request, render_template, abort, flash, redirect, url_for
from flask_wtf.csrf import CSRFProtect
from flask import render_template, request
from werkzeug.security import generate_password_hash, check_password_hash
from Flask_project.HW_3.models import db, User
from Flask_project.HW_3.forms import RegistrationForm

app = Flask(__name__)

# защищаем от CSRF-атак, создаем ключ
app.config['SECRET_KEY'] = b'e3001ac912d3e18f78bb61852f4e64c7325bd85bbd1bedd81968d7cfdb933a71'
csrf = CSRFProtect(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users_database.db'
db.init_app(app)


@app.route('/')
@app.route('/index/')
def index():
    context = {
        'title': 'Главная'
    }
    return render_template('index.html', **context)

# инициализация БД
@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('The database has been created')


@app.cli.command("add-john")
def add_user():
    user = User(username='john', email='john@example.com', password='john11')
    db.session.add(user)
    db.session.commit()
    print('John add in DB!')


# заполняем БД случайными данными
@app.cli.command('fill-db')
def fill_db():
    count = 5
    for user in range(1, count + 1):
        new_user = User(username=f'user{user}', email=f'user{user}@mail.ru')
        db.session.add(new_user)
    db.session.commit()
    print(f'The database is full')


@app.route('/register/', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if request.method == 'POST' and form.validate():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        print(username, email, password)

        new_user = User(
            username=username,
            email=email,
            password=password,
        )
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
    return render_template('register.html', form=form)


# приветствуем зарегистрированного пользователя
@app.route('/hello/')
def hello():
    return render_template('hello')


# выводим всех пользователей из БД
@app.route('/users/')
def users():
    users = User.query.all()
    res = ", ".join([user.username for user in users])
    return res


if __name__ == '__main__':
    app.run(debug=True)
