
from inspect import stack
from matplotlib.pyplot import margins
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
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
import histograme
import matplotlib as plt
from GrayLevelSlicingA1 import A1
from GrayLevelSlicingA2 import A2
from medianFilter import median_filter

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
        [sg.Checkbox('Gray Scale Slicing 1', key = '-GRAY1-', pad = (0,10)),],
        [sg.Checkbox('Gray Scale Slicing 2', key = '-GRAY2-', pad = (0,10)),]
        ]),sg.Column([
            [sg.Input(key = '-min1-', size = (5,3),pad = (0,5)),sg.Text('min')],
            [sg.Input(key = '-max1-', size = (5,3)),sg.Text('max')],
            [sg.Input(key = '-min2-', size = (5,3),pad = (0,5)),sg.Text('min')],
            [sg.Input(key = '-max2-', size = (5,3)),sg.Text('max')],
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
        [sg.Checkbox('Average Filter', key = '-AVERAGEFILTER-', pad = (0,0) ), sg.Checkbox('Median Filter', key = '-MEDIANFILTER-', pad = (0,0) )],
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
    [left_col,mid_col,sg.Canvas(key='-CANVAS-')],
    [down_col],
    [filter_col]
    
]

# Display Window
window = sg.Window('Window Title', layout, margins=(0, 0), resizable=False, return_keyboard_events=True, finalize=True)
# window.maximize()

# update_image(original , window['-BYTES-'], window['-GRAY-'], window['-NEGATIVEIMAGE-'], window['-LOG-'], window['-INVERSELOG-'])
def update_image(original ,bytes , gray , negativeimage , log , negativelog,threshold,sthreshold,add,sadition,subtract,ssubtraction,averageFilter,gray1,gray2,min1,max1,min2,max2,medianFilter):
    

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
    if gray1 and min1 and max1 :
        A1(image,int(min1),int(max1))
    if gray2 and min2 and max2 :
        A2(image,int(min2),int(max2))
    if averageFilter :
        Avg_filter(image)
    if medianFilter :
        median_filter(image)
        
        
    
        
    res = Image.fromarray(image)
    bio = BytesIO()
    res.save(bio, format = 'PNG')
    if [gray,threshold] :
        window['-IMAGE-'].update(data = bio.getvalue())
    else :
        bio = BytesIO()
        original.save(bio, format = 'PNG')
        window['-IMAGE-'].update(data = bio.getvalue())

        
plt.use('TkAgg')
def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg
        
        


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
        # print(file)
        # if file :
        #     fig = histograme.draw_histo_RGP(file)
        #     draw_figure(window['-CANVAS-'].TKCanvas, fig)
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
                     values['-AVERAGEFILTER-'],
                     values['-GRAY1-'],
                     values['-GRAY2-'],
                     values['-min1-'],
                     values['-max1-'],
                     values['-min2-'],
                     values['-max2-'],
                     values['-MEDIANFILTER-']
                     
                    )

        
window.close()






