from tkinter import *

def HelloWorld(): 
    fenetre = Tk()
    fenetre.title("Hello World")
    fenetre.geometry("455x250")
    fenetre.config(bg = "#00FFFF")
    label1 = Label (fenetre, text = "Yes Hello world")
    label1.pack()
    label1.config(fg="#00FF00")
    fenetre.mainloop()
    
    
HelloWorld
