import requests
import json
import datetime

# Program purpose: Display weather data user for specified location( City or Zip)
# Author: Reuben Martor
# Date: 2/18/2023

def display_date():
    now = datetime.datetime.now()
    print(f"Current date and time : {now.strftime('%m-%d-%Y %H:%M:%S')}")

def request(url):  # create a connection object to test http connection to location or weather API endpoints
    try:
        response = requests.get(url)
    except:
        print('HTTP CONNECTION PROBLEM: ', response.status_code)
    else:
        print(f'\nHTTP CONNECTION HAS BEEN ESTABLISHED. REQUEST CODE: ', response.status_code)
        return response


def welcome_user():  # great user
    print("\nWelcome to Reuben's weather information system. The program provides weather information of a given city.\
It is designed for cities in the United States only.\r")


def choose_temp(choice):  # ask user to select unit of temperature to display weather data
    choice = (choice).lower()
    if choice == 'c':
        temp_unit = 'metric' # temp in celcius
    elif choice == 'f':
        temp_unit = 'imperial' # temp in Fahrenheit
    elif choice == 'k':
        temp_unit = 'standard' # temp in kelvin incase someone needs it
    return temp_unit


def geo_look_up_name(city_name, state_code, api_key, unit):  # get lat & lon for city to obtain weather data
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},US&appid={api_key}"
    response = request(url)
    try:
        city_data = response.json()
    except Exception as ex:
        print('There was a problem making HTTP request to location', ex)

    else:
        data = {}  # create a dict to extract dict items within list
        for item in city_data:
            data.update(item)
        city = data['name']
        latitude = data['lat']
        longitude = data['lon']
        state = data['state']
        print('\nLocation information')
        print('--------------------')
        print(f"{city}, {state}")
        print(f"Latitude: {latitude}")
        print(f"Longitude: {longitude}")

         # This is a url to obtain weather data for look up by city name
        url_weather = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&units={unit}"
        city_name_response = request(url_weather)
        try:
            city_weather_data = city_name_response.json()

        except Exception as ex:
            print('There was a problem making HTTP request to weather source', ex)

        else:
            if city_weather_data['cod'] == "404":
                print('No city found')
            else:

                temp = city_weather_data['main']['temp']
                feel_like = city_weather_data['main']['feels_like']
                temp_min = city_weather_data['main']['temp_min']
                temp_max = city_weather_data['main']['temp_max']
                pressure = city_weather_data['main']['pressure']
                humidity = city_weather_data['main']['humidity']
                cloud_cover = city_weather_data['clouds']['all']
                if cloud_cover >= 90:
                    cloud_cover = 'cloudy'
                elif cloud_cover >= 70:
                    cloud_cover = "Mostly Cloudy"
                elif cloud_cover > 30:
                    cloud_cover = "Partly Cloudy/Partly Sunny"
                else:
                    cloud_cover = "Clear"
                description = city_weather_data['weather'][0]['description']
                wind_speed = city_weather_data['wind']['speed']
                display_date()
                print()
                print('Current Weather Information')
                print('--------------------')
                print(f'Temperature: {temp}{chr(176)}')
                print(f'Feels Like: {feel_like}{chr(176)}')
                print(f'High Temperature: {temp_max}{chr(176)}')
                print(f'Low Temperature: {temp_min}{chr(176)}')
                print(f'Pressure: {pressure} hPa')
                print(f'Humidity: {humidity}%')
                print(f'Clove Cover: {cloud_cover}')
                print(f'Description: {description}')
                print(f'Wind speed: {wind_speed} ')


