# just a little window to choose among a list of known paths

import tkinter as tk

window = tk.Tk()

lbl_text = tk.Label(text="Choose among saved local paths")
lbl_text.grid(row=0, column=0)

lbl_text.mainloop()