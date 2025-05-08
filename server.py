import sys
from flask import Flask, request, render_template
from weather import get_current_weather
from waitress import serve
import os


app = Flask(__name__)

@app.route('/')
def index():
    print("Rendering index.html")
    return render_template("index.html")

@app.route('/health')
def health():
    return "OK", 200


@app.route('/weather')
def get_weather():
    print("Rendering weather.html")
    city = request.args.get('city')

    if not bool(city.strip()):
        city = "Mumbai"


    weather_data = get_current_weather(city)
    if not weather_data["cod"] == 200:
        return render_template("city_not_found.html")

    return render_template(
        "weather.html",
        title=weather_data["name"],
        status=weather_data["weather"][0]["description"].capitalize(),
        temp=f"{weather_data['main']['temp']:.1f}",
        feels_like=f"{weather_data['main']['feels_like']:.1f}"
    )

if __name__ == '__main__':
    print(f"Flask app starting with APP_Name = {os.getenv('APP_Name')}", flush=True)
    serve(app, host='0.0.0.0', port=8000)
