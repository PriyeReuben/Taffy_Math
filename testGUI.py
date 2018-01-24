import logic as taffy
import tkinter as tk
from tkinter import ttk
import GUI.ComboBoxes as cb

import time

window = tk.Tk()

correct_answers = 0
incorrect_answers = 0



window.title("T&F-fy Math")
def setup():

    taf = taffy.Taffy().math()
    taffy.Taffy.min =100

    '''
    min_value = tk.StringVar()
    min_value_chosen = ttk.Combobox(window, width=8, textvariable=min_value, state="readonly")
    min_value_chosen['values'] = (1, 5, 10, 15, 20, 25)
    min_value_chosen.grid(column=3, row=0)
    min_value_chosen.current(0)  # this assignes the first value in the tuple to be displaed in the combobox
    '''

    expression_label = ttk.Label(window, text=taf[0])
    expression_label.grid(column=1, row=1)

    results_label= ttk.Label(window, text = "Results")
    results_label.grid(column=1, row =2)


    #correct_answers_label = ttk.Label(window, text=correct_answers)
    #correct_answers_label.grid(column =1, row =4)

    #incorrect_answers_label = ttk.Label(window, text=incorrect_answers)
    #incorrect_answers_label.grid(column=4, row=4)

    def true_button_pressed():
        #expression_label.configure(text="")
        if (taf[3]==taf[1]):
            print("Correct")
            expression_label.configure(foreground="blue", text ="correct!")
            #expression_label.after(1000, expression_label.configure(background="green", text="correct"))

        elif(taf[3]==taf[2]):
            print("Wrong")
            print("correct answer is " + str(taf[1]))
        else:
            print(taf[3])
        print("----------------------")
        setup()
    def false_button_pressed():
        expression_label.configure(text=" ")
        if taf[3]==taf[1]:
            print("Wrong")
        elif(taf[3]==taf[2]):
            print("Correct")
        else:
            print(taf[3])
        print("----------------------")
        setup()


    true_button = ttk.Button(window, text = "True", command = true_button_pressed).grid(column = 1, row = 3)
    false_button = ttk.Button(window, text = "False", command = false_button_pressed).grid(column = 4, row = 3)


setup()

window.mainloop()