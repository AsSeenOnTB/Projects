import tkinter as tk
import tkinter.ttk as ttk
from os import *


of = tk.TK()
of.title("Open file")
os_str_var = tk.StringVar(of)


def viewNotebook():
    try:
        print(os_str_var.get())
        tk.Label(of, text=f'{os_str_var.get()}'.pack() )
        get_os_input = os_str_var.get()
        startfile(f"{get_os_input}")
        tk.Label(of, text=f"Good News! The system can find the path({get_os_input}) specified").pack()
        return get_os_input
    except:
        tk.Label(of, text="The system cannot find the path specified.  ").pack()
        print("The system cannot find the path specified  ")
        
        os_entry = tk.Entry(of, textvariable=os_str_var).pack()
        os_button = tk.Button(of, text='Open', command=get_value_os).pack()
        of.mainloop()