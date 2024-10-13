import requests
import streamlit as st
import os
from datetime import datetime

# Set up page configuration
st.set_page_config(page_title="Reuben's Weather Information System", layout="wide")

# Cache the API key retrieval since it doesn't change
@st.cache_data
def get_api_key():
    api_key = os.getenv('API_KEY')  # Fetch from environment/secrets
    if not api_key:
        st.error("API key not found. Please ensure it is correctly configured.")
    return api_key

API_KEY = get_api_key()

# Function to display the current date and time using Python's datetime
def display_local_date():
    now = datetime.now()  # Get the current local time
    st.sidebar.write(f"### Current Date and Time: {now.strftime('%Y-%m-%d %H:%M:%S')}")

# Cache the results of HTTP requests to reduce redundant API calls
@st.cache_data
def request(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"HTTP connection problem: {e}")
        return None

# Function to choose the temperature unit
def choose_temp(unit_choice):
    return {'Celsius': 'metric', 'Fahrenheit': 'imperial', 'Kelvin': 'standard'}.get(unit_choice, 'metric')

# Lookup weather by city name
def geo_lookup_city(city_name, state_code, unit):
    if not API_KEY:
        return
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},US&appid={API_KEY}"
    city_info = request(url)

    if city_info:
        city_display = f"{city_info[0]['name']}, {city_info[0].get('state', state_code)}"
        fetch_weather_data(city_info[0]['lat'], city_info[0]['lon'], unit, city_display)

# Fetch state and city from Zippopotam API
@st.cache_data
def get_state_from_zip(zip_code):
    url = f"https://api.zippopotam.us/us/{zip_code}"
    data = request(url)

    if data:
        state = data['places'][0]['state abbreviation']
        city = data['places'][0]['place name']
        return city, state
    return None, None

# Lookup weather by zip code
def geo_lookup_zip(zip_code, unit):
    if not API_KEY:
        return
    url = f"http://api.openweathermap.org/geo/1.0/zip?zip={zip_code},US&appid={API_KEY}"
    zip_data = request(url)

    if zip_data:
        city_name = zip_data.get('name', 'Unknown City')
        state_code = zip_data.get('state', None)

        if not state_code:
            city_name, state_code = get_state_from_zip(zip_code)

        city_display = f"{city_name}, {state_code if state_code else 'Unknown State'}"
        fetch_weather_data(zip_data['lat'], zip_data['lon'], unit, city_display)

# Fetch and display weather data
@st.cache_data
def fetch_weather_data(latitude, longitude, unit, city_display):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_KEY}&units={unit}"
    weather_data = request(url)

    if weather_data and weather_data.get('cod') == 200:
        temp = weather_data['main']['temp']
        feel_like = weather_data['main']['feels_like']
        temp_max = weather_data['main']['temp_max']
        temp_min = weather_data['main']['temp_min']
        pressure = weather_data['main']['pressure']
        humidity = weather_data['main']['humidity']
        cloud_cover = weather_data['clouds']['all']
        description = weather_data['weather'][0]['description']
        wind_speed = weather_data['wind']['speed']

        st.subheader(f'Weather Information for {city_display}')
        display_local_date()
        st.markdown(
            f"""
            **Temperature:** {temp}°  
            **Feels Like:** {feel_like}°  
            **High Temperature:** {temp_max}°  
            **Low Temperature:** {temp_min}°  
            **Pressure:** {pressure} hPa  
            **Humidity:** {humidity}%  
            **Cloud Cover:** {cloud_cover}%  
            **Description:** {description.capitalize()}  
            **Wind Speed:** {wind_speed} m/s  
            """,
            unsafe_allow_html=True,
        )

# Main function to run the Streamlit app
def main():
    st.title("Reuben's Weather Information System")

    # Display the local date and time from the user's computer

    # Sidebar input options
    lookup_choice = st.sidebar.radio("Select lookup method", ["City Name", "Zip Code"])
    unit_choice = st.sidebar.selectbox("Select Temperature Unit", ["Celsius", "Fahrenheit", "Kelvin"])
    unit = choose_temp(unit_choice)

    if lookup_choice == "City Name":
        col1, col2, _ = st.columns([2, 1, 3])
        with col1:
            city_name = st.text_input("City Name:", max_chars=20, placeholder="e.g., New York")
        with col2:
            state_code = st.text_input("State Code:", max_chars=2, placeholder="e.g., NY")
        if st.button("Get Weather by City"):
            if city_name and state_code:
                geo_lookup_city(city_name.strip(), state_code.strip(), unit)
            else:
                st.error("Please provide both city name and state code.")

    elif lookup_choice == "Zip Code":
        col1, _ = st.columns([2, 4])
        with col1:
            zip_code = st.text_input("Zip Code:", max_chars=5, placeholder="e.g., 10001")
        if st.button("Get Weather by Zip Code"):
            if zip_code.isdigit() and len(zip_code) == 5:
                geo_lookup_zip(zip_code, unit)
            else:
                st.error("Please provide a valid 5-digit zip code.")

if __name__ == '__main__':
    main()
