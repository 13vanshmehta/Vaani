import requests
import json
import schedule
import time
from datetime import datetime

# Replace with your OpenWeatherMap API key
API_KEY = 'your_openweathermap_api_key'
BASE_URL = 'http://api.openweathermap.org/data/2.5/forecast/daily'

# Function to fetch 7-day weather forecast for a specific region in India
def fetch_weather_data(region):
    params = {
        'q': f"{region},IN",
        'cnt': 7,  # 7-day forecast
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        weather_data = response.json()
        return weather_data
    else:
        print("Failed to fetch data:", response.status_code)
        return None

# Function to save the forecast data to a JSON file
def save_forecast_to_json(region, weather_data):
    filename = f"{region}_7day_forecast_{datetime.now().strftime('%Y%m%d')}.json"
    with open(filename, 'w') as json_file:
        json.dump(weather_data, json_file, indent=4)
    print(f"Weather data saved to {filename}")

# Main function to execute the data fetching and saving process
def main(region):
    weather_data = fetch_weather_data(region)
    if weather_data:
        save_forecast_to_json(region, weather_data)

# Schedule the script to run every 7 days
def schedule_forecast():
    region = 'Mumbai'  # Change this to your desired region
    schedule.every(7).days.do(main, region=region)
    
    print("Starting weather data fetch scheduler...")
    while True:
        schedule.run_pending()
        time.sleep(1)  # Check every second for scheduled tasks

# Run the scheduler
if __name__ == "__main__":
    schedule_forecast()
