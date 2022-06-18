from inspect import stack
from matplotlib.pyplot import margins
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from numpy import asarray, average, int8
from numpy import pad, size
import PySimpleGUI as sg
import os
import pathlib
from __and import _and0
from __and import _and1
from __or import _or0
from __or import _or1
from contrststrecting import contrast_stretching
from firstDrivative import st1
from gray_sacle import gray_scale3d
from PIL import Image
from io import BytesIO
from gussianfilter import gussian_filter
from highpass_filter import high_gussian_filter
from inverselog import inv_logtransform
from max import max_filter
from min import min_filter
from negative import negative
from powerlow import power_low 
from threshold import Threshold
from ArithmaticOperationAdd import Addition
from ArithmaticOperationSubtract import Subtraction
from average_filter import Avg_filter
import histograme
import matplotlib as plt
from GrayLevelSlicingA1 import A1
from GrayLevelSlicingA2 import A2
from medianFilter import median_filter
from LogTransform import logtransform
from histoGrameEqualization import hiso_grame_equalization
from second_drevative import second_div
from firstDrivative import st1

sg.theme('DarkTanBlue')
# Colores
FIRST_COLOR = f'#E7E7E7 on #041B2D'
SECOND_COLOR = '#041B2D on #9B9B9B '
sg.set_options(element_padding=(0, 0))
file = None
original = None
image = None
actions = list()

# Menu bar
menu_def = [
    ['&File', ['&Open (Ctrl+O)', '&Save', 'Exit']],
]

# Open function (Menu)
def open_file():
    filename = sg.popup_get_file('Open', no_window=True)
    if filename:
        file = pathlib.Path(filename)
        return file

# Buttons for manibulate image (every button has many buttons)
left_col = sg.Column([
    [sg.B('Spatial Inhancement', size=(20, 2), button_color=SECOND_COLOR, pad = (3,10))],
    [sg.B('Filters', size=(20, 2), button_color=SECOND_COLOR, pad = (3,10))]

])

# Will Show Image and histo grame
mid_col = sg.Column([

    [sg.Text("import image:")],
    [sg.Image(key="-IMAGE-",size = (300,300), background_color='white')]
    
],pad = (5,0))

# column for changable buttons
down_col = sg.Frame('actions',[
    [sg.Column([
        [sg.B('Gray Scale', size=(10, 1), button_color=SECOND_COLOR, pad = (0,0)) , sg.B('threshold', size=(10, 1), button_color=SECOND_COLOR, pad = (100,0))],
        # [sg.Checkbox('Gray Scale', key = '-GRAY-', pad = (0,0)),sg.Checkbox('threshold', key = '-THRESHOLD-', pad = (90,0)),],
        [sg.Slider(range = (1,8),orientation = 'h', enable_events=True, disable_number_display=True , key = '-BYTES-', pad = (0,5)),
         sg.Slider(range = (1,255),orientation = 'h', enable_events=True, disable_number_display=True , key = '-STHRESHOLD-', pad = (5,5)),],
        [sg.B('Add Constant', size=(10, 1), button_color=SECOND_COLOR, pad = (0,0)),  sg.B('Subtract Constant', size=(15, 1), button_color=SECOND_COLOR, pad = (100,0))],
        [sg.Slider(range = (1,255,20),orientation = 'h', enable_events=True, disable_number_display=True , key = '-SADITION-', pad = (0,5)),
         sg.Slider(range = (1,255),orientation = 'h', enable_events=True, disable_number_display=True , key = '-SSUBTRACTION-', pad = (5,5)),]
    ]),sg.Column([
        [sg.B('Gray Scale Slicing 1', size=(12, 2), button_color=SECOND_COLOR , pad = (15,8)),],
        [sg.B('Gray Scale Slicing 2', size=(12, 2), button_color=SECOND_COLOR, pad = (15,8)),]
        ]),sg.Column([
            [sg.Input(key = '-min1-', size = (5,3),pad = (0,5)),sg.Text('min')],
            [sg.Input(key = '-max1-', size = (5,3)),sg.Text('max')],
            [sg.Input(key = '-min2-', size = (5,3),pad = (0,5)),sg.Text('min')],
            [sg.Input(key = '-max2-', size = (5,3)),sg.Text('max')],
            ]),sg.Column([
        [sg.B('Negative Image', size=(12, 1), button_color=SECOND_COLOR , pad = (5,2)),   ],
        [sg.B('Log Transform', size=(12, 1), button_color=SECOND_COLOR , pad = (5,2)) ],
        [sg.B('Power Low', size=(12, 1), button_color=SECOND_COLOR , pad = (5,2))],
        [sg.Slider(range = (1,5),orientation = 'h',size = (12,15), enable_events=True, disable_number_display=True , key = '-power-', pad = (0,3))],
        
        ]),sg.Column([
            [sg.B('Inverse Log', size=(12, 1), button_color=SECOND_COLOR , pad = (5,3))],
            [sg.B('Contrast Stretching', size=(12, 2), button_color=SECOND_COLOR , pad = (5,3)) ],
            [sg.B('Histo Equalization', size=(12, 1), button_color=SECOND_COLOR , pad = (5,3))]
        ]),sg.Column([
            [sg.B('AND 0', size=(12, 1), button_color=SECOND_COLOR , pad = (5,3))],
            [sg.B('AND 1', size=(12, 1), button_color=SECOND_COLOR , pad = (5,3))],
            [sg.B('OR 0', size=(12, 1), button_color=SECOND_COLOR , pad = (5,3)) ],
            [sg.B('OR 1', size=(12, 1), button_color=SECOND_COLOR , pad = (5,3)) ],
        ]),sg.Column([
            [sg.Button('Undo', key = '-LOAD-' , pad = (3,0),mouseover_colors = ('white', 'blue'),button_color = ('black','white'))]
        ])
            ],

], visible = False, key = '-Spatial Inhancement-',pad = (20,0))


