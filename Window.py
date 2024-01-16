from customtkinter import CTkFrame, NSEW, set_default_color_theme, CTk
from PIL import Image, ImageTk
from CTkWidgets import *
from CTkScrollableDropdown import *

class Window():
    def __init__(self):
        self.root = CTk()
        self.icon = ImageTk.PhotoImage(Image.open('./main_files/files/rain.ico'))

        self.root._set_appearance_mode('dark')
        set_default_color_theme("dark-blue")
        
        self.root.title("Verde Weather")
        self.root.iconphoto(False, self.icon)

        self.root.geometry("522x928")
        self.root.resizable(False, False)

        self.grid_config()
        self.create_elements()
        self.grid_elements()

    def grid_config(self):
        self.root.grid_rowconfigure((0, 1, 2, 3, 4, 5), pad=16, weight=1)
        self.root.grid_columnconfigure((0,1), weight=1)

        self.root.top_frame = CTkFrame(master=self.root, corner_radius=28, border_width=0)
        self.root.unit_frame = CTkFrame(master=self.root, corner_radius=28, border_width=0)
        self.root.temp_frame = CTkFrame(master=self.root, corner_radius=28, border_width=0)
        self.root.day_frame = CTkFrame(master=self.root, corner_radius=28, border_width=0)
        self.root.info_frame = CTkFrame(master=self.root, corner_radius=28, border_width=0)
        self.root.selection_frame = CTkFrame(master=self.root, corner_radius=28, border_width=0)
        self.root.map_frame = CTkFrame(master=self.root, corner_radius=28, border_width=0)
        self.root.hourly_frame = CTkFrame(master=self.root, corner_radius=28, border_width=0)
        self.root.air_pollution_frame = CTkFrame(master=self.root, corner_radius=28, border_width=0)
        self.root.bottom_frame = CTkFrame(master=self.root, corner_radius=28, border_width=0)

        self.root.top_frame.grid(row=0, column=1, pady=8, padx=8, sticky=NSEW)
        self.root.top_frame.grid_rowconfigure((0,1), weight=1)
        self.root.top_frame.grid_columnconfigure((0,1,2,3), weight=1)

        self.root.unit_frame.grid(row=0, column=0, pady=8, padx=8, sticky=NSEW)
        self.root.unit_frame.grid_rowconfigure((0,1,2,3,4), weight=1)
        self.root.unit_frame.grid_columnconfigure((0,1,2), weight=1)

        self.root.temp_frame.grid(row=1, column=0, pady=8, padx=16, columnspan=2, sticky=NSEW)
        self.root.temp_frame.grid_rowconfigure((0, 1), weight=1)
        self.root.temp_frame.grid_columnconfigure(0, weight=1)

        self.root.info_frame.grid(row=2, column=0, pady=8, padx=16, columnspan=2, sticky=NSEW)
        self.root.info_frame.grid_rowconfigure((0, 1, 2), weight=1)
        self.root.info_frame.grid_columnconfigure((0, 1), weight=1)

        self.root.selection_frame.grid(row=3, column=0, pady=8, padx=16, columnspan=2, sticky=NSEW)
        self.root.selection_frame.grid_rowconfigure((0,1,2), weight=1)
        self.root.selection_frame.grid_columnconfigure((0,1,2), weight=1)

        self.root.map_frame.grid(row=4, column=0, pady=8, padx=16, columnspan=2, sticky=NSEW)
        self.root.map_frame.grid_rowconfigure((0,1), weight=1)
        self.root.map_frame.grid_columnconfigure((0,1,2), weight=1)

        self.root.hourly_frame.grid(row=4, column=0, pady=8, padx=16, columnspan=2, sticky=NSEW)
        self.root.hourly_frame.grid_rowconfigure((0,1,2,3), weight=1)
        self.root.hourly_frame.grid_columnconfigure((0,1,2), weight=1)
     
        self.root.air_pollution_frame.grid(row=4, column=0, pady=8, padx=16, columnspan=2, sticky=NSEW)
        self.root.air_pollution_frame.grid_rowconfigure((0,1,2,3,4,5,6), weight=1)
        self.root.air_pollution_frame.grid_columnconfigure((0,1,2), weight=1)    

        self.root.bottom_frame.grid(row=5, column=0, pady=8, padx=16, columnspan=2, sticky=NSEW)
        self.root.bottom_frame.grid_rowconfigure((0,1), weight=1)
        self.root.bottom_frame.grid_columnconfigure(0, weight=1)

    def create_elements(self):
        self.root.country_button = create_button(self.root.top_frame)
        self.root.city_button = create_button(self.root.top_frame)
        self.root.day_button = create_segmented_button(self.root.top_frame)
        self.root.unit_text = create_label(self.root.unit_frame, (primary_font, 20))
        self.root.metric_radio_button = create_radio_button(self.root.unit_frame, 1)
        self.root.imperial_radio_button = create_radio_button(self.root.unit_frame, 2)
        self.root.selection_button = create_segmented_button(self.root.selection_frame)
        self.root.temperature_label = create_label(self.root.temp_frame, (primary_font, 96))
        self.root.weather_details_label = create_label(self.root.temp_frame, (secondary_font, 24))
        self.root.wind_label = create_label(self.root.info_frame, (secondary_font, 16))
        self.root.ground_level = create_label(self.root.info_frame, (secondary_font, 16))
        self.root.humidity_label = create_label(self.root.info_frame, (secondary_font, 16))
        self.root.pressure_label = create_label(self.root.info_frame, (secondary_font, 16))
        self.root.temp_max_label = create_label(self.root.info_frame, (secondary_font, 16))
        self.root.temp_min_label = create_label(self.root.info_frame, (secondary_font, 16))
        self.root.map_canvas = create_canvas(self.root.map_frame, 512, 256)
        self.root.map_button = create_segmented_button(self.root.map_frame)
        self.root.hourly_button = create_segmented_button(self.root.hourly_frame)
        self.root.hourly_air_button = create_segmented_button(self.root.air_pollution_frame)
        self.root.feels_like_label = create_label(self.root.bottom_frame, (secondary_font, 16))
        self.root.city_label = create_label(self.root.bottom_frame, (primary_font, 20))

        self.root.hourly_temprature = create_label(self.root.hourly_frame, (secondary_font, 16))
        self.root.hourly_min_temprature = create_label(self.root.hourly_frame, (secondary_font, 16))
        self.root.hourly_max_temprature = create_label(self.root.hourly_frame, (secondary_font, 16))
        self.root.hourly_feels_like = create_label(self.root.hourly_frame, (secondary_font, 16))
        self.root.hourly_humidity = create_label(self.root.hourly_frame, (secondary_font, 16))
        self.root.hourly_pressure = create_label(self.root.hourly_frame, (secondary_font, 16))
        self.root.hourly_weather_details = create_label(self.root.hourly_frame, (secondary_font, 16))
        self.root.hourly_ground_level = create_label(self.root.hourly_frame, (secondary_font, 16))

        self.root.air_pollution_air_quality = create_label(self.root.air_pollution_frame, (secondary_font, 16))
        self.root.air_pollution_co = create_label(self.root.air_pollution_frame, (secondary_font, 16))
        self.root.air_pollution_no = create_label(self.root.air_pollution_frame, (secondary_font, 16))
        self.root.air_pollution_no2 = create_label(self.root.air_pollution_frame, (secondary_font, 16))
        self.root.air_pollution_o3 = create_label(self.root.air_pollution_frame, (secondary_font, 16))
        self.root.air_pollution_pm2_5 = create_label(self.root.air_pollution_frame, (secondary_font, 16))
        self.root.air_pollution_so2 = create_label(self.root.air_pollution_frame, (secondary_font, 16))
        self.root.air_pollution_pm10 = create_label(self.root.air_pollution_frame, (secondary_font, 16))
        self.root.air_pollution_nh3 = create_label(self.root.air_pollution_frame, (secondary_font, 16))
        
        self.root.map_canvas.create_image(224,132, tag='map')
        self.root.selection_button.configure(values=['Map', 'Hourly Forecast', 'Air Pollution'],font=(primary_font, 14))
        

    def grid_elements(self):
        self.root.unit_text.grid(row=1, column=1, pady=0, padx=0, sticky=NSEW)
        self.root.metric_radio_button.grid(row=2, column=1, pady=10, padx=10, sticky=NSEW)
        self.root.imperial_radio_button.grid(row=3, column=1, pady=10, padx=10, sticky=NSEW)

        self.root.country_button.grid(row=0, column=1,pady=10, padx=10, sticky=NSEW)
        self.root.city_button.grid(row=1, column=1, pady=10, padx=10, sticky=NSEW)
        self.root.day_button.grid(row=2, column=1, pady=16, padx=16, sticky=NSEW)

        self.root.temperature_label.grid(row=0, column=0, pady=0, padx=72, sticky=NSEW)
        self.root.weather_details_label.grid(row=1, column=0, pady=0, padx=64, sticky=NSEW)
        self.root.wind_label.grid(row=0, column=1, pady=4, padx=24, sticky=NSEW)
        self.root.ground_level.grid(row=0, column=0, pady=4, padx=24, sticky=NSEW)
        self.root.humidity_label.grid(row=1, column=1, pady=4, padx=24, sticky=NSEW)
        self.root.pressure_label.grid(row=1, column=0, pady=4, padx=24, sticky=NSEW)
        self.root.temp_max_label.grid(row=2, column=1, pady=4, padx=24, sticky=NSEW)
        self.root.temp_min_label.grid(row=2, column=0, pady=4, padx=24, sticky=NSEW)
        self.root.map_canvas.grid(row=1, column=1, pady=0, padx=32, sticky=NSEW)
        self.root.city_label.grid(row=1, column=0, pady=0, padx=32, sticky=NSEW)
        self.root.feels_like_label.grid(row=0, column=0, pady=0, padx=32, sticky=NSEW)
        self.root.selection_button.grid(row=1, column=1, pady=16, padx=16, sticky=NSEW)
        self.root.map_button.grid(row=0, column=1, pady=16, padx=16, sticky=NSEW)
        self.root.hourly_button.grid(row=0, column=0,columnspan=3, pady=16, padx=16, sticky=NSEW)
        self.root.hourly_air_button.grid(row=0, column=0,columnspan=3, pady=16, padx=16, sticky=NSEW)

        self.root.hourly_min_temprature.grid(row=1, column=0, pady=4, padx=24, sticky=NSEW)
        self.root.hourly_max_temprature.grid(row=1, column=1, pady=4, padx=24, sticky=NSEW)
        self.root.hourly_humidity.grid(row=2, column=0, pady=4, padx=24, sticky=NSEW)
        self.root.hourly_pressure.grid(row=2, column=1, pady=4, padx=24, sticky=NSEW)
        self.root.hourly_temprature.grid(row=3, column=0, pady=4, padx=24, sticky=NSEW)
        self.root.hourly_feels_like.grid(row=3, column=1, pady=4, padx=24, sticky=NSEW)
        self.root.hourly_weather_details.grid(row=4, column=0, pady=4, padx=24, sticky=NSEW)
        self.root.hourly_ground_level.grid(row=4, column=1, pady=4, padx=24, sticky=NSEW)

        self.root.air_pollution_air_quality.grid(row=1, column=0, pady=4, padx=16, sticky=NSEW)
        self.root.air_pollution_co.grid(row=1, column=1, pady=4, padx=16, sticky=NSEW)
        self.root.air_pollution_no.grid(row=1, column=2, pady=4, padx=16, sticky=NSEW)
        self.root.air_pollution_no2.grid(row=2, column=0, pady=4, padx=16, sticky=NSEW)
        self.root.air_pollution_o3.grid(row=2, column=1, pady=4, padx=16, sticky=NSEW)
        self.root.air_pollution_pm2_5.grid(row=2, column=2, pady=4, padx=16, sticky=NSEW)
        self.root.air_pollution_so2.grid(row=3, column=0, pady=4, padx=16, sticky=NSEW)
        self.root.air_pollution_pm10.grid(row=3, column=1, pady=4, padx=16, sticky=NSEW)
        self.root.air_pollution_nh3.grid(row=3, column=2, pady=4, padx=16, sticky=NSEW)
