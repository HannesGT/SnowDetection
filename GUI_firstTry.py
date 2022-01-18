import tkinter
from PIL import Image, ImageTk
import pandas as pd
import openpyxl

v = 0


def next():
    global v
    global filename
    global pic_load
    global pathtraining
    global pic
    global rate
    global snow
    global s
    global snowmodule
    global sm
    global gras
    global g
    global time
    global t
    global spezial
    global sp
    global length
    v = v + 1
    if v == length:
        v = 0
    filename = str(file[v])  # Dateiname als String der jeweiligen Spalte
    pic_load = Image.open(pathtraining + '\\' + filename).resize((576, 324))
    pic = ImageTk.PhotoImage(pic_load)  # Nötig um Bild ins Fenster einzufügen
    pic_put.config(image=pic)
    rate = rating['y wenn Bewertung möglich']  # die Spalte mit der Bewertungsangabe
    r = rate[v]  # Bewertung für das entsprechende Bild
    if r == 'y':
        r = 'ja'
    elif r == 'n':
        r = 'nein'
    else:
        r = 'nicht angegeben'
    snow = rating['y wenn Schnee']  # die Spalte mit der Schneeangabe
    s = snow[v]  # Schneebewertung für das entsprechende Bild
    if s == 'y':
        s = 'ja'
    elif s == 'n':
        s = 'nein'
    else:
        s = 'nicht angegeben'
    snowmodule = rating['y wenn Schnee auf Modul']  # die Spalte mit der Schneeangabe für die Module
    sm = snowmodule[v]  # Schneebewertung der Module für das entsprechende Bild
    if sm == 'y':
        sm = 'ja'
    elif sm == 'n':
        sm = 'nein'
    else:
        sm = 'nicht angegeben'
    gras = rating['1= kurz, 2= lang, 3=zulang']  # die Spalte mit der Grashöhenangabe
    g = gras[v]  # Grasbewertung für das entsprechende Bild
    if g == 1:
        g = 'kurz'
    elif g == 2:
        g = 'lang'
    elif g == 3:
        g = 'zulang'
    else:
        g = 'nicht definiert'
    time = rating['y, wenn Tag']  # die Spalte mit der Tageszeit
    t = time[v]  # Tageszeitbewertung für das entsprechende Bild
    if t == 'y':
        t = 'Tag'
    elif t == 'n':
        t = 'Nacht'
    else:
        t = 'nicht zu erkennen'
    spezial = rating['Besonderheit']  # die Spalte für Besonderheiten
    sp = spezial[v]  # Besonderheiten für das entsprechende Bild

    rating_label.config(text='Ist eine Bewertung möglich? ' + r)
    snow_label.config(text='Liegt Schnee? ' + s)
    snowmodule_label.config(text='Liegt Schnee auf den Modulen? ' + sm)
    gras_label.config(text='Wie hoch ist das Gras? ' + g)
    time_label.config(text='Es ist:  ' + t)
    spezial_label.config(text='Besonderheiten:  ' + sp)


