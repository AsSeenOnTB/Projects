import tkinter as tk
import tkinter.ttk as ttk
from newNote import newNote

#Initializes the main window
mm = tk.Tk()
mm.title('Notes')

#Set the dimensions and center them
mm.geometry('600x400+50+50')

#Dimensions
ww = 600
wh = 400

#Finding the center
sw = mm.winfo_screenwidth()
sh = mm.winfo_screenheight()
cx = int(sw / 2 - ww/2)
cy = int(sh / 2 - wh/2)


#Centering
mm.geometry(f'{ww}x{wh}+{cx}+{cy}')
#Rezizing Main Menu will be diabled, as the window will be closed once a option is chosen
mm.resizable(False, False)

#Opens a new window
    

#New Notebook button
nnb = ttk.Button(mm, text='New Note',command=newNote)
nnb.pack(pady=10, padx=10, expand=False)

#View Notebooks button
vnb = ttk.Button(mm, text='View Notebooks', command=newNote)
vnb.pack(padx=10, pady=10, expand=False)

#Exit
ep = ttk.Button(mm,text='Exit', command=mm.destroy)
ep.pack(padx=10, pady=10, expand=False)


#mainloop
mm.mainloop()