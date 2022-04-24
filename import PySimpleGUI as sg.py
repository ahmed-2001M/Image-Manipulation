import PySimpleGUI as sg
from PySimpleGUI import InputCombo, Combo, Multiline, ML, MLine, Checkbox, CB, Check, Button, B, Btn, \
    ButtonMenu, Canvas, Column, Col, Combo, Frame, Graph, Image, InputText, Input, In, Listbox, LBox,  \
    Menu, Multiline, ML, MLine, OptionMenu, Output, Pane, ProgressBar,  Radio, Slider, Spin, StatusBar, \
    Tab, TabGroup, Table, Text, Txt, T, Tree, TreeData,  VerticalSeparator, Window, Sizer

sg.change_look_and_feel('GreenTan')

col2 = Column([[Frame('Accounts:', [[Column([[Listbox(values=('test1','test2', 'test3'), size=(15, 20)), ]],
        size=(150, 400))]])]], pad=(0, 0))

col1 = Column([
    # Categories frame
    [Frame('Categories:', [[Radio('Websites', 'radio1', default=True, size=(10, 1)),
                       Radio('Software', 'radio1', size=(10, 1))]],)],
    # Information frame
    [Frame(layout=[[Column([[Text('Account:', pad=(0, 0))],
                      [Input(size=(19, 1), pad=(0, 0))],
                      [Text('User Id:', pad=(0, 0))],
                      [Input(size=(19, 1), pad=(0, 0)), Button('Copy', key='-USERID-', size=(4, 0))],
                      [Text('Password:', pad=(0, 0))],
                      [Input(size=(19, 1), pad=(0, 0)), Button('Copy', key='-PASS-', pad=None)],
                      [Text('Location:', pad=(0, 0))],
                      [Input(size=(19, 1), pad=(0, 0)), Button('Copy', key='-LOC')],
                      [Text('Notes:', pad=(0, 0))],
                      [Multiline(size=(17, 5))],
                      ], size=(235, 350), pad=(0,0))]], title='Information:')], ], pad=(0,0))

layout = [ [col1, col2],
    # Actions Frame
    [Frame('Actions:', [[Column([[Button('Save'), Button('Clear'), Button('Delete'),
        ]], size=(480,45), pad=(0,0))]])]]

# Position at top left side corner on right hand monitor
window = Window('Passwords', layout)

while True:
    event, values = window.read()
    print(event, values)
    if event is None:
        break
window.close()

