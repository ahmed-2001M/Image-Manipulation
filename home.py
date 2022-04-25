
from inspect import stack
from matplotlib.pyplot import margins
import numpy as np
from numpy import asarray, average
from numpy import pad, size
import PySimpleGUI as sg
import os
import pathlib
from gray_sacle import gray_scale3d
from PIL import Image
from io import BytesIO 
from threshold import Threshold
from ArithmaticOperationAdd import Addition
from ArithmaticOperationSubtract import Subtraction
from average_filter import Avg_filter

# Colores
FIRST_COLOR = f'#E7E7E7 on #041B2D'
SECOND_COLOR = '#041B2D on #9B9B9B '
sg.set_options(element_padding=(0, 0))
file = None
original = None

# Menu bar
menu_def = [
    ['&File', ['&Open (Ctrl+O)', '&Save', '&Properties', 'E&xit']],
]

# Open function (Menu)
def open_file():
    filename = sg.popup_get_file('Open', no_window=True)
    if filename:
        file = pathlib.Path(filename)
        return file

# Buttons for manibulate image (every button has many buttons)
left_col = sg.Column([
    [sg.B('Contrast', size=(20, 1), button_color=SECOND_COLOR, pad = (3,3))],
    [sg.B('difference', size=(20, 1), button_color=SECOND_COLOR, pad = (3,3))],
    [sg.B('Contrast Stretching', size=(20, 1), button_color=SECOND_COLOR, pad = (3,3))],
    [sg.B('Filter', size=(20, 1), button_color=SECOND_COLOR, pad = (3,3))]

])

# Will Show Image and histo grame
mid_col = sg.Column([

    [sg.Text("import image:")],
    [sg.Image(key="-IMAGE-",size = (300,300), background_color='blue')]
    
],pad = (5,0))

# column for changable buttons
down_col = sg.Frame('actions',[
    [sg.Column([
        [sg.Checkbox('Gray Scale', key = '-GRAY-', pad = (0,0)),sg.Checkbox('threshold', key = '-THRESHOLD-', pad = (90,0)),],
        [sg.Slider(range = (1,8),orientation = 'h', enable_events=True, disable_number_display=True , key = '-BYTES-', pad = (0,0)),
         sg.Slider(range = (1,255),orientation = 'h', enable_events=True, disable_number_display=True , key = '-STHRESHOLD-', pad = (5,0)),],
        [sg.Checkbox('Add Constant', key = '-ADITION-', pad = (0,0)),  sg.Checkbox('Subtract Constant', key = '-SUBTRACTION-', pad = (75,0))],
        [sg.Slider(range = (1,255,20),orientation = 'h', enable_events=True, disable_number_display=True , key = '-SADITION-', pad = (0,0)),
         sg.Slider(range = (1,255),orientation = 'h', enable_events=True, disable_number_display=True , key = '-SSUBTRACTION-', pad = (5,0)),]
    ]),sg.Column([
        [sg.Checkbox('Negative Image', key = '-NEGATIVEIMAGE-', pad = (0,0)), sg.Checkbox('Contrast Stretching', key = '-CONTRAST-', pad = (0,0)), sg.Checkbox('Power Low', key = '-POWERLOW-', pad = (0,0)), ],
        [sg.Checkbox('Log Transform', key = '-LOG-', pad = (0,0)), sg.Checkbox('Inverse Log', key = '-INVERSELOG-' , pad = (0,0)), sg.Button('LOAD', key = '-LOAD-' , pad = (0,0))],

        
    ])],

], visible = False, key = '-Contrast-',pad = (20,0))
# down_col = sg.Frame('actions',[
#     [sg.Column([
#         [sg.Checkbox('Gray Scale', key = '-GRAY-', pad = (0,0)),sg.Checkbox('threshold', key = '-THRESHOLD-', pad = (90,0)),],
#         [sg.Slider(range = (1,8),orientation = 'h', enable_events=True, disable_number_display=True , key = '-BYTES-', pad = (0,0)),
#          sg.Slider(range = (1,255),orientation = 'h', enable_events=True, disable_number_display=True , key = '-STHRESHOLD-', pad = (5,0)),],
#         [sg.Checkbox('Add Constant', key = '-ADITION-', pad = (0,0)),sg.InputText(key='-SADITION-',size=(5,3)),  sg.Checkbox('Subtract Constant', key = '-SUBTRACTION-', pad = (5,0)),sg.InputText(key='-SSUBTRACTION-',size=(5,3))]
#     ]),sg.Column([
#         [sg.Checkbox('Negative Image', key = '-NEGATIVEIMAGE-', pad = (0,0)), sg.Checkbox('Contrast Stretching', key = '-CONTRAST-', pad = (0,0)), sg.Checkbox('Power Low', key = '-POWERLOW-', pad = (0,0)), ],
#         [sg.Checkbox('Log Transform', key = '-LOG-', pad = (0,0)), sg.Checkbox('Inverse Log', key = '-INVERSELOG-' , pad = (0,0)), sg.Button('Load', key = '-LOAD-' , pad = (0,0))],

        
#     ])],

