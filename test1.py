from matplotlib.pyplot import margins
from numpy import pad, size
import PySimpleGUI as sg
import os
import pathlib
import gray_sacle



layout =[[sg.Image(r"C:\Users\Ahmed\Downloads\sd login diagrame.png", key="-IMAGE-")],[sg.B('press', key='boo')]]

window = sg.Window('Window Title', layout, margins=(0, 0), resizable=True, return_keyboard_events=True, finalize=True)
window.maximize()

while True:
    event, values = window.read()
    print(event, values)
    if event in (None, 'Exit'):
        break
    
    if event == 'boo' :
        res = gray_sacle.gray_scale2d("C:\\Users\\Ahmed\\Downloads\\sd login diagrame.png",8)
        window['-IMAGE-'].update(data = res)
    
window.close()

