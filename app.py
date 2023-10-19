import configparser
import requests
from flask import Flask
from flask import render_template, request # allows us to render HTML files

app = Flask(__name__) # application instance

@app.route('/') # application route
def index(): # view function
    return render_template('index.html') # renders the index.html file as a view function

@app.route('/results', methods=['POST'])
def render_results():
    zipcode = request.form['zipCode']

    api_key = get_api_key()
    data = get_weather_results(zipcode, api_key)

    # variables
    temp = "{0:.2f}".format(data["main"]["temp"])
    feels_like = "{0:.2f}".format(data["main"]["feels_like"])
    weather = data["weather"][0]["main"]
    location = data["name"]

    return render_template('base.html', location=location, temp=temp, feels_like=feels_like, weather=weather)

def get_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini') # read in the config.ini file
    return config['weatherly']['api'] # getting the api key, now we can run 'get_api_key()'

# function to take in a zipcode and api key to return weather results
def get_weather_results(zipcode, api_key):
    api_url = "https://api.openweathermap.org/data/2.5/weather?zip={},&units=imperial&appid={}".format(zipcode,api_key)
    r = requests.get(api_url)
    return r.json()

if __name__ == '__main__':
    app.run(debug=True) # programmatitically running Flask