#from bs4 import BeautifulSoup
'''
import requests

url = f"http://api.openweathermap.org/data/2.5/weather?q=kannur&units=metric&appid=b21a2633ddaac750a77524f91fe104e7"

resp = requests.get(url).json()

icon = resp['weather'][0]['icon']
latitude = resp['coord']['lat']
longitude = resp['coord']['lon']
humidity = resp['main']['humidity']
temperature = resp['main']['temp']
city = resp['name']

data = {
    'icon':icon,
    'city': city,
    'latitude' : latitude,
    'longitude': longitude,
    'humidity': humidity,
    'temperature':temperature
}



print(data['city'])


'''

from dotenv import load_dotenv
import os
load_dotenv()

apikey = os.getenv('API_KEY')

print(type(apikey))