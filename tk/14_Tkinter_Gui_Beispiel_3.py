# 1. Modul tkinter importieren
import tkinter # einfache Import-Option

#2. tkinter initialisieren und Verweis
root = tkinter.Tk()

#3. Widget vom Typ "Label" erzeugen mit Text = "Hello World!"
w = tkinter.Label(root,text="Hello, world!")

#4. Geometriemanager "pack" für Label starten
w. pack()

# 5. Eventloop starten
root.mainloop()