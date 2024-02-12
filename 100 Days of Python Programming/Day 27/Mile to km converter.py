from tkinter import *


def convert():
    miles = entry.get()
    km = round((float(miles) * 1.609))
    km_label.config(text=str(km))


window = Tk()
window.minsize(width=300, height=100)
window.title("Miles to KM Convertor")
window.config(pady=20, padx=20)

entry = Entry()
entry.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

inform_label = Label(text="is equal to")
inform_label.grid(column=0, row=1)

km_label = Label(text="0")
km_label.grid(column=1, row=1)

km_indicator_label = Label(text="km")
km_indicator_label.grid(column=2, row=1)

btn = Button(text="Convert", command=convert)
btn.grid(column=1, row=2)

window.mainloop()
