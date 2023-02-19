import requests
import os
import re
from datetime import datetime, timedelta

# Get API key from environment variable
# make sure you have exported your key- export OPEN_WEATHER_API_KEY=your_api_key_here
api_key = os.environ['OPEN_WEATHER_API_KEY']

url = 'http://api.openweathermap.org/data/2.5/forecast'

# user input e.g. valid zip code = 10001, 10002, 10004
zip_code = input('Enter zip code: ')

# validate zip code using regular expressions
#regular expression r"^\d{5}(?:[-\s]\d{4})?$" matches any string that starts with 5 digits
if not re.match(r"^\d{5}(?:[-\s]\d{4})?$", zip_code):
    print("Invalid zip code. Please enter a valid zip code.")
    exit()

# Make API call with zip code
response = requests.get(url, params={'zip': zip_code, 'appid': api_key, 'units': 'imperial'})

# Check if response is successful
if response.status_code == 200:

   # Parse JSON response from API call
    response_data = response.json()
    if response_data['cod'] == '404':
        print(response_data['message'])
        exit()
    data = response_data['list']
    city_name = response_data['city']['name']

    # Create dictionary to store data for each unique date
    forecast_data = {}

    # Iterate over list of forecasts and add data to dictionary
    for forecast in data:
        date = datetime.fromtimestamp(forecast['dt']).date()
        high_temp = forecast['main']['temp_max']
        low_temp = forecast['main']['temp_min']
        precipitation = forecast.get('rain', {'3h': 0}).get('3h') + forecast.get('snow', {'3h': 0}).get('3h')
        if date not in forecast_data:
            forecast_data[date] = {'high_temp': high_temp, 'low_temp': low_temp, 'precipitation': precipitation}
        else:
            if high_temp > forecast_data[date]['high_temp']:
                forecast_data[date]['high_temp'] = high_temp
            if low_temp < forecast_data[date]['low_temp']:
                forecast_data[date]['low_temp'] = low_temp
            forecast_data[date]['precipitation'] += precipitation
    

    # Display forecast data
    print(f'\033[1;32mForecast for {city_name}:\033[0m')
    print('\033[1;32mDate\t\tTemperature\tPrecipitation\033[0m')  
    for date, data in forecast_data.items():
        print(f'{date.strftime("%m/%d/%Y")}\t{int(data["high_temp"])}°/{int(data["low_temp"])}°\t\t{data["precipitation"]:.2f} in')
        
        
else:
    # Handle 404 response
    if response.json()['cod'] == "404":
        print("City not found. Please enter a valid zipcode.")
    # Handle 401 response    
    elif response.json()['cod'] == "401":
        print("Invalid API key. Pls refer API documentation for more info!")    
    else:
        print("Error fetching data from API. Pls refer API documentation for more info!")        