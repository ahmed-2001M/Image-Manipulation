
from matplotlib.pyplot import margins
from numpy import pad, size
import PySimpleGUI as sg
import os
import pathlib
import gray_sacle

# Colores
FIRST_COLOR = f'#E7E7E7 on #041B2D'
SECOND_COLOR = '#041B2D on #9B9B9B '
sg.set_options(element_padding=(2, 10))
file = None

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
left_col = [
    [sg.B('Contrast', size=(20, 1), button_color=SECOND_COLOR)],
    [sg.B('difference', size=(20, 1), button_color=SECOND_COLOR)],
    [sg.B('Contrast Stretching', size=(20, 1), button_color=SECOND_COLOR)],
    [sg.B('filter', size=(20, 1), button_color=SECOND_COLOR)]

]

# filter_buttons
filter_buttons = [
    [sg.B('gilter', size=(20, 1), button_color=FIRST_COLOR), sg.B('avg filter', size=(20, 1), button_color=FIRST_COLOR)]
]

# Will Change######################################
contrast_buttons = [
    [sg.B('gray_scale', size=(20, 1)), sg.B('gogo filter', size=(20, 1)), sg.B('MONMO filter', size=(20, 1))]
]

# Will Show Image and histo grame
mid_col = [

    [sg.Text("import image:")],
    [sg.Image(key="-IMAGE-")]
    
]

slider_row =[
    [sg.Frame('bits',layout = [[sg.Slider(range = (1,8),orientation = 'h', enable_events=True, disable_number_display=True)]])]
]

#Make Histo Grame######################################

#######################################################


# layout to put elements on window
layout = [
    # , tearoff=False
    [sg.MenubarCustom(menu_def)],
    [sg.Column(left_col, key='-left-'), sg.Column(mid_col, key='-mid-')],
    [sg.Column(slider_row, visible=False, key='-gray_slider_col-', pad=(175,0))],
    [sg.Column(filter_buttons, key='-filter-'), sg.Column(contrast_buttons, visible=False, key='-GrayScale-')]
]

# Display Window
window = sg.Window('Window Title', layout, margins=(0, 0), resizable=True, return_keyboard_events=True, finalize=True)
window.maximize()


active = 'filter'  # To Save Active Button

# running loop
while True:
    event, values = window.read()
    print(event, values)
    if event in (None, 'Exit'):
        break
    
    #left_col events
    if event =='Contrast' and active != 'Contrast':
        window[f'-GrayScale-'].update(visible=True)
        window[f'-gray_slider_col-'].update(visible=True)
        active ='Contrast'
    else :
        window[f'-GrayScale-'].update(visible=False)
        window[f'-gray_slider_col-'].update(visible=False)
        
        
    if event =='filter' and active != 'filter':
        window[f'-filter-'].update(visible=True) 
        active = 'filter'  
    else :
        window[f'-filter-'].update(visible=False) 
        
###################end of events #######################
        
    if event in ('Open (Ctrl+O)', 'o:79'):
        file = open_file()
        # print(file)
        window["-IMAGE-"].update(filename=file)
        
        
    if event == 'gray_scale' :
        res = gray_sacle.gray_scale2d(f'{file}',8)
        byte=res.tobytes()
        window['-IMAGE-'].update(byte)
window.close()
