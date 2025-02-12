from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# Contoh data suhu dan kelembapan untuk masing-masing kota di Jawa Timur
cities = {
    "Surabaya": {"lat": -7.2575, "lon": 112.7521},
    "Malang": {"lat": -7.9819, "lon": 112.6265},
    "Kediri": {"lat": -7.8228, "lon": 112.0111},
    "Madiun": {"lat": -7.6296, "lon": 111.5233},
    "Blitar": {"lat": -8.0955, "lon": 112.1628},
    "Jember": {"lat": -8.1845, "lon": 113.6681},
    "Banyuwangi": {"lat": -8.2192, "lon": 114.3696},
    "Sidoarjo": {"lat": -7.4478, "lon": 112.7183},
    "Pasuruan": {"lat": -7.6453, "lon": 112.9075}
}

def generate_weather_data():
    return {city: {
        "temperature": round(random.uniform(24, 35), 1),
        "humidity": round(random.uniform(50, 90), 1),
        "air_quality": round(random.uniform(50, 150), 1)
    } for city in cities}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/weather', methods=['GET'])
def get_weather_data():
    data = generate_weather_data()
    print("Weather Data:", data)  # Debugging log
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