def back():
    global v
    global filename
    global pic_load
    global pathtraining
    global pic
    global rate
    global snow
    global s
    global snowmodule
    global sm
    global gras
    global g
    global time
    global t
    global spezial
    global sp
    global length
    v = v - 1
    if v == -1:
        v = length -1
    filename = str(file[v])  # Dateiname als String der jeweiligen Spalte
    pic_load = Image.open(pathtraining + '\\' + filename).resize((576, 324))
    pic = ImageTk.PhotoImage(pic_load)  # Nötig um Bild ins Fenster einzufügen
    pic_put.configure(image=pic)

    r = rate[v]  # Bewertung für das entsprechende Bild
    if r == 'y':
        r = 'ja'
    elif r == 'n':
        r = 'nein'
    else:
        r = 'nicht angegeben'
    snow = rating['y wenn Schnee']  # die Spalte mit der Schneeangabe
    s = snow[v]  # Schneebewertung für das entsprechende Bild
    if s == 'y':
        s = 'ja'
    elif s == 'n':
        s = 'nein'
    else:
        s = 'nicht angegeben'
    snowmodule = rating['y wenn Schnee auf Modul']  # die Spalte mit der Schneeangabe für die Module
    sm = snowmodule[v]  # Schneebewertung der Module für das entsprechende Bild
    if sm == 'y':
        sm = 'ja'
    elif sm == 'n':
        sm = 'nein'
    else:
        sm = 'nicht angegeben'
    gras = rating['1= kurz, 2= lang, 3=zulang']  # die Spalte mit der Grashöhenangabe
    g = gras[v]  # Grasbewertung für das entsprechende Bild
    if g == 1:
        g = 'kurz'
    elif g == 2:
        g = 'lang'
    elif g == 3:
        g = 'zulang'
    else:
        g = 'nicht definiert'
    time = rating['y, wenn Tag']  # die Spalte mit der Tageszeit
    t = time[v]  # Tageszeitbewertung für das entsprechende Bild
    if t == 'y':
        t = 'Tag'
    elif t == 'n':
        t = 'Nacht'
    else:
        t = 'nicht zu erkennen'
    spezial = rating['Besonderheit']  # die Spalte für Besonderheiten
    sp = spezial[v]  # Besonderheiten für das entsprechende Bild

    rating_label.config(text='Ist eine Bewertung möglich? ' + r)
    snow_label.config(text='Liegt Schnee? ' + s)
    snowmodule_label.config(text='Liegt Schnee auf den Modulen? ' + sm)
    gras_label.config(text='Wie hoch ist das Gras? ' + g)
    time_label.config(text='Es ist:  ' + t)
    spezial_label.config(text='Besonderheiten:  ' + sp)

def choise():
    global v
    global filename
    global pic_load
    global pathtraining
    global pic
    global rate
    global snow
    global s
    global snowmodule
    global sm
    global gras
    global g
    global time
    global t
    global spezial
    global sp
    global length
    filename = list.get('active')  # Dateiname als String der jeweiligen Spalte
    pic_load = Image.open(pathtraining + '\\' + filename).resize((576, 324))
    pic = ImageTk.PhotoImage(pic_load)  # Nötig um Bild ins Fenster einzufügen
    pic_put.configure(image=pic)


    r = rate[v]  # Bewertung für das entsprechende Bild
    if r == 'y':
        r = 'ja'
    elif r == 'n':
        r = 'nein'
    else:
        r = 'nicht angegeben'
    snow = rating['y wenn Schnee']  # die Spalte mit der Schneeangabe
    s = snow[v]  # Schneebewertung für das entsprechende Bild
    if s == 'y':
        s = 'ja'
    elif s == 'n':
        s = 'nein'
    else:
        s = 'nicht angegeben'
    snowmodule = rating['y wenn Schnee auf Modul']  # die Spalte mit der Schneeangabe für die Module
    sm = snowmodule[v]  # Schneebewertung der Module für das entsprechende Bild
    if sm == 'y':
        sm = 'ja'
    elif sm == 'n':
        sm = 'nein'
    else:
        sm = 'nicht angegeben'
    gras = rating['1= kurz, 2= lang, 3=zulang']  # die Spalte mit der Grashöhenangabe
    g = gras[v]  # Grasbewertung für das entsprechende Bild
    if g == 1:
        g = 'kurz'
    elif g == 2:
        g = 'lang'
    elif g == 3:
        g = 'zulang'
    else:
        g = 'nicht definiert'
    time = rating['y, wenn Tag']  # die Spalte mit der Tageszeit
    t = time[v]  # Tageszeitbewertung für das entsprechende Bild
    if t == 'y':
        t = 'Tag'
    elif t == 'n':
        t = 'Nacht'
    else:
        t = 'nicht zu erkennen'
    spezial = rating['Besonderheit']  # die Spalte für Besonderheiten
    sp = spezial[v]  # Besonderheiten für das entsprechende Bild

    rating_label.config(text='Ist eine Bewertung möglich? ' + r)
    snow_label.config(text='Liegt Schnee? ' + s)
    snowmodule_label.config(text='Liegt Schnee auf den Modulen? ' + sm)
    gras_label.config(text='Wie hoch ist das Gras? ' + g)
    time_label.config(text='Es ist:  ' + t)
    spezial_label.config(text='Besonderheiten:  ' + sp)


