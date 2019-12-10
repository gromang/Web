from flask import Flask, render_template
from weather import weather_by_city

app = Flask(__name__)


@app.route('/')
def index():
    title = "Прогноз погоды"
    weather = weather_by_city('Tver,Russia')

    if weather:
        weather_text = f"Погода: {weather['temp_C']}, ощущается как {weather['FeelsLikeC']}"
    else:
        weather_text = "Сервис погоды временно не доступен"
    return render_template('index.html', page_title=title, weather=weather_text)


if __name__ == "__main__":
    app.run(debug=True)
