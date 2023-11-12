import requests
import requests_cache
import pandas as pd
from flask import Flask, render_template, request
from retry_requests import retry
import openmeteo_requests

app = Flask(__name__)

geo_key = "f77471c0df5447bcbdb66b74acd0acc6"
api_key = "cc631ac49cd8a748900eedaba0033755"

# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
openmeteo = openmeteo_requests.Client(session=retry_session)

# Function to convert zipcode into lat and long for daily forecast data
def get_coordinates_from_zip(zipcode, geo_key):
    geocoding_url = f"https://api.opencagedata.com/geocode/v1/json?q={zipcode}&key={geo_key}"
    r = requests.get(geocoding_url)
    data = r.json()

    if data["results"]:
        latitude = data["results"][0]["geometry"]["lat"]
        longitude = data["results"][0]["geometry"]["lng"]
        return latitude, longitude
    else:
        return None

# Function to fetch Open Meteo forecast data
def get_open_meteo_forecast(zipcode, geo_key, openmeteo):
    # Get coordinates from the ZIP code
    coordinates = get_coordinates_from_zip(zipcode, geo_key)

    if coordinates:
        latitude, longitude = coordinates
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "daily": ["temperature_2m_max", "temperature_2m_min", "uv_index_max"],
            "temperature_unit": "fahrenheit",
            "wind_speed_unit": "mph",
            "precipitation_unit": "inch",
            "timezone": "America/New_York"
        }
        responses = openmeteo.weather_api(url, params=params)

        # Process daily data
        response = responses[0]
        daily = response.Daily()
        daily_temperature_2m_max = daily.Variables(0).ValuesAsNumpy()
        daily_temperature_2m_min = daily.Variables(1).ValuesAsNumpy()
        daily_uv_index_max = daily.Variables(2).ValuesAsNumpy()

        daily_data = {"date": pd.date_range(
            start=pd.to_datetime(daily.Time(), unit="s"),
            end=pd.to_datetime(daily.TimeEnd(), unit="s"),
            freq=pd.Timedelta(seconds=daily.Interval()),
            inclusive="left"
        )}
        daily_data["temperature_2m_max"] = daily_temperature_2m_max
        daily_data["temperature_2m_min"] = daily_temperature_2m_min
        daily_data["uv_index_max"] = daily_uv_index_max  # Fix: Add this line to define uv_index_max

        daily_dataframe = pd.DataFrame(data=daily_data)

        # Extract data for the first 7 days
        forecast_data = {
            "date": daily_data["date"][:7],
            "high": ["{:.0f}".format(temp) for temp in daily_data["temperature_2m_max"][:7]],
            "low": ["{:.0f}".format(temp) for temp in daily_data["temperature_2m_min"][:7]],
            "uv": ["{:.0f}".format(uv) for uv in daily_data["uv_index_max"][:7]]  # Fix: Use uv_index_max here
        }

        return forecast_data
    else:
        # Handle the case where coordinates couldn't be obtained
        print(f"Unable to get coordinates for ZIP code: {zipcode}")
        return None

# function to take in a zipcode and api key to return weather results
def get_weather_results(zipcode, api_key):
    api_url = f"https://api.openweathermap.org/data/2.5/weather?zip={zipcode}&units=imperial&appid={api_key}"
    r = requests.get(api_url)
    return r.json()

# function to return hourly forecast weather data by zipcode
def get_hourly_weather(zipcode, api_key):
    api_url = f"https://api.openweathermap.org/data/2.5/forecast?zip={zipcode}&units=imperial&cnt=8&appid={api_key}"
    r = requests.get(api_url)
    return r.json()

# Route for the main page
@app.route('/', methods=["POST", 'GET'])
def index():
    location, temp, feels_like, weather, high, low, uv, hourly_temps, humidity = None, None, None, None, None, None, None, None, None

    forecast_data = {}

    default_zipcode = "16801"

    if request.method == "POST":
        # If there is a POST request, use the submitted ZIP code
        zipcode = request.form['zipCode']
    else:
        # For initial load, use the default ZIP code
        zipcode = default_zipcode

    current_data = get_weather_results(zipcode, api_key)
    hourly_data = get_hourly_weather(zipcode, api_key)

    # Fetch Open Meteo forecast data
    forecast_data = get_open_meteo_forecast(zipcode, geo_key, openmeteo)

    # sec 2 current weather variables
    temp = "{:.0f}".format((current_data["main"]["temp"]) // 1)  # current temp
    weather = current_data["weather"][0]["main"]  # weather type
    location = current_data["name"]  # location
    high = "{:.0f}".format(current_data["main"]["temp_max"])  # current high
    low = "{:.0f}".format(hourly_data["list"][4]["main"]["temp_min"])  # current low

    # sec 3 weather variables
    humidity = "{:.0f}".format(current_data["main"]["humidity"])  # current humidity
    feels_like = "{:.0f}".format(current_data["main"]["feels_like"])  # current feels temp

    hourly_temps = [round(entry["main"]["temp"]) for entry in hourly_data["list"][:8]]

    # renders the index.html file as a view function with all of the variables from the api data
    return render_template('index.html', location=location, temp=temp, feels_like=feels_like,
                           weather=weather, high=high, low=low, uv=uv, hourly_temps=hourly_temps,
                           forecast_data=forecast_data, humidity=humidity)  # Pass forecast_data to the template

if __name__ == '__main__':
    app.run(debug=True)
