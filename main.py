
# main.py

from flask import Flask, render_template, jsonify, request
import requests

app = Flask(__name__)

# Route to render the main HTML page
@app.route('/')
def index():
    return render_template('index.html')

# API endpoint to fetch air quality data
@app.route('/air_quality_data')
def get_air_quality_data():
    # Fetch the data from the API
    response = requests.get('https://api.breezometer.com/air-quality/v2/current-conditions?lat=37.78&lon=-122.41&key=YOUR_API_KEY')
    data = response.json()

    # Prepare the data for the map
    air_quality_data = []
    for location in data['data']:
        air_quality_data.append({
            'lat': location['lat'],
            'lon': location['lon'],
            'aqi': location['indexes']['baqi']['aqi']
        })

    return jsonify(air_quality_data)

# Route to serve static files
@app.route('/static/<path:filename>')
def static_files(filename):
    return app.send_static_file(filename)

if __name__ == '__main__':
    app.run()
