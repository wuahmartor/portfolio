import requests
import datetime
import streamlit as st
import pandas as pd

st.set_page_config(page_title="US Weather Info", layout="wide")

# Securely read the API key from a file
@st.cache_data
def get_api_key(file_path='ap_file.txt'):
    try:
        with open(file_path, 'r') as f:
            api_key = f.read().strip()
        return api_key
    except FileNotFoundError:
        st.error("API key file not found. Please ensure 'ap_file.txt' is present.")
        return None

API_KEY = get_api_key()

# Load and process city-zip data
@st.cache_data
def load_city_zip_data():
    data = pd.read_csv('uscities_zips.csv')

    # Handle NaN values in the 'zips' column and split by comma
    data = data.dropna(subset=['zips'])  # Drop rows where 'zips' is NaN
    data['zips'] = data['zips'].str.split(',').explode().str.strip()  # Split and explode

    # Filter to ensure only valid 5-digit zip codes
    data = data[data['zips'].str.match(r'^\d{5}$', na=False)]  # Avoid NaN-related errors

    # Drop any remaining duplicates
    valid_data = data[['city', 'state_id', 'zips']].drop_duplicates()
    return valid_data

uscity_zip = load_city_zip_data()

# Display the current date and time
def display_date():
    now = datetime.datetime.now()
    st.write(f"**Current date and time:** {now.strftime('%m-%d-%Y %H:%M:%S')}")

# Make API request
def request(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        st.error(f"HTTP connection issue: {e}")

# Select temperature unit
def choose_temp(unit):
    return {'Celsius': 'metric', 'Fahrenheit': 'imperial', 'Kelvin': 'standard'}.get(unit, 'standard')

# Fetch and display weather data with city and state information
def fetch_weather_data(latitude, longitude, unit, city_name=None, state_id=None):
    url_weather = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_KEY}&units={unit}"
    response = request(url_weather)

    if response:
        weather_data = response.json()
        if weather_data.get('cod') == 200:
            temp = weather_data['main']['temp']
            feel_like = weather_data['main']['feels_like']
            temp_min = weather_data['main']['temp_min']
            temp_max = weather_data['main']['temp_max']
            pressure = weather_data['main']['pressure']
            humidity = weather_data['main']['humidity']
            description = weather_data['weather'][0]['description']
            wind_speed = weather_data['wind']['speed']

            # Display weather data along with city and state
            display_date()
            st.markdown(
                f"""
                **City:** {city_name}, {state_id}\n  
                
                **Temperature:** {temp}°  
                **Feels Like:** {feel_like}°  
                **High Temperature:** {temp_max}°  
                **Low Temperature:** {temp_min}°  
                **Pressure:** {pressure} hPa  
                **Humidity:** {humidity}%  
                **Description:** {description.capitalize()}  
                **Wind Speed:** {wind_speed} m/s  
                """, unsafe_allow_html=True
            )
        else:
            st.error("City not found. Please try again.")
# Lookup weather by city
def geo_lookup_city(city_name, state_id, unit):
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_id},US&appid={API_KEY}"
    response = request(url)

    if response:
        city_data = response.json()
        if city_data:
            city_info = city_data[0]
            latitude, longitude = city_info['lat'], city_info['lon']
            fetch_weather_data(latitude, longitude, unit)
        else:
            st.error("Invalid city. Please select a valid US city.")



# Lookup weather by zip code and display city and state
def geo_lookup_zip(zip_code, unit):
    # Get city and state associated with the selected zip code
    location = uscity_zip[uscity_zip['zips'] == zip_code].iloc[0]
    city_name, state_id = location['city'], location['state_id']

    url = f"http://api.openweathermap.org/geo/1.0/zip?zip={zip_code},US&appid={API_KEY}"
    response = request(url)

    if response:
        zip_data = response.json()
        latitude, longitude = zip_data['lat'], zip_data['lon']
        fetch_weather_data(latitude, longitude, unit, city_name, state_id)
    else:
        st.error("Invalid zip code. Please select a valid US zip code.")

# Streamlit main function
def main():
    st.title("US Weather Information System")
    col1, col2 = st.columns(2)

    # Sidebar options
    lookup_choice = st.sidebar.radio("Select lookup method", ["City Name", "Zip Code"])
    unit_choice = st.sidebar.selectbox("Select Temperature Unit", ["Celsius", "Fahrenheit", "Kelvin"])
    unit = choose_temp(unit_choice)

    if lookup_choice == "City Name":
        with col1:
            city_name = st.selectbox("Select City", uscity_zip['city'].unique())
            state_id = st.selectbox("Select State Code", uscity_zip[uscity_zip['city'] == city_name]['state_id'].unique())
            if st.button("Get Weather by City"):
                geo_lookup_city(city_name, state_id, unit)

    elif lookup_choice == "Zip Code":
        with col1:
            # Ensure only valid 5-digit zip codes are shown
            zip_code = st.selectbox("Select Zip Code", uscity_zip['zips'].unique())
            if st.button("Get Weather by Zip Code"):
                geo_lookup_zip(zip_code, unit)

# Run the Streamlit app
if __name__ == '__main__':
    main()