import tkinter

window = tkinter.Tk() # Erzeugt Fenster

window.title('Sonnen') # Name des Fensters

button_next = tkinter.Button(window, text='>')
button_next.pack()

window.mainloop() # Nötig um Fenster zu öffnen
