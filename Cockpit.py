# skript / function um die Bilder inkl. der Bewertung anzuzeigen
# Ziel könnte sein: Auswahl eines Pfads (etwa "Sonnen"). Fenster mit links ->Liste der Bewertungsdatei (Filterung möglich?)
# Fenster rechts -> Anzeige des Fotos mit der Klassifizierung (muss ja nicht im Bild sein)

import tkinter as tk
import os
# from tkinter import *  # GUI
from tkinter import filedialog  # GUI
loadPath = open("config/trainPath").read()     # read path from config file

def browse_button():
    # Allow user to select a directory and store it in global var called folder_path
    filename = tk.filedialog.askdirectory()
    folder_path.set(filename)

def chose_preset():
    # chose known folder
    root.destroy()
    os.system('choosPaths.py')

def open_viewer():
    # save seleted path to config
    open("config/trainPath",mode="w").write(folder_path.get())
    root.destroy()
    os.system('ImageWindow.py')

def open_training():
    #tbd
    open("config/trainPath",mode="w").write(folder_path.get())
    1+1


root = tk.Tk()
root.title('Snow Detection V1.0')
folder_path = tk.StringVar()
folder_path.set(loadPath)

frm_intro = tk.Frame()
lbl_intro1 = tk.Label(master=frm_intro,text="Cockpit: Auswahl des Trainingsordners", font="1")
lbl_intro1.grid(row=0, column=0, sticky="w")
lbl_intro2 = tk.Label(master=frm_intro,text="Dieser enthält die Datei 'Bewertung.xlsx' und den Ordner 'training'.")
lbl_intro2.grid(row=1, column=0, sticky="w")
frm_intro.grid(row=0, column=0, padx=5, pady=5, sticky="w")

lbl_path = tk.Entry(textvariable=folder_path)
lbl_path.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

btn_browse = tk.Button(text="Browse", command=browse_button)
btn_browse.grid(row=2, column=0, padx=5, pady=5, sticky="w")

btn_known = tk.Button(text="Chose known folder",command=chose_preset)
btn_known.grid(row=3, column=0, padx=5, pady=5, sticky="w")

btn_view = tk.Button(root, text="View images",command=open_viewer, bg="lightblue")
btn_view.grid(row=1, column=1, padx=5, pady=5, sticky="w")

btn_trainer = tk.Button(root, text="Trainer",command=open_training, bg="lightgreen")
btn_trainer.grid(row=2, column=1, padx=5, pady=5, sticky="w")

root.mainloop()

# Set image training path:
#trainingPath = "C:/Users/HannesSchütze/OneDrive - greentech/1_Data_Analysis/7_SnowDetector/Sonnen"
#Bewertung = read_excel(trainingPath + "/Bewertung.xlsx.")

#A = PIL.Image.open(trainingPath + "/training/" + Bewertung.Dateinamen[1])
#window = tkinter.Tk()
#window.mainloop()