filter_col = sg.Frame('action',[
    [sg.Column([
        [sg.B('Average Filter', size=(10, 1), button_color=SECOND_COLOR , pad = (0,0) ), sg.B('Median Filter', size=(10, 1), button_color=SECOND_COLOR, pad = (100,0) ) ],
        [sg.Slider(range = (1,10),orientation = 'h', enable_events=True, disable_number_display=True , key = '-SAVERAGEFILTER-', pad = (0,5)),sg.Slider(range = (1,10),orientation = 'h', enable_events=True, disable_number_display=True , key = '-SMEDIANFILTER-', pad = (10,0))],
        [sg.B('First Drivative', size=(10, 1), button_color=SECOND_COLOR , pad = (10,0) ), sg.B('Second Drivative', size=(10, 1), button_color=SECOND_COLOR, pad = (0,0) ) ,sg.B('Gussian Filter', size=(10, 1), button_color=SECOND_COLOR , pad = (10,5) ) , sg.B('High Gussian Filter', size=(10, 1), button_color=SECOND_COLOR , pad = (10,5) )],
        [sg.B('Min Filter', size=(10, 1), button_color=SECOND_COLOR , pad = (10,0) ), sg.B('Max Filter', size=(10, 1), button_color=SECOND_COLOR , pad = (10,5) )],
        [sg.Button('Undo', key = '-LOAD1-' , pad = (200,0),mouseover_colors = ('white', 'blue'),button_color = ('black','white'))]
    ])]
], visible = False, key = '-Filters-',pad = (20,0))





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
    [filter_col,down_col],
    
]

# Display Window
window = sg.Window('Image Inhancement', layout , margins=(0, 0), resizable=False, return_keyboard_events=True)

# update_image(original , window['-BYTES-'], window['-GRAY-'], window['-NEGATIVEIMAGE-'], window['-LOG-'], window['-INVERSELOG-'])
def update_image(original ,bytes , gray , negativeimage , log ,
                threshold,sthreshold,add,sadition,
                subtract,ssubtraction,averageFilter,saverageFilter,
                gray1,gray2,min1,max1,min2,max2,medianFilter,smedianFilter,
                histoE,powerlow,contrast,firstdrivative,gussianfilter):
    



    if gray :
        gray_scale3d(image,bytes)
    if threshold:
        Threshold(image,int(sthreshold))
    
    if subtract and ssubtraction !='':
        Subtraction(image,ssubtraction)
    if gray1 and min1 and max1 :
        A1(image,int(min1),int(max1))
    if gray2 and min2 and max2 :
        A2(image,int(min2),int(max2))
    if averageFilter :
        Avg_filter(image,int(saverageFilter))
    if medianFilter :
        median_filter(image,int(smedianFilter))
    if log :
        image = logtransform(image)
    if histoE :
        image = hiso_grame_equalization(image)
    if negativeimage :
        negative(image)
    if powerlow :
        image = power_low(image)
        print(type(image))
    if contrast :
        contrast_stretching(image)
    if firstdrivative :
        st1(image)
    if add:
        Addition(image,int(sadition))
    
    # if gussianfilter :
    #     image = high_gussian_filter(image)
    
        
    res = Image.fromarray(image)
    
    if gussianfilter :
        res = high_gussian_filter(res)
    
    res = Image.fromarray(image)
    bio = BytesIO()
    res.save(bio, format = 'PNG')
    if [gray,threshold] :
        window['-IMAGE-'].update(data = bio.getvalue())
    else :
        bio = BytesIO()
        original.save(bio, format = 'PNG')
        window['-IMAGE-'].update(data = bio.getvalue())
        
        
