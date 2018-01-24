import GUI.ComboBoxes as combo
import GUI.Labels as label
import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Workhorse")

label.Labels.min(window)
label.Labels.max(window)
label.Labels.duration(window)

combo.ComboBoxes.minValue(window)
combo.ComboBoxes.maxValue(window)
combo.ComboBoxes.duration(window)

label.Labels.expression(window)



window.mainloop()