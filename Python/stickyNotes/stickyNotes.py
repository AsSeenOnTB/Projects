# Created by TB
# github.com/AsSeenOnTB

# imports
import tkinter as tk
import tkinter.ttk as ttk
from functions import newNote

# Initialize the window
r = tk.Tk()

# Metadata
r.minsize(400, 400)
r.geometry("400x400+50+50")
r.title('Sticky Notes')

# Textbox
rt = tk.Text(r, height = 400, width=400).pack()


#Keybinds
r.bind('Control-n', newNote)


    




# Mainloop allows the program to stay in the system memory.  Find out how to make this a background process
r.mainloop()