def draw(image) :
    res = Image.fromarray(image)
    bio = BytesIO()
    res.save(bio, format = 'PNG')
    
    window['-IMAGE-'].update(data = bio.getvalue())



plt.use('TkAgg')
def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg
        
        


active = 'Filters'

# running loop
while True:
    event, values = window.read()
    # print(event, values)
    if event in (None, 'Exit'):
        break
    
    if event =='Save':
        im = Image.fromarray(image)
        im.save('vv.png')
    
    if event in ('Open (Ctrl+O)', 'o:79'):
        file = open_file()
        original = Image.open(file)
        
        original.thumbnail((400,400))
        image = asarray(original)
        
        actions.append(image)
        bio = BytesIO()
        original.save(bio, format = 'PNG')
        window["-IMAGE-"].update(data = bio.getvalue())
        
        if file :
            po = str(file)
            po = po.replace('\\','/')
            fig = histograme.draw_histo_RGP(po)
            draw_figure(window['-CANVAS-'].TKCanvas, fig)

    if event == 'Spatial Inhancement' :
        window[f'-{active}-'].update(visible=False) 
        active = 'Spatial Inhancement'
        window[f'-{active}-'].update(visible=True)  
    
    if event == 'Filters' :
        window[f'-{active}-'].update(visible=False)  
        active = 'Filters'
        window[f'-{active}-'].update(visible=True) 
        
#actions----------------------------------------------
    if event == 'Gray Scale' and values['-BYTES-'] :
        image = gray_scale3d(image,values['-BYTES-'])
        draw(image)
        actions.append(image)
        
    
    if event == 'threshold' and values['-STHRESHOLD-'] :
        image = Threshold(image,int(values['-STHRESHOLD-']))
        draw(image)
        actions.append(image)
    
    if event == 'Add Constant':
        image = Addition(image,int(values['-SADITION-']))
        draw(image)
        actions.append(image)
    
    if event == 'Subtract Constant':
        image = Subtraction(image,values['-SSUBTRACTION-'])
        draw(image)
        actions.append(image)
    
    if event == 'Gray Scale Slicing 1' and values['-min1-'] and values['-max1-'] :
        image = A1(image , int(values['-min1-']) , int(values['-max1-']))
        draw(image)
        actions.append(image)
        
    if event == 'Gray Scale Slicing 2' and values['-min2-'] and values['-max2-'] :
        image = A2(image , int(values['-min2-']) , int(values['-max2-']))
        draw(image)
        actions.append(image)
        
    if event == 'Negative Image' :
        image = negative(image)
        draw(image)
        actions.append(image)
        
    if event == 'Log Transform' :
        image = logtransform(image)
        draw(image)
        actions.append(image)
        
    if event == 'Contrast Stretching' :
        image = contrast_stretching(image)
        draw(image)
        actions.append(image)
    
    if event == 'Power Low' :
        image = power_low(image,values['-power-'])
        draw(image)
        actions.append(image)
    
    if event == 'Histo Equalization' :
        image = hiso_grame_equalization(image)
        draw(image)
        actions.append(image)
    
    if event == 'Average Filter' :
        image = Avg_filter(image,int(values['-SAVERAGEFILTER-']))
        draw(image)
        actions.append(image)
    
    if event == 'Median Filter' :
        image = median_filter(image,int(values['-SMEDIANFILTER-']))
        draw(image)
        actions.append(image)
    
    if event == 'First Drivative' :
        image = st1(image)
        draw(image)
        actions.append(image)
    
    if event == 'Second Drivative' :
        image = second_div(image)
        draw(image)
        actions.append(image)
    
    if event == 'Gussian Filter' :
        how = Image.fromarray(image)
        image = gussian_filter(how)
        draw(image)
        actions.append(image)
    
    if event == 'High Gussian Filter' :
        how = Image.fromarray(image)
        image = high_gussian_filter(how)
        draw(image)
        actions.append(image)
    
    if event == 'Inverse Log' :
        image = inv_logtransform(image)
        draw(image)
        actions.append(image)
        
    if event == 'AND 0' :
        image = _and0(image)
        draw(image)
        actions.append(image)
        
    if event == 'AND 1' :
        image = _and1(image)
        draw(image)
        actions.append(image)
    
    if event == 'OR 0' :
        image = _or0(image)
        draw(image)
        actions.append(image)
        
    if event == 'OR 1' :
        image = _or1(image)
        draw(image)
        actions.append(image)
        
    if event == 'Max Filter' :
        image = max_filter(image)
        draw(image)
        actions.append(image)
    
    if event == 'Min Filter':
        image = min_filter(image)
        draw(image)
        actions.append(image)
    
#end--------------------------------------------------
    if (event in['-LOAD-','-LOAD1-']):
        if len(actions) > 1 :
            actions.pop()
            image = actions[-1]
            draw(image)
        

window.close()






