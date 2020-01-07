from flask import Flask, render_template

from webapp.python_org_news import get_python_news
from webapp.weather import weather_by_city


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        title = "Новости Python"
        weather = weather_by_city('Tver,Russia')
        news_list = get_python_news()
        return render_template('index.html', title=title, weather=weather, news_list=news_list)

    return app


# Linux и Mac:   export FLASK_APP=webapp && export FLASK_ENV=development && flask run
# Windows:       set FLASK_APP=webapp && set FLASK_ENV=development && set FLASK_DEBUG=1 && flask run
