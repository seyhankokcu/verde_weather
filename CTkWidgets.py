from customtkinter import CTkButton, CTkSegmentedButton, CTkLabel, CTkCanvas, CTkRadioButton, FontManager

primary_font = FontManager.load_font("./main_files/files/Champagne & Limousines Bold.ttf")
secondary_font = FontManager.load_font("./main_files/files/Champagne & Limousines.ttf")

primary_color = '#444444'
secondary_color = '#323232'

def create_button(master):
    return CTkButton(
        master=master, 
        width=256,
        height=16,
        corner_radius=64,
        border_width=0,
        font=(primary_font,16),
        fg_color=primary_color,
        hover_color=secondary_color,
        text=' '
        )

def create_segmented_button(master):
    return CTkSegmentedButton(
        master=master, 
        width=256,
        height=16,
        values=[' '],
        corner_radius=64,
        border_width=0,
        font=(primary_font,12),
        selected_color=secondary_color,
        selected_hover_color=secondary_color,
        )
        
def create_label(master, font):
    return CTkLabel(
        master=master,
        font=font,
        text=' ',
        )

def create_image(master, image):
    return CTkLabel(
        master=master,
        image=image,
        )

def create_canvas(master, width, height):
    return CTkCanvas(
        master=master,
        width=width,
        height=height,
        )

def create_radio_button(master, value):
    return CTkRadioButton(
        master=master,
        value=value,
        text=' ',
        font=(primary_font, 12),
        )