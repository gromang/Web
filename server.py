from flask import Flask
from weather import weather_by_city

app = Flask(__name__)


@app.route('/')
def index():
    weather = weather_by_city('Tver,Russia')

    if weather:
        tempr = weather["temp_C"]
        feels = weather['FeelsLikeC']
        return f"Погода: {tempr}, ощущается как {feels}"
    else:
        return "Сервис погоды временно не доступен"


if __name__ == "__main__":
    app.run(debug=True)
