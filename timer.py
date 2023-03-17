from datetime import datetime
import tkinter as tk
from tkinter import *
import ttkbootstrap as ttk

def Draw():
    global text

    frame=tk.Frame(app,width=100,height=100,relief='solid',bd=1)
    frame.place(x=10,y=50)
    text=tk.Label(frame,text='HELLO',font=("Arial",33))
    text.pack()

def Refresh():
    tme = datetime.now().strftime("%H:%M:%S")
    # print(tme)
    text.configure(text=tme)
    app.after(1000, Refresh)

if __name__=="__main__":
    # app = tk.Tk()
    app = ttk.Window(title="Time", themename="darkly", resizable=(False, False))
    app.geometry('280x180')
    app.resizable(0, 0)
    app.attributes('-topmost', True)
    Draw()
    
    Refresh()
    app.mainloop()
        