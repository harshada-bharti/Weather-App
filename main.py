
import requests

import os

API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)

        if response.status_code == 401:
            print("Invalid API key or the key is not active yet.")
            return

        response.raise_for_status()
        data = response.json()

        print("\n--- Weather Report ---")
        print(f"City: {data['name']}")
        print(f"Temperature: {data['main']['temp']} °C")
        print(f"Feels Like: {data['main']['feels_like']} °C")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Weather: {data['weather'][0]['description'].title()}")
        print(f"Wind Speed: {data['wind']['speed']} m/s")

    except requests.exceptions.HTTPError:
        print("City not found or the weather service returned an error.")
    except requests.exceptions.ConnectionError:
        print("Connection failed. Please check your internet.")
    except requests.exceptions.Timeout:
        print("The request timed out. Please try again.")
    except (KeyError, IndexError, ValueError):
        print("Could not read the weather data.")


if __name__ == "__main__":
    city = input("Enter city name: ").strip()

    if city:
        get_weather(city)
    else:
        print("Please enter a city name.")
