
from matplotlib.pyplot import margins
import numpy as np
from numpy import asarray
from numpy import pad, size
import PySimpleGUI as sg
import os
import pathlib
from gray_sacle import gray_scale2d
from PIL import Image
from io import BytesIO 

# Colores
FIRST_COLOR = f'#E7E7E7 on #041B2D'
SECOND_COLOR = '#041B2D on #9B9B9B '
sg.set_options(element_padding=(2, 10))
file = None
original = None

# Menu bar
menu_def = [
    ['&File', ['&Open (Ctrl+O)', '&Save', '&Properties', 'E&xit']],
]

# Open function (Menu)
def open_file():
    '''Open file and update the infobar'''
    filename = sg.popup_get_file('Open', no_window=True)
    if filename:
        file = pathlib.Path(filename)
        return file

# Buttons for manibulate image (every button has many buttons)
left_col = sg.Column([
    [sg.B('Contrast', size=(20, 1), button_color=SECOND_COLOR)],
    [sg.B('difference', size=(20, 1), button_color=SECOND_COLOR)],
    [sg.B('Contrast Stretching', size=(20, 1), button_color=SECOND_COLOR)],
    [sg.B('filter', size=(20, 1), button_color=SECOND_COLOR)]

])

# Will Show Image and histo grame
mid_col = sg.Column([

    [sg.Text("import image:")],
    [sg.Image(key="-IMAGE-",size = (300,300), background_color='yellow')]
    
])

# column for changable buttons
right_col = sg.Column([
    [sg.Frame('bits',layout = [[sg.Slider(range = (1,8),orientation = 'h', enable_events=True, disable_number_display=True , key = '-BYTES-')]])],
    [sg.Checkbox('Gray_Scale', key = '-GRAY-'), sg.Checkbox('Negative_Image', key = '-NEGATIVEIMAGE-')],
    [sg.Checkbox('Log', key = '-LOG-'), sg.Checkbox('Negative_Log', key = '-NEGATIVELOG-')]
], visible = False, key = '-Contrast-')


#Make Histo Grame######################################

#######################################################


# layout to put elements on window
layout = [
    [sg.MenubarCustom(menu_def)],
    [left_col,mid_col,right_col],
    
]

# Display Window
window = sg.Window('Window Title', layout, margins=(0, 0), resizable=False, return_keyboard_events=True, finalize=True)
window.maximize()

# update_image(original , window['-BYTES-'], window['-GRAY-'], window['-NEGATIVEIMAGE-'], window['-LOG-'], window['-NEGATIVELOG-'])
def update_image(original ,bytes , gray , negativeimage , log , negativelog):


    global image
    image = original

    if gray :
        image = gray_scale2d(original,bytes)

    bio = BytesIO()
    image.save(bio, format = 'PNG')

    window['-IMAGE-'].update(data = bio.getvalue())


active = 'filter'  # To Save Active Button

# running loop
while True:
    event, values = window.read(timeout = 1000)
    print(event, values)
    if event in (None, 'Exit'):
        break
    
    if event in ('Open (Ctrl+O)', 'o:79'):
        file = open_file()
        original = Image.open(file)
        window["-IMAGE-"].update(filename=file)
    if event == 'Contrast' :
        active = 'Contrast'
        window[f'-{active}-'].update(visible=True)  
    
    if (active == 'Contrast' and file):
        print(original)
        update_image(original,
                     values['-BYTES-'],
                     values['-GRAY-'], 
                     values['-NEGATIVEIMAGE-'], 
                     values['-LOG-'], 
                     values['-NEGATIVELOG-']
                     )
        print('ahmed')
        
window.close()
