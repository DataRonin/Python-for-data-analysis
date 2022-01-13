import tkinter as tk  # empfohlene Import-Option

root = tk.Tk()        # Instantiierung von Tk
                      # erzeugt "Label" widget
w = tk.Label(root,text="Hello, world!")
w. pack()             # Geometriemanager pack()
root.mainloop()       # startet den eventloop.