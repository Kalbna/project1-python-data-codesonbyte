import pandas as pd
import requests

# OpenWeatherMap API endpoint and API key
api_key = 'aec17148fc0f49f733d0d202418155b3'  # Replace 'YOUR_API_KEY_HERE' with your actual API key
city_name = 'New York'  # Replace 'New York' with the city you want to fetch data for
api_endpoint = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'

# Fetch weather data from the OpenWeatherMap API
response = requests.get(api_endpoint)
if response.status_code == 200:
    weather_data = response.json()
    # Extract relevant data from the API response
    weather_info = {
        'City': [weather_data['name']],
        'Country': [weather_data['sys']['country']],
        'Temperature (Celsius)': [weather_data['main']['temp'] - 273.15],  # Convert temperature to Celsius
        'Humidity (%)': [weather_data['main']['humidity']],
        'Wind Speed (m/s)': [weather_data['wind']['speed']]
    }

    # Create a DataFrame from the weather information
    df = pd.DataFrame(weather_info)

    # Save the DataFrame to a CSV file
    df.to_csv('weather_data.csv',sep=",", index=False)
    print("Weather data saved to 'weather_data.csv' file.")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
