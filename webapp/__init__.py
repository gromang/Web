from flask import Flask, render_template

<<<<<<< HEAD
from webapp.python_org_news import get_python_news
from webapp.weather import weather_by_city
=======

from webapp.weather import weather_by_city
from webapp.model import db, News

>>>>>>> 0768386f247444a3c6f6034d732eed23c4b2b698


def create_app():
    app = Flask(__name__)
<<<<<<< HEAD
=======
    app.config.from_pyfile('config.py')
    db.init_app(app)
>>>>>>> 0768386f247444a3c6f6034d732eed23c4b2b698

    @app.route('/')
    def index():
        title = "Новости Python"
<<<<<<< HEAD
        weather = weather_by_city('Tver,Russia')
        news_list = get_python_news()
=======
        weather = weather_by_city(app.config['WEATHER_DEFAULT_CITY'])
        news_list = News.query.order_by(News.published.desc()).all()
>>>>>>> 0768386f247444a3c6f6034d732eed23c4b2b698
        return render_template('index.html', title=title, weather=weather, news_list=news_list)

    return app


<<<<<<< HEAD
# Linux и Mac:   export FLASK_APP=webapp && export FLASK_ENV=development && flask run
# Windows:       set FLASK_APP=webapp && set FLASK_ENV=development && set FLASK_DEBUG=1 && flask run
=======
>>>>>>> 0768386f247444a3c6f6034d732eed23c4b2b698
