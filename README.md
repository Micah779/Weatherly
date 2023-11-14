# Weatherly

Weatherly is a web application that provides weather information and in the future wildfire risk assessments. It leverages Flask, and the OpenWeather API to deliver current weather conditions, a 7-day forecast, and soon a predictive model for assessing wildfire risks based on historical weather data.

## Key Features

- **Current Conditions:** View real-time weather data for any location.
- **7-Day Forecast:** Plan ahead with a detailed forecast for the next week.
- **(Planned) Wildfire Risk Assessment:** Predictive model for assessing the risk of wildfires in a given area.

## Technologies Used

- **(Active) Flask:** A lightweight Python web framework for building the backend.
- **(Planned) SQLite:** A simple and easy-to-use database for storing user accounts and other persistent data.
- **(Active) OpenWeather API:** Provides current weather data for any location.
- **(Planned) Machine Learning Model:** Implements a predictive model for wildfire risk assessment.

## Getting Started

## Screenshots

![Screenshot 1](/weatherlyshot2.png)
*Light Mode*

![Screenshot 2](/weatherlyshot1.png)
*Dark Mode*

### Prerequisites

- [Python](https://www.python.org/) installed
- [Virtualenv](https://pypi.org/project/virtualenv/) for managing Python environments
- [API Key](https://openweathermap.org/appid) from OpenWeatherMap

markdown
Copy code
### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/weatherly.git
   cd weatherly
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
Open your browser and navigate to http://localhost:5000/ to access Weatherly.

# Usage

### Home Page:

- Enter a zip code in the search bar to get weather information for a specific location.
- Explore the current conditions, 7-day forecast, and wildfire risk assessment.

### Dark Mode:

- Toggle between light and dark modes using the light/dark button in the header.

### Community Engagement:

- Contribute to the project by providing feedback and reporting incidents.
- Engage with the community to enhance the wildfire risk assessment model.

# Contributing

If you'd like to contribute to FlameForecast, follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/improvement`).
3. Make changes and commit (`git commit -m 'Add feature/improvement'`).
4. Push to the branch (`git push origin feature/improvement`).
5. Open a pull request.

# Acknowledgements

- Thanks to OpenWeatherMap for providing the weather data API.
- Special mention to contributors and community members who help improve FlameForecast.

