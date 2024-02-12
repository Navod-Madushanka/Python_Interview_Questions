from tkinter import *


def button_click():
    label.config(text=input_field.get())


window = Tk()
window.title("First project")
window.minsize(600, 500)
window.config(padx=20, pady=20)

label = Label(text="My Label", font=("Arial", 24, "bold"))
label.grid(column=0, row=0)

btn = Button(text="Click Me", command=button_click)
btn.grid(column=1, row=1)

btn = Button(text="Click Me 2", command=button_click)
btn.grid(column=2, row=0)

input_field = Entry()
input_field.grid(column=4, row=2)

window.mainloop()
