from tkinter import *
from tkinter import messagebox
import pyperclip
import random
import string
import json

FONT_NAME = "Courier"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pass_generator(size=12, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase + string.punctuation):
    new_password = ''.join(random.choice(chars) for _ in range(size))
    password_entry.insert(0, f"{new_password}")
    pyperclip.copy(new_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    website_to_save = website_entry.get()
    username_to_save = username_entry.get()
    password_to_save = password_entry.get()
    # filename = "data.txt"
    new_data = {
        website_to_save: {
            "email": username_to_save, "password": password_to_save,
        }
    }

    if len(website_to_save) == 0 or len(username_to_save) == 0 or len(password_to_save) == 0:
        messagebox.showinfo(title="Empty", message="Enter the data")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # saving the updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    website_to_search = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="Data file not found")
    else:
        if website_to_search in data:
            user_email = data[website_to_search]["email"]
            user_password = data[website_to_search]["password"]
            messagebox.showinfo(title=website_to_search,
                                message=f"Email: {user_email}\nPassword: {user_password}")
        else:
            messagebox.showinfo(title="Error", message="Website file not found")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.resizable(width=False, height=False)
window.title("Password Manager")
window.config(padx=20, pady=20)

# canvas
canvas = Canvas(width=300, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website = Label(text="Website:", width=10, height=1)
website.grid(column=0, row=1)

website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)

username = Label(text="Email/Username:", width=15, height=1)
username.grid(column=0, row=2)

username_entry = Entry(width=35, fg="grey")
username_entry.insert(0, "login@gmail.com")
username_entry.grid(column=1, row=2, columnspan=2)

password = Label(text="Password:", width=21, height=1)
password.grid(column=0, row=3)

password_entry = Entry(width=35)
password_entry.grid(column=1, row=3, columnspan=2)

generate_button = Button(width=15, text="Generate", command=pass_generator, font=(FONT_NAME, 10))
generate_button.grid(column=2, row=1, columnspan=2)

add_button = Button(width=15, text="Add", command=save_data, font=(FONT_NAME, 10))
add_button.grid(column=2, row=2, columnspan=2)

search_button = Button(width=15, text="Search", command=find_password, font=(FONT_NAME, 10))
search_button.grid(column=2, row=3, columnspan=2)



window.mainloop()