# ], visible = False, key = '-Contrast-',pad = (20,0))

#filter column 
filter_col = sg.Frame('action',[
    [sg.Column([
        [sg.Checkbox('Average Filter', key = '-AVERAGEFILTER-', pad = (0,0) )],
        [sg.Button('LOAD', key = '-LOAD1-' , pad = (0,0))]
    ])]
], visible = False, key = '-Filter-',pad = (20,0))

#Make Histo Grame######################################
histo_col = sg.Column([
    [sg.Text("Histo Grame:")],
    [sg.Image(key='-HISTO-', size = (300,300), background_color='blue')]
])
#######################################################


# layout to put elements on window
layout = [
    [sg.MenubarCustom(menu_def)],
    [left_col,mid_col,histo_col],
    [down_col],
    [filter_col]
    
]

# Display Window
window = sg.Window('Window Title', layout, margins=(0, 0), resizable=False, return_keyboard_events=True, finalize=True)
# window.maximize()

# update_image(original , window['-BYTES-'], window['-GRAY-'], window['-NEGATIVEIMAGE-'], window['-LOG-'], window['-INVERSELOG-'])
def update_image(original ,bytes , gray , negativeimage , log , negativelog,threshold,sthreshold,add,sadition,subtract,ssubtraction,averageFilter):
    

    global image
    image = asarray(original)

    if gray :
        gray_scale3d(image,bytes)
    if threshold:
        Threshold(image,int(sthreshold))
    if add:
        Addition(image,int(sadition))
    if subtract and ssubtraction !='':
        Subtraction(image,ssubtraction)
    if averageFilter :
        Avg_filter(image)
    
        
    res = Image.fromarray(image)
    bio = BytesIO()
    res.save(bio, format = 'PNG')
    if [gray,threshold] :
        window['-IMAGE-'].update(data = bio.getvalue())
    else :
        bio = BytesIO()
        original.save(bio, format = 'PNG')
        window['-IMAGE-'].update(data = bio.getvalue())


active = 'Filter'  # To Save Active Button

# running loop
while True:
    event, values = window.read()
    print(event)
    # print(event, values)
    if event in (None, 'Exit'):
        break
    
    if event in ('Open (Ctrl+O)', 'o:79'):
        file = open_file()
        original = Image.open(file)
        original.thumbnail((400,400))
        bio = BytesIO()
        original.save(bio, format = 'PNG')
        window["-IMAGE-"].update(data = bio.getvalue())
    if event == 'Contrast' :
        window[f'-{active}-'].update(visible=False) 
        active = 'Contrast'
        window[f'-{active}-'].update(visible=True)  
    
    if event == 'Filter' :
        window[f'-{active}-'].update(visible=False)  
        active = 'Filter'
        window[f'-{active}-'].update(visible=True)  
    
    if (event in['-LOAD-','-LOAD1-'] and file):
        # print(original)
        update_image(original,
                     values['-BYTES-'],
                     values['-GRAY-'], 
                     values['-NEGATIVEIMAGE-'], 
                     values['-LOG-'], 
                     values['-INVERSELOG-'],
                     values['-THRESHOLD-'],
                     values['-STHRESHOLD-'],
                     values['-ADITION-'],
                     values['-SADITION-'],
                     values['-SUBTRACTION-'],
                     values['-SSUBTRACTION-'],
                     values['-AVERAGEFILTER-']
                    )

        
window.close()
