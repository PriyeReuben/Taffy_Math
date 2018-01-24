import tkinter as tk
from tkinter import ttk
import logic as taffy

taf = taffy.Taffy().math()

class Labels:

    def min(window):
        min_label = tk.Label(window, text="Minimum factor:")
        min_label.grid(column=1, row=0)

    def max(window):
        max_label = tk.Label(window, text="Maximum factor:")
        max_label.grid(column=5, row=0)

    def duration(window):
        duration_label = tk.Label(window, text="Duration:")
        duration_label.grid(column=9, row=0)

    def expression(window):
        expression_label = tk.Label(window, text=taf[0], background = "blue", relief = "raised", height=2)
        expression_label.grid(column=2, row=4)
