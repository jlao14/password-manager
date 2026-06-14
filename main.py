from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letter + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)

    if len(password_entry.get()) != 0:
        yesno_pass = messagebox.askyesno(title="Error", message="There is already a password!\n"
                                                                "Do you wish to generate again?")
        if yesno_pass:
            password_entry.delete(0, END)
            password_entry.insert(0, password)
            pyperclip.copy(password)
    else:
        password_entry.insert(0, password)
        pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    new_website = website_entry.get()
    new_user = user_entry.get()
    new_password = password_entry.get()
    new_data = {
        new_website: {
            "username": new_user,
            "password": new_password
        }
    }

    if len(new_website) == 0 or len(new_password) == 0:
        messagebox.showerror(title="Error", message="Please don't leave any fields empty!")
    else:
        yes_no = messagebox.askyesno(title=new_website, message=f"These are the details you have entered:\n"
                                                                f"\nUsername: {new_user}\nPassword: {new_password}\n"
                                                                f"\nDo you wish to save?")
        if yes_no:
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
# ---------------------------- SEARCH BUTTON ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="Data file not found.")
    else:
        if website in data:
            username = data[website]["username"]
            password = data[website]["password"]
            messagebox.showinfo(title="Password Details", message=f"Username: {username}\nPassword: {password}")
        else:
            messagebox.showerror(title="Error", message="No such username or password!")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")

# Canvas
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(125, 100, image=logo)
canvas.grid(row=0, column=1, sticky="ew")

# Labels
website_label = Label(text="Website:")
user_label = Label(text="Email/Username:")
password_label = Label(text="Password:")

website_label.grid(row=1, column=0)
user_label.grid(row=2, column=0)
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=34)
website_entry.focus()
user_entry = Entry(width=53)
user_entry.insert(0, "Insert your email here")
password_entry = Entry(width=34)

website_entry.grid(row=1, column=1, columnspan=2, sticky="w")
user_entry.grid(row=2, column=1, columnspan=2)
password_entry.grid(row=3, column=1, sticky="w")

# Button's
search_button = Button(text="Search", command=find_password)
gen_pass_button = Button(text="Generate Password", command=generate_password)
add_pass_button = Button(text="Add", width=45, command=save)

search_button.grid(row=1, column=2, sticky="ew")
gen_pass_button.grid(row=3, column=2, sticky="ew")
add_pass_button.grid(row=4, column=1, columnspan=2)

window.mainloop()