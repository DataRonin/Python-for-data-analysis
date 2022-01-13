import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog


root = tk.Tk()

def callbackdeletefile():
    myint = simpledialog.askinteger(title='Some random window', prompt='Enter a number yo', minvalue=1,
                                            maxvalue=1236546)
    messagebox.showinfo('info', f"Output: {myint}")


b1=tk.Button(root,text='Enter a number', command=callbackdeletefile)
#Button(root,text='Datei löschen', bg = 'red', command=callbackdeletefile)
b1.pack(expand =1, fill=tk.X)
root.mainloop()