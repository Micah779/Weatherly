import configparser
import requests
from flask import Flask
from flask import render_template, request # allows us to render HTML files

app = Flask(__name__) # application instance

api_key = "cc631ac49cd8a748900eedaba0033755"

@app.route('/', methods=["POST", 'GET']) # application route
def index(): # view function

    # initializing data variables outside of the conditional statement so that they can be accessed
    location, temp, feels_like, weather, high, low, humidity, hourly_temps = None, None, None, None, None, None, None, None

    if request.method == "POST":
        zipcode = request.form['zipCode']
        current_data = get_weather_results(zipcode, api_key)
        hourly_data = get_hourly_weather(zipcode, api_key)

        # sec 2 current weather variables
        temp = "{:.0f}".format((current_data["main"]["temp"])//1) # current temp
        weather = current_data["weather"][0]["main"] # weather type
        location = current_data["name"] # location
        high = "{:.0f}".format(current_data["main"]["temp_max"]) # current high
        low = "{:.0f}".format(hourly_data["list"][4]["main"]["temp_min"]) # current low

        # sec 3 weather variables
        humidity = "{:.0f}".format(current_data["main"]["humidity"]) # current humidity
        feels_like = "{:.0f}".format(current_data["main"]["feels_like"]) # current feels temp

        hourly_temps = [round(entry["main"]["temp"]) for entry in hourly_data["list"][:8]] 


    # renders the index.html file as a view function with all of the variables from the api data
    return render_template('index.html', location=location, temp=temp, feels_like=feels_like, weather=weather, high=high, low=low, humidity=humidity, hourly_temps=hourly_temps)

# function to take in a zipcode and api key to return weather results
def get_weather_results(zipcode, api_key):
    api_url = "https://api.openweathermap.org/data/2.5/weather?zip={},&units=imperial&appid={}".format(zipcode,api_key)
    r = requests.get(api_url)

    return r.json()

# function to return hourly forecast weather data by zipcode
def get_hourly_weather(zipcode, api_key):
    api_url = "https://api.openweathermap.org/data/2.5/forecast?zip={},&units=imperial&cnt=8&appid={}".format(zipcode, api_key)
    r = requests.get(api_url)

    return r.json()

if __name__ == '__main__':
    app.run(debug=True) # programmatitically running Flask