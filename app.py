import requests
from flask import Flask, render_template,request
from os import environ

app = Flask(__name__)
app.config['SECRET_KEY'] = environ.get('API_KEY')
API_KEY = app.config['SECRET_KEY']

@app.route('/', methods=["GET", "POST"])
def home():
    place = request.args.get('place')
    url = f"http://api.openweathermap.org/data/2.5/weather?q={place}&units=metric&appid={API_KEY}"
    resp = requests.get(url).json()

    latitude = resp['coord']['lat']
    longitude = resp['coord']['lon']
    humidity = resp['main']['humidity']
    temperature = resp['main']['temp']
    city = resp['name']
    icon = resp['weather'][0]['icon']
    
    data = {
        'icon':icon,
        'city':city,
        'latitude' : latitude,
        'longitude': longitude,
        'humidity': humidity,
        'temperature':temperature
    }
    

    return render_template('index.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)
