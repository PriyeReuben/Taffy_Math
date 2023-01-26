import PySimpleGUI as sg
from logic import Taffy as t

class elements:

    def __init__(self):
        pass
    #text
    text_expression = sg.Text('expression', key='-text_expression-')
    text_correct_count = sg.Text('correct count', key='-text_correct_count-')
    text_incorrect_count = sg.Text('incorrect count', key='-text_incorrect_count-')
    text_result = sg.Text('result', key='-text_result-')
    text_min = sg.Text('Minimum Value:', key='-text_min')
    text_max = sg.Text('Maximum Value:', key='-text_max')

    #buttons
    button_true = sg.Button('True', key='-button_true-')
    button_false = sg.Button('False', key='-button_false-')

    #spinners
    spinner_min = sg.Spin([i for i in range(2,16)], initial_value=2, key='-spinner_min-')
    spinner_max = sg.Spin([i for i in range(1, 16)], initial_value=3, key='-spinner_max-')

    #rows
    row1 = []
