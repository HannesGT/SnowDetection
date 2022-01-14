import tkinter
from PIL import Image, ImageTk
import pandas as pd
import openpyxl

path = r'C:\Users\DanielaSchumann\OneDrive - greentech GmbH\7_SnowDetector\Sonnen\Bewertung.xlsx'
pathtraining = r'C:\Users\DanielaSchumann\OneDrive - greentech GmbH\7_SnowDetector\Sonnen\training'

##Bewertungstabelle einlesen
rating = pd.read_excel(path)
identity = rating['id'] #die Spalte mit den ID-Nummern
file = rating['Dateinamen'] #die Spalte mit den Dateinamen
#l = len(identity) #Länge der Spalte id

window = tkinter.Tk() # Erzeugt Fenster

window.title('Sonnen') # Name des Fensters

button_next = tkinter.Button(window, text='>') # Erstellt einen Button
button_next.pack() # Nötig, um Button einzufügen

filename = str(file[0]) # Dateiname als String der jeweiligen Spalte
pic_load = Image.open(pathtraining + '\\' + filename).resize((576, 324)) # Lädt das entsprechende Bild
pic = ImageTk.PhotoImage(pic_load) # Nötig um Bild ins Fenster einzufügen
pic_put = tkinter.Label(window, image=pic)

pic_put.pack()

window.mainloop() # Nötig um Fenster zu öffnen
