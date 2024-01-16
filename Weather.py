from requests import get
from io import BytesIO
from datetime import datetime
from PIL import Image, ImageTk
from customtkinter import IntVar

class Weather():
    def __init__(self):
        self.API_KEY = '03aa38b51b48e7908b44a12ac6ff2c55'
        self.FORECAST_BASE_URL = 'https://api.openweathermap.org/data/2.5/forecast'
        self.MAP_BASE_URL = 'https://tile.openweathermap.org/map'
        self.AIR_BASE_URL = 'http://api.openweathermap.org/data/2.5/air_pollution/forecast'

        self.start_day = datetime.now().weekday()
        self.initial_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

        self.country = 'Turkey'
        self.city = 'Ankara'
        self.alpha_2 = 'TR'
        self.units = 'Metric'

        self.map_index = 2

        self.days = [self.initial_days[(self.start_day + i) % 7] for i in range(5)]
        self.current_day = self.days[0]
        self.day_index = self.days.index(self.current_day) * 8

        self.weather_data = self.get_weather_data()

        self.lat = self.weather_data["city"]["coord"]["lat"]
        self.lon = self.weather_data["city"]["coord"]["lon"]

        self.air_pollution_data = self.get_air_pollution_data()
        self.map_data = self.get_map_data()

        self.get_unit_symbol()
        self.selected_units = IntVar()

        self.get_forecast()
        self.get_air_pollution()
        self.get_map()

        self.hours = [self.weather_data["list"][index]["dt_txt"].split()[1][:-3] for index in range(self.day_index, self.day_index + 8)]
        self.hour_index = 0
        self.current_hour_index = 0
    
    def get_unit_symbol(self):
        if self.units == 'Metric':
            self.temp_symbol =  '°C'
            self.wind_symbol = 'm/s'
            self.pressure_symbol = 'hPa'
        elif self.units == 'Imperial':
            self.temp_symbol = '°F'
            self.wind_symbol = 'mph'
            self.pressure_symbol = 'inHg'

    def get_map(self):
        self.map = self.map_data[self.map_index]

    def get_weather_data(self):
        url = f"{self.FORECAST_BASE_URL}?q={self.city}&units={self.units}&appid={self.API_KEY}"
        request = get(url)
        response = request.json()
        return response
    
    def get_air_pollution_data(self):
        url = f"{self.AIR_BASE_URL}?lat={self.lat}&lon={self.lon}&appid={self.API_KEY}"
        request = get(url)
        response = request.json()
        return response

    def get_forecast(self):
        self.curr_temps = [int(self.weather_data["list"][index]["main"]["temp"]) for index in range(40)]
        self.min_temps = [int(self.weather_data["list"][index]["main"]["temp_min"]) for index in range(40)]
        self.max_temps = [int(self.weather_data["list"][index]["main"]["temp_max"]) for index in range(40)]
        self.feels_likes = [int(self.weather_data["list"][index]["main"]["feels_like"]) for index in range(40)]
        self.humidities = [self.weather_data["list"][index]["main"]["humidity"] for index in range(40)]
        self.pressures = [self.weather_data["list"][index]["main"]["pressure"] for index in range(40)]
        self.wind_speeds = [self.weather_data["list"][index]["wind"]["speed"] for index in range(40)]
        self.weather_details = [self.weather_data["list"][index]["weather"][0]["description"] for index in range(40)]
        self.ground_levels = [self.weather_data["list"][index]["main"]["grnd_level"] for index in range(40)]

    def get_air_pollution(self):
        self.air_qualities = [self.air_pollution_data["list"][index]["main"]["aqi"] for index in range(40)]
        self.cos = [self.air_pollution_data["list"][index]["components"]["co"] for index in range(40)]
        self.nos = [self.air_pollution_data["list"][index]["components"]["no"] for index in range(40)]
        self.no2s = [self.air_pollution_data["list"][index]["components"]["no2"] for index in range(40)]
        self.o3s = [self.air_pollution_data["list"][index]["components"]["o3"] for index in range(40)]
        self.so2s = [self.air_pollution_data["list"][index]["components"]["so2"] for index in range(40)]
        self.pm2_5s = [self.air_pollution_data["list"][index]["components"]["pm2_5"] for index in range(40)]
        self.pm10s = [self.air_pollution_data["list"][index]["components"]["pm10"] for index in range(40)]
        self.nh3s = [self.air_pollution_data["list"][index]["components"]["nh3"] for index in range(40)]

    def get_map_data(self):
        z = 0
        y = 0
        x = 0

        layer = 'clouds_new'
        url = f"{self.MAP_BASE_URL}/{layer}/{z}/{y}/{x}/.png?appid={self.API_KEY}"
        response = get(url)
        img_data = BytesIO(response.content)
        self.clouds_map = ImageTk.PhotoImage(Image.open(img_data).resize((450,280)))

        layer = 'precipitation_new'
        url = f"{self.MAP_BASE_URL}/{layer}/{z}/{y}/{x}/.png?appid={self.API_KEY}"
        response = get(url)
        img_data = BytesIO(response.content)
        self.precipitation_map = ImageTk.PhotoImage(Image.open(img_data).resize((450,280)))

        layer = 'pressure_new'
        url = f"{self.MAP_BASE_URL}/{layer}/{z}/{y}/{x}/.png?appid={self.API_KEY}"
        response = get(url)
        img_data = BytesIO(response.content)
        self.pressure_map = ImageTk.PhotoImage(Image.open(img_data).resize((450,280)))

        layer = 'wind_new'
        url = f"{self.MAP_BASE_URL}/{layer}/{z}/{y}/{x}/.png?appid={self.API_KEY}"
        response = get(url)
        img_data = BytesIO(response.content)
        self.wind_map = ImageTk.PhotoImage(Image.open(img_data).resize((450,280)))

        layer = 'temp_new'
        url = f"{self.MAP_BASE_URL}/{layer}/{z}/{y}/{x}/.png?appid={self.API_KEY}"
        response = get(url)
        img_data = BytesIO(response.content)
        self.temp_map = ImageTk.PhotoImage(Image.open(img_data).resize((450,280)))

        return [self.clouds_map, self.precipitation_map, self.pressure_map, self.wind_map, self.temp_map]