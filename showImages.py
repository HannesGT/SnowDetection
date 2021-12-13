# skript / function um die Bilder inkl. der Bewertung anzuzeigen
# Ziel könnte sein: Auswahl eines Pfads (etwa "Sonnen"). Fenster mit links ->Liste der Bewertungsdatei (Filterung möglich?)
# Fenster rechts -> Anzeige des Fotos mit der Klassifizierung (muss ja nicht im Bild sein)
4234
import pandas   # read excel
import PIL      # Anzeige Bilder
#from tkinter import *  # GUI
from tkinter import filedialog  # GUI
testHS
import tkinter
#sds
def browse_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path
    filename = tkinter.filedialog.askdirectory()
    folder_path.set(filename)

def chose_presetF():
    # chose known folder
    global folder_path
    folder_path.set("C:/Users/HannesSchütze/OneDrive - greentech/1_Data_Analysis/7_SnowDetector/Sonnen")

root = tkinter.Tk()
root.title('Snow Detection V1.0')
root.geometry('500x200')
folder_path = tkinter.StringVar()
folder_path.set("Bitte einen Trainingsordner auswählen..")

labelPath = tkinter.Label(master=root, textvariable=folder_path, anchor= "w")
labelPath.place(x=5, y=5, width=300, height=40)
labelPath.pack()

button2 = tkinter.Button(root,text="Browse", command=browse_button)
button2.place(x=5, y=60)

button3 = tkinter.Button(root, text="Use Sonnen HS",command=chose_presetF)
button3.place(x=5, y=100)

button4 = tkinter.Button(root, text="Open",command=chose_presetF)
button4.place(x=300, y=60)

root.mainloop()

print(folder_path)

# Set image training path:
#trainingPath = "C:/Users/HannesSchütze/OneDrive - greentech/1_Data_Analysis/7_SnowDetector/Sonnen"
#Bewertung = pandas.read_excel(trainingPath + "/Bewertung.xlsx.")

#A = PIL.Image.open(trainingPath + "/training/" + Bewertung.Dateinamen[1])
#window = tkinter.Tk()
#window.mainloop()