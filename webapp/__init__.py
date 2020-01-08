from flask import Flask, render_template


from webapp.weather import weather_by_city
from webapp.model import db, News
from webapp.forms import LoginForm


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route('/')
    def index():
        title = "Новости Python"
        weather = weather_by_city(app.config['WEATHER_DEFAULT_CITY'])
        news_list = News.query.order_by(News.published.desc()).all()
        return render_template('index.html', title=title, weather=weather, news_list=news_list)

    @app.route('/login')
    def login():
        title = "Авторизация"
        login_form = LoginForm()
        return render_template("login.html", title=title, form=login_form)

    return app

# Linux и Mac:   export FLASK_APP=webapp && export FLASK_ENV=development && flask run
# Windows:       set FLASK_APP=webapp && set FLASK_ENV=development && set FLASK_DEBUG=1 && flask run
