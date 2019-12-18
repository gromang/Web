import os
basedir = os.path.abspath(os.path.dirname(__file__))

WEATHER_DEFAULT_CITY = "Tver,Russia"
WEATHER_API_KEY = "290249d9abc34900bf8170408190512"
WEATHER_URL = "http://api.worldweatheronline.com/premium/v1/weather.ashx"
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'webapp.db')