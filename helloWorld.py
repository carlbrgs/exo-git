from tkinter import *

def HelloWorld(): 
    fenetre = Tk()
    fenetre.title("Hello World")
    fenetre.geometry("250x250")
    fenetre.config(bg = "#FFFF00")
    label1 = Label (fenetre, text = "Yes Hello world")
    label1.pack()
    label1.config(fg="#00FF00")
    fenetre.mainloop()
    
    
HelloWorld
