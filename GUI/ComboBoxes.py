import tkinter as tk
from tkinter import ttk

class ComboBoxes:
    def minValue(window):
        min_value = tk.StringVar()
        min_value_chosen = ttk.Combobox(window, width=8, textvariable=min_value, state="readonly")
        min_value_chosen['values'] = (1, 5, 10, 15, 20, 25)
        min_value_chosen.grid(column=1, row=1)
        min_value_chosen.current(0)  # this assignes the first value in the tuple to be displaed in the combobox

    def maxValue(window):
        max_value = tk.StringVar()
        max_value_chosen = ttk.Combobox(window, width=8, textvariable=max_value, state="readonly")
        max_value_chosen['values'] = (1, 5, 10, 15, 20, 25)
        max_value_chosen.grid(column=5, row=1)
        max_value_chosen.current(0)  # this assignes the first value in the tuple to be displaed in the combobox

    def duration(window):
        duration = tk.StringVar()
        duration_chosen = ttk.Combobox(window, width=8, textvariable=duration, state="readonly")
        duration_chosen['values'] = (15, 30, 45, 60)
        duration_chosen.grid(column=9, row=1)
        duration_chosen.current(0)
