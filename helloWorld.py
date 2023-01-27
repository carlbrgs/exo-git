from tkinter import *

def HelloWorld(): 
    fenetre = Tk()
    fenetre.title("Hello World")
    fenetre.geometry("200x200")
    label1 = Label (fenetre, text = "Hello world",fg='#0000FF')
    label1.pack()
    label1.config(fg="#00FF00")
    fenetre.mainloop()
    
    
HelloWorld