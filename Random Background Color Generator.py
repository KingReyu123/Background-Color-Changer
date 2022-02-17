from tkinter import *
import random

root= Tk()
root.title("Random Background Generator")
root.geometry("600x400")

dictionary= {'colors': ['magneta', 'chocolate', 'purple', 'lawn green', 'silver', 'red']}

def bg_color():
    random_color= random.randint(0,6)
    print(dictionary["colors"][random_color])
    root.configure(background= dictionary["colors"][random_color])
    
btn= Button(root, text="Generate background color", command= bg_color)
btn.place(relx= 0.5, rely= 0.5, anchor= CENTER)

root.mainloop()