import PySimpleGUI as sg
#from logic2 import Taffy



class elements:

    def __init__(self):
        pass


    #text
    text_expression = sg.Text('Press Start to begin:', key='-text_expression-')
    text_correct_value = sg.Text('0', key='-text_correct_value-')
    text_incorrect_value = sg.Text('0', key='-text_incorrect_value-')
    text_correct_count = sg.Text('correct count', key='-text_correct_count-')
    text_incorrect_count = sg.Text('incorrect count', key='-text_incorrect_count-')
    text_result = sg.Text('result', key='-text_result-')
    text_min = sg.Text('Minimum Factor:', key='-text_min')
    text_max = sg.Text('Maximum Factor:', key='-text_max')

    #buttons
    button_true = sg.Button('True', key='-button_true-')
    button_false = sg.Button('False', key='-button_false-')
    button_start = sg.Button('Start Game', key='-button_start-')

    #spinners
    spinner_min = sg.Spin([i for i in range(2,20)], initial_value=2, key='-spinner_min-')
    spinner_max = sg.Spin([i for i in range(1, 30)], initial_value=10, key='-spinner_max-')

    #rows
    row1 = []
