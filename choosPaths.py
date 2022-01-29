# just a little window to choose among a list of known paths

import os
import tkinter as tk
chosenPath = open("config/trainPath").read()     # current path from config file
loadPath = chosenPath

def closeGoBack():
    # dont change path
    global chosenPath
    chosenPath = loadPath
    window.destroy()

def saveGoBack():
    global chosenPath
    chosenPath=txB.get(txB.curselection())
    # end window
    window.destroy()

window = tk.Tk()

lbl_text = tk.Label(text = "Current path is")
lbl_text.grid(row=0, column=0, padx=5, pady=5, sticky="w")

lbl_current = tk.Label(text=chosenPath)
lbl_current.grid(row=1, column=0, padx=5, pady=5, sticky="w")

lbl_text = tk.Label(text = "Change to saved local path")
lbl_text.grid(row=2, column=0, padx=5, pady=5, sticky="w")

txB = tk.Listbox(width=100)

txB.insert(1, "C:\\Users\\DanielaSchumann\\OneDrive - greentech GmbH\\7_SnowDetector\\Sonnen")
txB.insert(2, "C:\\Users\\Hansi\\Documents\\SonnenDaten")
txB.insert(3, "tbd..")
txB.insert(4, "tbd")

txB.grid(row=3, column=0, padx=5, pady=5, sticky="w")

btn_ok = tk.Button(text="choose",command = saveGoBack)
btn_ok.grid(row=4, column=0, padx=5, pady=5, sticky="w")

btn_clo = tk.Button(text="close",command = closeGoBack)
btn_clo.grid(row=5, column=0, padx=5, pady=5, sticky="w")

window.mainloop()

# write to config
loadPath = open("config/trainPath", mode="w")
loadPath.write(chosenPath)
loadPath.close()

os.system('Cockpit.py')