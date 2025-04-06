from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

WHITE = "#ffffff"
BLACK = "#000000"
FONT_NAME = "Arial"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    password_input.delete(0,END)
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)

# ---------------------------- SEARCH PASSWORD ------------------------------- #
def find_password():
    website = website_input.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists")



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=WHITE)

canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
lock_img = PhotoImage(file="logo.gif")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", font=(FONT_NAME,12), bg=WHITE, fg=BLACK)
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:", font=(FONT_NAME,12), bg=WHITE, fg=BLACK)
email_label.grid(column=0, row=2)

password_label = Label(text="Password:", font=(FONT_NAME,12), bg=WHITE, fg=BLACK)
password_label.grid(column=0, row=3)

website_input = Entry(width=27)
website_input.grid(column=1, row=1, columnspan=2, sticky=W)
website_input.focus()

email_input = Entry(width=45)
email_input.grid(column=1, row=2, columnspan=2, sticky=W)
email_input.insert(0, "artur@knothe.org")

password_input = Entry(width=27)
password_input.grid(column=1, row=3, sticky=W)

add_button = Button(text="Add", width=55, command=save)
add_button.config(bg=WHITE, fg=BLACK)
add_button.config(font=(FONT_NAME, 12, 'underline italic'))
add_button.grid(column=1, row=4, columnspan=2, sticky=W)

generate_password_button = Button(text="Generate Password", command=generate_password, width=18)
generate_password_button.config(bg=WHITE, fg=BLACK)
generate_password_button.config(font=(FONT_NAME, 12, 'underline italic'))
generate_password_button.grid(column=2, row=3, sticky=W)

search_button = Button(text="Search", command=find_password, width=18)
search_button.config(bg=WHITE, fg=BLACK)
search_button.config(font=(FONT_NAME, 12, 'underline italic'))
search_button.grid(column=2, row=1, sticky=W)

window.mainloop()