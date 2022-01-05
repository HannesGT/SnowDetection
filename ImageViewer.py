#xrld package installieren
#pandas package installieren
#anaconda package installieren
#openpyxl package installieren
#join package installieren
#Pillow package installieren
import os
import pandas as pd
import join
import xlrd
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
## Pfad der Bewertungstabellen-Datei
path = r'C:\Users\DanielaSchumann\OneDrive - greentech GmbH\7_SnowDetector\Sonnen\Bewertung.xlsx'
pathtraining = r'C:\Users\DanielaSchumann\OneDrive - greentech GmbH\7_SnowDetector\Sonnen\training'

##Bewertungstabelle einlesen
rating = pd.read_excel(path)
identity = rating['id'] #die Spalte mit den ID-Nummern
file = rating['Dateinamen'] #die Spalte mit den Dateinamen
#l = len(identity) #Länge der Spalte id
l = 2
for x in range(0, l): #von 1 bis Anzahl der Bilder
    filename = str(file[x]) #Dateiname als String der jeweiligen Spalte
    pic = Image.open(pathtraining + '\\' + filename) #lädt das entsprechende Bild
    rate = rating['y wenn Bewertung möglich'] #die Spalte mit der Bewertungsangabe
    r = rate[x] #Bewertung für das entsprechende Bild
    snow = rating['y wenn Schnee']  # die Spalte mit der Schneeangabe
    s = snow[x]  # Schneebewertung für das entsprechende Bild
    snowmodule = rating['y wenn Schnee auf Modul']  # die Spalte mit der Schneeangabe für die Module
    sm = snowmodule[x]  # Schneebewertung der Module für das entsprechende Bild
    gras = rating['1= kurz, 2= lang, 3=zulang']  # die Spalte mit der Grashöhenangabe
    g = gras[x] # Grasbewertung für das entsprechende Bild
    if g == 1:
        g = 'kurz'
    elif g == 2:
        g = 'lang'
    elif g == 3:
        g = 'zulang'
    else:
        g = 'nicht definiert'
    time = rating['y, wenn Tag']  # die Spalte mit der Tageszeit
    t = time[x]  # Tageszeitbewertung für das entsprechende Bild
    spezial = rating['Besonderheit']  # die Spalte für Besonderheiten
    sp = spezial[x]  # Besonderheiten für das entsprechende Bild
    picRate = ImageDraw.Draw(pic)
    picspes = ImageFont.truetype('arial.ttf', 40)
    picRate.text((20, 1000), 'Bewertung möglich?: ' + r, font=picspes, fill=(250, 250, 0))
    picRate.text((20, 1050), 'Liegt Schnee?: ' + s, font=picspes, fill=(250, 250, 0))
    picRate.text((20, 1100), 'Liegt Schnee auf den Modulen?: ' + sm, font=picspes, fill=(250, 250, 0))
    picRate.text((20, 1150), 'Wie hoch ist das Gras?: ' + g, font=picspes, fill=(250, 250, 0))
    picRate.text((20, 1200), 'Ist Tag?: ' + t, font=picspes, fill=(250, 250, 0))
    picRate.text((20, 1250), 'Besonderheiten: ' + sp, font=picspes, fill=(250, 250, 0))
    pic.show()