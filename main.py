from customtkinter import FontManager, NSEW
from pycountry import countries
from pandas import read_csv
from Weather import Weather
from Window import *

class WeatherApp():
    def __init__(self):
        self.window = Window()
        self.weather = Weather()
        self.selection = 'Map'

        self.city_data = read_csv('./main_files/files/worldcities.csv')
        self.country_values = self.city_data['country'].unique()
        self.country_values.sort()
        self.city_values = self.city_data[self.city_data['country'] == self.weather.country]['city'].unique().tolist()
        self.city_values.sort()
        
        self.map_values = ['clouds_new', 'precipitation_new', 'pressure_new', 'wind_new', 'temp_new']
        self.primary_font = FontManager.load_font("./main_files/files/Champagne & Limousines Bold.ttf")
        self.secondary_font = FontManager.load_font("./main_files/files/Champagne & Limousines.ttf")

        self.config_layout()
        self.config_commands()
        self.update_elements()
        self.update_hourly(self.weather.hours[self.weather.current_hour_index])


    def update_time_buttons(self):
            self.window.root.hourly_air_button.set(self.weather.hours[self.weather.hour_index])
            self.window.root.hourly_button.set(self.weather.hours[self.weather.hour_index])

    def config_layout(self):
            self.window.root.day_button.configure(values=self.weather.days)
            self.window.root.map_button.configure(values=[value.split('_')[0] for value in self.map_values])
            self.window.root.hourly_button.configure(values=self.weather.hours)
            self.window.root.hourly_air_button.configure(values=self.weather.hours)
            self.window.root.map_button.set(self.map_values[self.weather.map_index][:-4])
            self.window.root.day_button.set(self.weather.current_day)
            self.window.root.selection_button.set(self.selection)
            self.window.root.unit_text.configure(text='Units')

            self.window.root.metric_radio_button.configure(text='Metric', variable=self.weather.selected_units, command=lambda: self.update_units('Metric'))
            self.window.root.imperial_radio_button.configure(text='Imperial', variable=self.weather.selected_units, command=lambda: self.update_units('Imperial'))
            self.window.root.metric_radio_button.select()
            self.update_map(self.map_values[self.weather.map_index])
            self.update_selection(self.selection)

            self.window.root.cuntry_menu = CTkScrollableDropdown(attach=self.window.root.country_button,values=self.country_values,button_height=32,hover_color='#323232',y=36,command=self.update_country)
            self.window.root.city_menu = CTkScrollableDropdown(attach=self.window.root.city_button,values=self.city_values,button_height=32,hover_color='#323232',y=36,command=self.update_city)
    
    def config_commands(self):
            self.window.root.selection_button.configure(command=self.update_selection)
            self.window.root.day_button.configure(command=self.update_day)
            self.window.root.map_button.configure(command= lambda map_type: self.update_map(f'{map_type}_new'))
            self.window.root.hourly_button.configure(command=self.update_hourly)
            self.window.root.hourly_air_button.configure(command=self.update_hourly)

    def update_elements(self): 
            self.window.root.country_button.configure(text=self.weather.country)
            self.window.root.city_button.configure(text=self.weather.city)
            self.window.root.temperature_label.configure(text=f"{self.weather.curr_temps[self.weather.day_index]} {self.weather.temp_symbol}")
            self.window.root.weather_details_label.configure(text=self.weather.weather_details[self.weather.day_index])
            self.window.root.wind_label.configure(text=f"wind: {self.weather.wind_speeds[self.weather.day_index]} {self.weather.wind_symbol}")
            self.window.root.humidity_label.configure(text=f"humidity: {self.weather.humidities[self.weather.day_index]}%")
            self.window.root.ground_level.configure(text=f"ground level: {self.weather.ground_levels[self.weather.day_index]} {self.weather.pressure_symbol}")
            self.window.root.pressure_label.configure(text=f"pressure: {self.weather.pressures[self.weather.day_index]} {self.weather.pressure_symbol}")
            self.window.root.temp_max_label.configure(text=f"max temp: {self.weather.max_temps[self.weather.day_index]} {self.weather.temp_symbol}")
            self.window.root.temp_min_label.configure(text=f"min temp: {self.weather.min_temps[self.weather.day_index]} {self.weather.temp_symbol}")
            self.window.root.feels_like_label.configure(text=f"feels like: {self.weather.feels_likes[self.weather.day_index]} {self.weather.temp_symbol}")
            self.window.root.city_label.configure(text=f"{self.weather.city}, {self.weather.alpha_2.upper()}")

    def update_units(self, units):
        self.weather.units = units
        self.weather.get_unit_symbol()
        self.weather.weather_data = self.weather.get_weather_data()
        self.weather.get_forecast()
        self.update_elements()

    def update_hourly(self, hour):
        self.weather.hour_index = self.weather.hours.index(hour)
        self.weather.current_hour_index = self.weather.hour_index + self.weather.day_index
        self.update_time_buttons()

        self.window.root.hourly_temprature.configure(text=f"temprature: {self.weather.curr_temps[self.weather.current_hour_index]} {self.weather.temp_symbol}")
        self.window.root.hourly_min_temprature.configure(text=f"min temprature: {self.weather.min_temps[self.weather.current_hour_index]} {self.weather.temp_symbol}")
        self.window.root.hourly_max_temprature.configure(text=f"max temprature: {self.weather.max_temps[self.weather.current_hour_index]} {self.weather.temp_symbol}")
        self.window.root.hourly_feels_like.configure(text=f"feels like: {self.weather.feels_likes[self.weather.current_hour_index]} {self.weather.temp_symbol}")
        self.window.root.hourly_humidity.configure(text=f"humidity: {self.weather.humidities[self.weather.current_hour_index]}%")
        self.window.root.hourly_pressure.configure(text=f"pressure: {self.weather.pressures[self.weather.current_hour_index]}{self.weather.pressure_symbol}")
        self.window.root.hourly_weather_details.configure(text=f"weather details: {self.weather.weather_details[self.weather.current_hour_index]}")
        self.window.root.hourly_ground_level.configure(text=f"ground level: {self.weather.ground_levels[self.weather.current_hour_index]} {self.weather.pressure_symbol}")

        self.window.root.air_pollution_air_quality.configure(text=f"air quality: {self.weather.air_qualities[self.weather.current_hour_index]}")
        self.window.root.air_pollution_co.configure(text=f"co: {self.weather.cos[self.weather.current_hour_index]}μg/m3")
        self.window.root.air_pollution_no.configure(text=f"no: {self.weather.nos[self.weather.current_hour_index]}μg/m3")
        self.window.root.air_pollution_no2.configure(text=f"no2: {self.weather.no2s[self.weather.current_hour_index]}μg/m3")
        self.window.root.air_pollution_o3.configure(text=f"o3: {self.weather.o3s[self.weather.current_hour_index]}μg/m3")
        self.window.root.air_pollution_pm2_5.configure(text=f"pm2.5: {self.weather.pm2_5s[self.weather.current_hour_index]}μg/m3")
        self.window.root.air_pollution_so2.configure(text=f"so2: {self.weather.so2s[self.weather.current_hour_index]}μg/m3")
        self.window.root.air_pollution_pm10.configure(text=f"pm10: {self.weather.pm10s[self.weather.current_hour_index]}μg/m3")
        self.window.root.air_pollution_nh3.configure(text=f"nh3: {self.weather.nh3s[self.weather.current_hour_index]}μg/m3")
    
    def update_selection(self, selection):
        if selection == 'Map':
            self.window.root.air_pollution_frame.grid_forget()
            self.window.root.hourly_frame.grid_forget()

            self.window.root.map_frame.grid(row=4, column=0, pady=8, padx=16, columnspan=2, sticky=NSEW)
            self.window.root.map_frame.grid_rowconfigure((0,1), weight=1)
            self.window.root.map_frame.grid_columnconfigure((0,1,2), weight=1)
            
        elif selection == 'Hourly Forecast':
            self.window.root.air_pollution_frame.grid_forget()
            self.window.root.map_frame.grid_forget()

            self.window.root.hourly_frame.grid(row=4, column=0, pady=8, padx=16, columnspan=2, sticky=NSEW)
            self.window.root.hourly_frame.grid_rowconfigure((0,1,2,3), weight=1)
            self.window.root.hourly_frame.grid_columnconfigure((0,1,2), weight=1)

        elif selection == 'Air Pollution':
            self.window.root.map_frame.grid_forget()
            self.window.root.hourly_frame.grid_forget()

            self.window.root.air_pollution_frame.grid(row=4, column=0, pady=8, padx=16, columnspan=2, sticky=NSEW)
            self.window.root.air_pollution_frame.grid_rowconfigure((0,1,2,3,4,5,6), weight=1)
            self.window.root.air_pollution_frame.grid_columnconfigure((0,1,2), weight=1)

    def update_country(self, country):
        self.weather.country = country
        self.weather.alpha_2 = self.city_data[self.city_data['country'] == self.weather.country]['iso2'].unique().tolist()[0]
        self.city_values = self.city_data[self.city_data['country'] == self.weather.country]['city'].unique().tolist()
        self.weather.city = self.city_values[0]
        self.window.root.city_menu.configure(values=self.city_values)
        self.weather.weather_data = self.weather.get_weather_data()
        self.weather.air_pollution_data = self.weather.get_air_pollution_data()
        self.weather.get_forecast()
        self.weather.get_air_pollution()
        self.update_elements()

    def update_city(self, city):
        self.weather.city = city
        self.weather.weather_data = self.weather.get_weather_data()
        self.weather.air_pollution_data = self.weather.get_air_pollution_data()
        self.weather.get_forecast()
        self.weather.get_air_pollution()
        self.update_elements()

    def update_day(self, selected_day):
        self.weather.current_day = selected_day
        self.weather.day_index = self.weather.days.index(self.weather.current_day) * 8
        self.weather.current_hour_index = self.weather.hour_index + self.weather.day_index
        self.update_elements()

    def update_map(self, map_type):
        self.weather.map_index = self.map_values.index(map_type)
        self.weather.get_map()
        self.window.root.map_canvas.itemconfig('map', image=self.weather.map)

    def build(self):
        self.window.root.mainloop()

if __name__ == '__main__':
    app = WeatherApp()
    app.build()