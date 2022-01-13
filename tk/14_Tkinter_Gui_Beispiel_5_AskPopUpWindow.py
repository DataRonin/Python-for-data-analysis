import tkinter as tk # tkinter importieren, umbenannt zu tk
class Application(tk.Frame): # Klasse "erbt" von "Frame" Klasse
    def __init__(self, master=None):
        tk.Frame.__init__(self, master) # Init Methode der Elternklasse "Frame"
        self.pack() # Erforderlich zur Darstellung
        self.createWidgets() # Aufruf der Widget-Erzeugung
    def createWidgets(self):
        self.quitButton = tk.Button(self, text='Quit', command=self.quit) # erzeugt "Quit" button
        self.quitButton.pack() # Darstellung
app = Application() # Hauptprogramm startet durch Instantiierung
app.master.title('Hallo, tkinter') # Titel erzeugen
app.mainloop() # Event Loop starten (Maus- und Keyboard)