def geo_look_up_zip(zip_code, api_key, unit):  # look up weather by city zip code
    url = f'http://api.openweathermap.org/geo/1.0/zip?zip={zip_code},US&appid={api_key}' #geo look up for zip code

    zip_response = request(url)
    try:
        zip_data = zip_response.json() #obtain json (dictionary) to extract lat/lon
    except Exception as ex:
        print('There was a problem making HTTP request to location', ex)
    else:
        city = zip_data['name']
        latitude = zip_data['lat']
        longitude = zip_data['lon']
        print('Location information')
        print('--------------------')
        print(f"{city}")
        print(f"Latitude: {latitude}")
        print(f"Longitude: {longitude}")

         # # This is a url to obtain weather data for look up by zip code
        url_weather = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&units={unit}"

        city_zip_response = request(url_weather)
        try:
            city_weather_data = city_zip_response.json()
        except Exception as ex:
            print('There was a problem making HTTP request to location', ex)
        else:
            if city_weather_data['cod'] == "404":  # double check for connection problem or validate location
                print('No city found or problem with data source')
            else:
                temp = city_weather_data['main']['temp']
                feel_like = city_weather_data['main']['feels_like']
                temp_min = city_weather_data['main']['temp_min']
                temp_max = city_weather_data['main']['temp_max']
                pressure = city_weather_data['main']['pressure']
                humidity = city_weather_data['main']['humidity']
                cloud_cover = city_weather_data['clouds']['all']
                if cloud_cover >= 90:
                    cloud_cover = 'cloudy'
                elif cloud_cover >= 70:
                    cloud_cover = "Mostly Cloudy"
                elif cloud_cover > 30:
                    cloud_cover = "Partly Cloudy/Partly Sunny"
                else:
                    cloud_cover = "Clear"
                description = city_weather_data['weather'][0]['description']
                wind_speed = city_weather_data['wind']['speed']
                display_date()
                print()
                print('Current Weather Information')
                print('----------------------')
                print(f'Temperature: {temp}{chr(176)}')
                print(f'It feels like: {feel_like}{chr(176)}')
                print(f'High Temperature: {temp_max}{chr(176)}')
                print(f'Low Temperature: {temp_min}{chr(176)}')
                print(f'Pressure: {pressure}hPa')
                print(f'Humidity: {humidity}%')
                print(f'Clove Cover: {cloud_cover}')
                print(f'Description: {description}')
                print(f'Wind speed: {wind_speed} ')


def main():
    api_key = "06a941e071d1e5a54da69f7a5a36641d"

    prompt = 'y'
    welcome_user()
    while prompt.lower() == 'y':
        try:
            lookup_choice = input('Type 1 for city name or 2 for zip code or "quit" to exit: ')
            if lookup_choice.lower() =='quit':
                print("Thank you for using Reuben's weather application. Goodbye!")
                exit()
            elif lookup_choice == 1 or 2:
                lookup_choice = int(lookup_choice)
            else:
                print('Wrong selection')
        except ValueError:
            print('invalid input type. ')

        else:
            if lookup_choice == 1:
                try:
                    city_name = input('Enter City name: '.strip())
                    if city_name.isdigit():
                        print('city name must be a string and not a digit(s)')
                        continue
                    state_code = input('Enter state code or name. Must be two Letters ex "IA" or "Iowa: '.strip())
                    if state_code.isdigit():
                        print('state name or code must be a string and not a digit(s)')
                    while len(state_code) < 2:
                        print('state code or name cannot be less than 2 letters.')
                        state_code = input('Enter state code or name. Must be two Letters ex "IA" or "Iowa: '.strip())

                    choice = input('Unit for temperature: C for Celsius, F for Fahrenheit, K for Kelvin: ')
                    choice_list = ['c', 'f', 'k']  # list for input validation
                    while not choice in choice_list:
                        print('invalid selection. Temp must be C, F, or K')
                        choice = input('Unit for temperature: C for Celsius, F for Fahrenheit, K for Kelvin: ')
                    else:
                        choose_temp(choice)
                        geo_look_up_name(city_name, state_code, api_key,
                                         choose_temp(choice))  # look up weather by city name
                        prompt = input('Do you want to look up another city ? y/n: ')
                except Exception as e:
                    print('unable to obtain weather information for location given, ', e)

            elif lookup_choice == 2:
                try:
                    city_zip = (input('Enter zip code: '))
                    while not len(city_zip) == 5:
                        print('Zip code must be 5 digit numbers')
                        city_zip = (input('Enter zip code: '))
                    else:
                        city_zip = int(city_zip)

                except:
                    print('You either did not type or you entered some invalid characters')
                    continue
                else:
                    choice = input('Unit for temperature: C for Celsius, F for Fahrenheit, K for Kelvin: ')
                    choice_list = ['c', 'f', 'k']
                    while not choice in choice_list:
                        print('invalid selection. Temp must be C, F, or K')
                        choice = input('Unit for temperature: C for Celsius, F for Fahrenheit, K for Kelvin: ')
                    choose_temp(choice)
                    geo_look_up_zip(city_zip, api_key, choose_temp(choice))
                    prompt = input('Do you want to look up another city ? y/n: ')

            else:
                print('Please choose from the options indicated')
                continue

            if prompt == 'n':
                print("Thank you for using Reuben's weather application. Goodbye!")
                exit()
            # else:
            #     print('invalid selection! ')
            #     prompt = input('Do you want to look up another city ? y/n: ')


if __name__ == '__main__':
    main()
