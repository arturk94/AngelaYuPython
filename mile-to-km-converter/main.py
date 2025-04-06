from tkinter import *

window = Tk()

window.title("Mile to km converter")
window.minsize(width=250, height=100)
window.config(padx=20, pady=20)

new_input = Entry(width=7)
new_input.insert(END, string="0")
new_input.grid(column=1, row=0)

new_label = Label(text="Miles", font=("Arial",18,"bold"))
new_label.grid(column=2, row=0)

new_label2 = Label(text="is equal to", font=("Arial",18,"bold"))
new_label2.grid(column=0, row=1)

new_label3 = Label(text="0", font=("Arial",18,"bold"))
new_label3.grid(column=1, row=1)

new_label4 = Label(text="km", font=("Arial",18,"bold"))
new_label4.grid(column=2, row=1)

def calculate():
    mile = new_input.get()
    if not mile == "None":
        new_label3.config(text=(float(mile) * 1.609344))


new_button = Button(text="Calculate", command=calculate)
new_button.config(bg='black', fg='white')
new_button.config(font=('helvetica', 20, 'underline italic'))
new_button.grid(column=1, row=2)

window.mainloop()