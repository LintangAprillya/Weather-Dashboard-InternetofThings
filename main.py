from flask import Flask, render_template
import random
import time

app = Flask(__name__)


# Fungsi untuk menghasilkan data suhu, kelembapan, dan kecepatan angin random
def generate_random_weather_data():
    temperature = round(random.uniform(20, 35), 2)  # Suhu antara 20°C hingga 35°C
    humidity = round(random.uniform(50, 90), 2)  # Kelembapan antara 50% hingga 90%
    wind_speed = round(random.uniform(0, 20), 2)  # Kecepatan angin antara 0 - 20 km/h
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())  # Waktu saat data diambil
    return {"temperature": temperature, "humidity": humidity, "wind_speed": wind_speed, "timestamp": timestamp}


@app.route('/')
def index():
    # Simulasikan data 24 jam (1 data per jam)
    weather_data = [generate_random_weather_data() for _ in range(24)]

    return render_template('index.html', weather_data=weather_data)


if __name__ == '__main__':
    app.run(debug=True)
