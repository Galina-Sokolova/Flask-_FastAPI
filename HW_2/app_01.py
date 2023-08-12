# Создать страницу, на которой будет форма для ввода имени и электронной почты, при отправке
# которой будет создан cookie-файл с данными пользователя, а также будет произведено
# перенаправление на страницу приветствия, где будет отображаться имя пользователя.
# На странице приветствия должна быть кнопка «Выйти», при нажатии на которую будет
# удалён cookie-файл с данными пользователя и произведено перенаправление на страницу
# ввода имени и электронной почты.
from flask import Flask, request, redirect, url_for, make_response

app = Flask(__name__)


@app.route('/inputdata/', methods=['POST', 'GET'])
def input_data():
    form = """
    <form method=post enctype=multipart/form-data>
    <input type="text" placeholder="Input name" name="name_input"><br>
    <input type="text" placeholder="Input email" name="email_input"><br>
    <input type=submit value=Отправить>
    </form>
    """

    if request.method == 'POST':
        name_input = request.form.get('name_input') or 'NoName'
        email_input = request.form.get('email_input') or 'NoEmail'
        response = make_response("Setting a cookie")
        response.set_cookie('name_input', name_input, max_age=60 * 60 * 24 * 365 * 2)
        response.set_cookie('email_input', email_input, max_age=60 * 60 * 24 * 365 * 2)
        return redirect(url_for('hello', name_input=name_input, email_input=email_input))
    return form


@app.route('/hello/<name_input>-<email_input>', methods=['POST', 'GET'])
def hello(name_input, email_input):
    form_2 = """
        <form method=post enctype=multipart/form-data>
        <input type=submit value=Выйти>
        </form>
        """
    if request.method == 'POST':
        response = make_response("Cookie")
        response.delete_cookie('name_input')
        response.delete_cookie('email_input')
        # print(request.cookies.get('name_input'))
        # print(request.cookies.get('email_input'))
        return redirect(url_for('input_data'))
    return f'Привет, {name_input}' + form_2


if __name__ == '__main__':
    app.run(debug=True)
