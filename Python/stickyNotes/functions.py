import tkinter as tk
import tkinter.ttk as ttk

# Function to add a new note based on a keybind
def newNote():
    nn = tk.Toplevel().Text(nn,height=400, width=400).pack()
    nn.minsize(400, 400)
    nn.title('Sticky Note')
    nn.geometry("400x400+40+50")