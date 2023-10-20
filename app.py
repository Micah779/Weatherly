import configparser
import requests
from flask import Flask
from flask import render_template, request # allows us to render HTML files

app = Flask(__name__) # application instance

api_key = "cc631ac49cd8a748900eedaba0033755"

@app.route('/', methods=["POST", 'GET']) # application route
def index(): # view function

    # initializing data variables outside of the conditional statement so that they can be accessed
    location, temp, feels_like, weather = None, None, None, None

    if request.method == "POST":
        zipcode = request.form['zipCode']
        data = get_weather_results(zipcode, api_key)

        # variables
        temp = "{0:.2f}".format(data["main"]["temp"])
        feels_like = "{0:.2f}".format(data["main"]["feels_like"])
        weather = data["weather"][0]["main"]
        location = data["name"]

    # renders the index.html file as a view function with all of the variables from the api data
    return render_template('index.html', location=location, temp=temp, feels_like=feels_like, weather=weather)

# function to take in a zipcode and api key to return weather results
def get_weather_results(zipcode, api_key):
    api_url = "https://api.openweathermap.org/data/2.5/weather?zip={},&units=imperial&appid={}".format(zipcode,api_key)
    r = requests.get(api_url)
    return r.json()

if __name__ == '__main__':
    app.run(debug=True) # programmatitically running Flask