import PySimpleGUI as sg
from Taffy_GUI_Elements import elements as e
from logic2 import Taffy

taf = Taffy()
#taf.workhorse()

def setup():
    # there should be a countdown here
    taf.min = int(window['-spinner_min-'].get())
    print("Minimum:", taf.min)
    taf.max = int(window['-spinner_max-'].get())
    print("Maximum:", taf.max)
    taf.correct_answer()
    taf.incorrect_answer()
    taf.math()
    window['-text_expression-'].update(str(taf.expression))



def check_true():
    print("Mult 1:", taf.r1)
    print("Mult 2:", taf.r2)
    print("Correct Answer:", taf.correct_value)
    print("Given value:", taf.gValue)
    if taf.correct_value == taf.gValue:
        taf.correct_count += 1
    else:
        taf.incorrect_count += 1
    print(taf.correct_count)
    window['-text_correct_value-'].update(str(taf.correct_count))
    window['-text_incorrect_value-'].update(str(taf.incorrect_count))
    setup()

def check_false():
    print("Mult 1:", taf.r1)
    print("Mult 2:", taf.r2)
    print("Correct Answer:", taf.correct_value)
    print("Given value:", taf.gValue)
    if taf.correct_value == taf.gValue:
        taf.incorrect_count += 1
    else:
        taf.correct_count += 1
    print(taf.incorrect_count)
    window['-text_incorrect_value-'].update(str(taf.incorrect_count))
    window['-text_correct_value-'].update(str(taf.correct_count))
    setup()


layout = [
    [e.text_min, e.spinner_min],
    [e.text_max, e.spinner_max],
    [e.button_start],
    [e.text_expression],
    [e.button_true, e.button_false],
    [e.text_correct_count, e.text_correct_value],
    [e.text_incorrect_count, e.text_incorrect_value],
    [sg.Exit()],
]

window = sg.Window("T&Ffy Math", layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break
    if event == '-button_start-':
        setup()
        taf.correct_count = 0
        window['-text_correct_value-'].update(str(taf.correct_count))
        taf.incorrect_count = 0
        window['-text_incorrect_value-'].update(str(taf.incorrect_count))
    if event == '-button_true-':
        check_true()
    if event == '-button_false-':
        check_false()
window.close()
