from numpy import size
import PySimpleGUI as sg
import os
import pathlib

# Colores
FIRST_COLOR = f'#E7E7E7 on #041B2D'
SECOND_COLOR = '#041B2D on #9B9B9B '
sg.set_options(element_padding=(1, 2))

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
    [sg.B('GrayScale', size=(20, 1), button_color=SECOND_COLOR)],
    [sg.B('difference', size=(20, 1), button_color=SECOND_COLOR)],
    [sg.B('Contrast Stretching', size=(20, 1), button_color=SECOND_COLOR)],
    [sg.B('filter', size=(20, 1), button_color=SECOND_COLOR)]

]

# filter_buttons
filter_buttons = [
    [sg.B('median filter', size=(20, 1), button_color=FIRST_COLOR), sg.B('avg filter', size=(20, 1), button_color=FIRST_COLOR)]
]

# Will Change######################################
one = [
    [sg.B('wow filter', size=(20, 1)), sg.B('gogo filter', size=(20, 1)), sg.B('MONMO filter', size=(20, 1))]
]

# Will Show Image and histo grame
mid_col = [

    [sg.Text("import image:")],
    [sg.Text(size=(40, 1), key="-TOUT-")],
    [sg.Image(key="-IMAGE-")],
]

#Make Histo Grame######################################

#######################################################


# layout to put elements on window
layout = [
    [sg.MenubarCustom(menu_def, tearoff=False)],
    [sg.Column(left_col, key='-left-'), sg.Column(mid_col, key='-mid-')],
    [sg.Column(filter_buttons, key='-filter-'), sg.Column(one, visible=False, key='-GrayScale-')]
]

# Display Window
window = sg.Window('Window Title', layout, margins=(
    0, 0), resizable=True, return_keyboard_events=True, finalize=True)
window.maximize()


active = 'filter'  # To Save Active Button

# running loop
while True:
    event, values = window.read()
    print(event, values)
    if event in (None, 'Exit'):
        break

    if event in ['filter', 'GrayScale']:
        window[f'-{active}-'].update(visible=False)
        active = event
        print(active)
        window[f'-{active}-'].update(visible=True)
    if event in ('Open (Ctrl+O)', 'o:79'):
        file = open_file()
        print(file)
        window["-IMAGE-"].update(filename=file)
window.close()
