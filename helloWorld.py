from tkinter import *

def HelloWorld(): 
    fenetre = Tk()
    fenetre.title("Hello World")
    fenetre.geometry("200x200")
    label1 = Label (fenetre, text = "Hello world")
    label1.pack()
    label1.config(fg="#FFFF00")
    fenetre.mainloop()
    
    
HelloWorld