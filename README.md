# FlameForecast

FlameForecast is a web application that provides weather information along with wildfire risk assessments. It leverages Flask, SQLite, and the OpenWeather API to deliver current weather conditions, a 7-day forecast, and a predictive model for assessing wildfire risks based on historical weather data.

## Key Features

- **Current Conditions:** View real-time weather data for any location.
- **7-Day Forecast:** Plan ahead with a detailed forecast for the next week.
- **Wildfire Risk Assessment:** Predictive model for assessing the risk of wildfires in a given area.

## Technologies Used

- **Flask:** A lightweight Python web framework for building the backend.
- **SQLite:** A simple and easy-to-use database for storing user accounts and other persistent data.
- **OpenWeather API:** Provides current weather data for any location.
- **Machine Learning Model:** Implements a predictive model for wildfire risk assessment.

## Getting Started

### Prerequisites

- [Python](https://www.python.org/) installed
- [Virtualenv](https://pypi.org/project/virtualenv/) for managing Python environments
- [API Key](https://openweathermap.org/appid) from OpenWeatherMap

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/flameforecast.git
   cd flameforecast
Set up a virtual environment:

bash
Copy code
virtualenv venv
source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Create a .env file in the project root and add your OpenWeatherMap API key:

plaintext
Copy code
OPENWEATHER_API_KEY=your_api_key
Run the application:

bash
Copy code
flask run
Open your browser and navigate to http://localhost:5000/ to access FlameForecast.

Usage
Home Page:

Enter a zip code in the search bar to get weather information for a specific location.
Explore the current conditions, 7-day forecast, and wildfire risk assessment.
Dark Mode:

Toggle between light and dark modes using the light/dark button in the header.
Community Engagement:

Contribute to the project by providing feedback and reporting incidents.
Engage with the community to enhance the wildfire risk assessment model.
Contributing
If you'd like to contribute to FlameForecast, follow these steps:

Fork the repository.
Create a new branch (git checkout -b feature/improvement)
Make changes and commit (git commit -m 'Add feature/improvement')
Push to the branch (git push origin feature/improvement)
Open a pull request.

Acknowledgements
Thanks to OpenWeatherMap for providing the weather data API.
Special mention to contributors and community members who help improve FlameForecast.
