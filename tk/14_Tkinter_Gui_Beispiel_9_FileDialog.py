import tkinter as tk
from tkinter.filedialog import askopenfilename

root = tk.Tk()
def callbackopenfilename():
    name = askopenfilename()
    print (name)
b1=tk.Button(root,text='Open File', command=callbackopenfilename)
b1.pack(fill=tk.X)
root.mainloop()

