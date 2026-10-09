# Weather App 🌦️

A Python application that fetches real-time weather information using the OpenWeather API.

## Features
- Current temperature
- Feels-like temperature
- Humidity
- Weather conditions
- Wind speed

## Technologies Used
- Python
- Requests library
- OpenWeather API

## How to Run
1. Install the required library: `pip install requests`
2. Set the `OPENWEATHER_API_KEY` environment variable.
3. Run the app: `python main.py`

## Author
Harshada Bharti# Weather App 🌦️

A Python application that fetches real-time weather information using the OpenWeather API.

## Features
- Current temperature
- Feels-like temperature
- Humidity
- Weather conditions
- Wind speed

## Technologies Used
- Python
- Requests library
- OpenWeather API

## How to Run
1. Install the required library: `pip install requests`
2. Set the `OPENWEATHER_API_KEY` environment variable.
3. Run the app: `python main.py`

## Author
Harshada Bharti
=======
# 🌦️ Weather App with Live OpenWeather API

A Python-based weather application that fetches real-time weather information for a selected city using the OpenWeather API. The application displays temperature, feels-like temperature, humidity, weather conditions, and wind speed. It also supports a 5-day forecast using forecast data from the API.

## 🚀 Features

- 🌡️ Displays current city temperature.
- 💧 Shows humidity and feels-like temperature.
- ☁️ Provides current weather conditions.
- 💨 Displays wind speed.
- 📅 Retrieves forecast data for the next five days.
- 🌐 Integrates with a REST API using Python Requests.
- 📄 Parses JSON responses from the weather service.
- ⚠️ Handles common API, connection, and input errors.

## 🛠️ Technologies Used

- **Python** – Application logic
- **Requests** – HTTP requests to the weather API
- **OpenWeather API** – Weather and forecast data
- **JSON** – API response parsing

## 📂 Project Structure

```text
weather-app/
│
├── main.py
├── README.md
└── .gitignore
```

The `.gitignore` file is recommended for keeping local configuration and secret files out of GitHub.

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the project folder

```bash
cd weather-app
```

### 3. Install the required dependency

```bash
pip install requests
```

### 4. Get an OpenWeather API key

Create an account at [OpenWeather](https://openweathermap.org/api) and generate an API key.

### 5. Configure your API key

Add your API key to `main.py` as shown below:

```python
API_KEY = "YOUR_API_KEY_HERE"
```

**Security note:** Never commit your real API key to a public repository. Use an environment variable or a local `.env` file excluded through `.gitignore` for safer configuration.

### 6. Run the application

```bash
python main.py
```

Enter a city name when prompted to view its weather information.

## 📊 Sample Output

```text
Enter city name: Pune

========== CURRENT WEATHER ==========
City: Pune
Temperature: 27.04 °C
Feels Like: 27.99 °C
Humidity: 58%
Condition: Few Clouds
Wind Speed: 0.27 m/s

========== 5-DAY FORECAST ==========
Forecast details will appear here.
```

*Sample values are illustrative. Actual results depend on the live API response.*

## 🎯 Learning Outcomes

- Understanding REST API integration.
- Sending HTTP requests using Python.
- Parsing JSON data.
- Working with external data services.
- Implementing error handling.
- Displaying structured weather information in the terminal.

## 🔮 Future Improvements

- Build a graphical interface using Tkinter.
- Add weather icons and a more attractive display.
- Move API credentials into environment variables.
- Allow users to save favorite cities.
- Improve daily forecast summaries.

## 👩‍💻 Author

**Harshada Bharti**

GitHub: [harshada-bharti](https://github.com/harshada-bharti)

---

*Built as a Python learning project to practice API integration, JSON parsing, and real-world data retrieval.*
>>>>>>> 94d072e6b1eca2366891e259f464a7f27c2c70b4
