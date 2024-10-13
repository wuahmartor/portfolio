# Weather Information System

This is a **Weather Information System** built with Streamlit. It retrieves and displays real-time weather information based on a 
given **city name** or **zip code**. The app uses the **OpenWeatherMap API** to fetch weather data and the **Zippopotam API** for accurate state lookups.

## Features

- Fetch current weather using:
  - **City Name and State Code**
  - **Zip Code**
- Display temperature, humidity, pressure, wind speed, and cloud cover.
- Supports multiple temperature units: **Celsius, Fahrenheit, and Kelvin**.
- Automatically fetches state information using **Zippopotam API** for zip codes.
- Caches API calls to improve performance.

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd weather-information-system
2.	Create a virtual environment (optional):
python -m venv env
source env/bin/activate  # On MacOS/Linux
env\Scripts\activate  # On Windows
