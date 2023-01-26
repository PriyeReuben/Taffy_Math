import PySimpleGUI as sg
from Taffy_GUI_Elements import elements as e
from logic2 import Taffy

t = Taffy()

layout = [
    [e.text_min, e.spinner_min],
    [e.text_max, e.spinner_max],
    [e.text_expression],
    [e.button_true, e.button_false],
    [e.text_correct_count, e.text_incorrect_count],
    [sg.Exit()],
]

window = sg.Window("T&Ffy Math", layout)

while True:
    event, values = window.read()
    window['-text_expression-'].update(str(t.expression))
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break
window.close()
