from numpy import size
import PySimpleGUI as sg
import os
import pathlib

# Colores
LIGHT_GRAY_BUTTON_COLOR = f'#212021 on #e0e0e0'
DARK_GRAY_BUTTON_COLOR = '#e0e0e0 on #212021'



def open_file():
    '''Open file and update the infobar'''
    filename = sg.popup_get_file('Open', no_window=True)
    if filename:
        file = pathlib.Path(filename)
        return file




sg.set_options(element_padding=(1, 2))

menu_def = [
    ['&File', ['&Open (Ctrl+O)', '&Save', '&Properties', 'E&xit' ]],
        ]




filter_bar = [
    [sg.B('median filter',size = (20,1),button_color =LIGHT_GRAY_BUTTON_COLOR),sg.B('avg filter',size = (20,1), button_color =LIGHT_GRAY_BUTTON_COLOR)]
]
one = [
    [sg.B('wow filter',size = (20,1)),sg.B('gogo filter',size = (20,1)),sg.B('MONMO filter',size = (20,1))]
]
left_bar = [
    [sg.B('GrayScale',size = (20,1), button_color=DARK_GRAY_BUTTON_COLOR )],
    [sg.B('difference',size = (20,1), button_color=DARK_GRAY_BUTTON_COLOR )],
    [sg.B('Contrast Stretching',size = (20,1), button_color=DARK_GRAY_BUTTON_COLOR )],
    [sg.B('filter',size = (20,1), button_color=DARK_GRAY_BUTTON_COLOR )]
    
]
mid_bar =[
    
    [sg.Text("import image:")],
    [sg.Text(size=(40, 1), key="-TOUT-")],
    [sg.Image(key="-IMAGE-")],
]




layout = [
    [sg.MenubarCustom(menu_def, tearoff=False)],
    [sg.Column(left_bar, key='-left-'),sg.Column(mid_bar,key='-mid-')],
    [sg.Column(filter_bar,key='-filter-'),sg.Column(one, visible=False, key='-GrayScale-')]
    ]


window = sg.Window('Window Title', layout ,margins = (0,0), resizable=True, return_keyboard_events=True, finalize=True)
window.maximize()

last='filter'
while True:
    event, values = window.read()
    print(event, values)
    if event in (None, 'Exit'):
        break
    
    if event in ['filter','GrayScale'] :
        window[f'-{last}-'].update(visible=False)
        last = event
        print(last)
        window[f'-{last}-'].update(visible=True)
    if event in ('Open (Ctrl+O)', 'o:79'):
        file = open_file()
        print(file)
        window["-IMAGE-"].update(filename=file)
window.close()