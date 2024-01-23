from tkinter import *
import random


window = Tk()

title_list = ["One", "Two", "Three", "Four"]
random_title = random.choice(title_list)
window.title(random_title)
window.minsize(width=500, height=500)

label1 = Label(text="Test label 1")
label1.pack()


def button_clicked():
    output = input.get()
    label1["text"] = output


button = Button(text="Click Me", command=button_clicked)
button.pack()


input = Entry()
input.pack()


window.mainloop()
