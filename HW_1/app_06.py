# Написать функцию, которая будет выводить на экран HTML
# страницу с блоками новостей.
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/news/')
def news():
    news = [{'title': 'News1', 'text': 'Text1', 'date': '20.06.2023'},
            {'title': 'News2', 'text': 'Text2', 'date': '21.06.2023'},
            {'title': 'News3', 'text': 'Text3', 'date': '22.06.2023'},
            {'title': 'News4', 'text': 'Text4', 'date': '23.06.2023'}]
    return render_template('news.html', news=news)


if __name__ == '__main__':
    app.run()
