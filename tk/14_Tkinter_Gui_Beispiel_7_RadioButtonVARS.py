import tkinter as tk
root = tk.Tk()
myVar = tk.IntVar()

lab  = tk.Label(root, text="""Waehlen Sie Ihre Lieblingssorte:""", justify = tk.CENTER, padx = 10,font=("arial",12)).grid(column=0)
lab1 = tk.Label(root, text="""Strowberries""", justify = tk.LEFT, padx = 10,font=("modern",14)).grid(column=1)
       tk.Button(root, text="Tally", justify = tk.LEFT, padx = 10,font=("modern",14), command=root.destroy).grid(column=2)
# for val, taste in enumerate(tastes):
#     tk.Radiobutton(root,
#     text=taste,
#     padx = 10,
#     variable=myVar,
#     indicatoron=0,
#     command=ShowChoice,value=val).grid(sticky="E"+"W")
tk.Button(root, text="close", command=root.destroy).grid()
root.mainloop()


