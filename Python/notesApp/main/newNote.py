import tkinter as tk
import tkinter.ttk as ttk

#New Notebook
def newNote():
    nn = tk.Toplevel()
    nn.title('New Notes')
    nn.config(height=400, width=400)
    nnt = tk.Text(nn, height=5, width=52)
    nnt.pack()

    