from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def weather():
    url = (
        "https://api.open-meteo.com/v1/forecast"
        "?latitude=-37.8136"
        "&longitude=144.9631"
        "&current_weather=true"
    )

    response = requests.get(url, timeout=10)
    data = response.json()
    current = data.get("current_weather", {})

    temperature = current.get("temperature")
    windspeed = current.get("windspeed")

    return f"""
    <h1>Melbourne Weather</h1>
    <p>Temperature: {temperature}°C</p>
    <p>Wind Speed: {windspeed} km/h</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)