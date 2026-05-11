from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def weather():
    try:
        url = (
            "https://api.open-meteo.com/v1/forecast"
            "?latitude=-37.8136"
            "&longitude=144.9631"
            "&current_weather=true"
        )

        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()
        current = data.get("current_weather", {})

        temperature = current.get("temperature", "Unavailable")
        windspeed = current.get("windspeed", "Unavailable")

        return f"""
        <h1>Melbourne Weather</h1>
        <p>Temperature: {temperature}°C</p>
        <p>Wind Speed: {windspeed} km/h</p>
        """

    except Exception as e:
        return f"""
        <h1>Melbourne Weather</h1>
        <p>Weather service is temporarily unavailable.</p>
        <p>Error: {str(e)}</p>
        """, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)