path = r'C:\Users\DanielaSchumann\OneDrive - greentech GmbH\7_SnowDetector\Sonnen\Bewertung.xlsx'
pathtraining = r'C:\Users\DanielaSchumann\OneDrive - greentech GmbH\7_SnowDetector\Sonnen\training'

##Bewertungstabelle einlesen
rating = pd.read_excel(path)
identity = rating['id'] #die Spalte mit den ID-Nummern
file = rating['Dateinamen'] #die Spalte mit den Dateinamen
length = len(identity) #Länge der Spalte id


window = tkinter.Tk() # Erzeugt Fenster

window.title('Sonnen') # Name des Fensters

button_next = tkinter.Button(window, text='>', height=2, width=5, font=10, command=next) # Erstellt einen Button
button_next.pack(side='right') # Nötig, um Button einzufügen

show_button = tkinter.Button(window, text='Bild anzeigen', command=choise)
show_button.pack(side='bottom', anchor='sw', padx=5, pady=5)

list = tkinter.Listbox(window, height=30, width=30)
list.pack(side='left', padx=5, pady=5)


for x in range(0, length):
    filename_l = str(file[x])  # Dateiname als String der jeweiligen Spalte
    list.insert('end', filename_l)


button_back = tkinter.Button(window, text='<', height=2, width=5, font=10, command=back) # Erstellt einen Button
button_back.pack(side='left') # Nötig, um Button einzufügen



v = 0 # Laufvariable

filename = str(file[v]) # Dateiname als String der jeweiligen Spalte
pic_load = Image.open(pathtraining + '\\' + filename).resize((576, 324)) # Lädt das entsprechende Bild
pic = ImageTk.PhotoImage(pic_load) # Nötig um Bild ins Fenster einzufügen
pic_put = tkinter.Label(window, image=pic)


pic_put.pack(side='bottom')

rate = rating['y wenn Bewertung möglich'] #die Spalte mit der Bewertungsangabe
r = rate[v] #Bewertung für das entsprechende Bild
if r == 'y':
    r = 'ja'
elif r == 'n':
    r = 'nein'
else:
    r = 'nicht angegeben'
snow = rating['y wenn Schnee']  # die Spalte mit der Schneeangabe
s = snow[v]  # Schneebewertung für das entsprechende Bild
if s == 'y':
    s = 'ja'
elif s == 'n':
    s = 'nein'
else:
    s = 'nicht angegeben'
snowmodule = rating['y wenn Schnee auf Modul']  # die Spalte mit der Schneeangabe für die Module
sm = snowmodule[v]  # Schneebewertung der Module für das entsprechende Bild
if sm == 'y':
    sm = 'ja'
elif sm == 'n':
    sm = 'nein'
else:
    sm = 'nicht angegeben'
gras = rating['1= kurz, 2= lang, 3=zulang']  # die Spalte mit der Grashöhenangabe
g = gras[v] # Grasbewertung für das entsprechende Bild
if g == 1:
    g = 'kurz'
elif g == 2:
    g = 'lang'
elif g == 3:
    g = 'zulang'
else:
    g = 'nicht definiert'
time = rating['y, wenn Tag']  # die Spalte mit der Tageszeit
t = time[v]  # Tageszeitbewertung für das entsprechende Bild
if t == 'y':
    t = 'Tag'
elif t == 'n':
    t = 'Nacht'
else:
    t = 'nicht zu erkennen'
spezial = rating['Besonderheit']  # die Spalte für Besonderheiten
sp = spezial[v]  # Besonderheiten für das entsprechende Bild

rating_label = tkinter.Label(window, text='Ist eine Bewertung möglich? ' + r)
rating_label.pack()
snow_label = tkinter.Label(window, text='Liegt Schnee? ' + s)
snow_label.pack()
snowmodule_label = tkinter.Label(window, text='Liegt Schnee auf den Modulen? ' + sm)
snowmodule_label.pack()
gras_label = tkinter.Label(window, text='Wie hoch ist das Gras? ' + g)
gras_label.pack()
time_label = tkinter.Label(window, text='Es ist:  ' + t)
time_label.pack()
spezial_label = tkinter.Label(window, text='Besonderheiten:  ' + sp)
spezial_label.pack()

window.mainloop() # Nötig um Fenster zu öffnen
