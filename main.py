from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_pass():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)


    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    # pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email_username = email_username_entry.get()
    password = password_entry.get()

    new_dic = {
        website: {
            "email" : email_username,
            "password" : password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Ooops", message="Please ensure that you have no empty fields.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details filled: \n Email:{email_username}"
                                                            f"\n Password: {password} \n Is it OK to save?")
        if is_ok:
            try:
                with open("data.json", mode="r") as passfile:
                    # read old data
                    data = json.load(passfile)
            except FileNotFoundError:
                with open("data.json", mode="w") as passfile:
                    json.dump(new_dic, passfile, indent=4)
            else:
                # updating old data with new data
                data.update(new_dic)

                with open("data.json", mode="w") as passfile:
                    # saving updated data
                    json.dump(data, passfile, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# -----------------------------SEARCH FUNCTIONALITY -------------------#

def find_password():
    website = website_entry.get()

    try:

        with open("data.json", mode="r") as passfile:
            data = json.load(passfile)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No such file Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Emmail: {email} \n Password: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No Details for this {website} exists!!!")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("My Pass Manager")
window.config(padx=50, pady=20)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website :")
website_label.grid(column=0, row=1)

website_entry = Entry(width=18)
website_entry.focus()
website_entry.grid(column=1, row=1)

search_btn = Button(text="Search", width=18, command=find_password)
search_btn.grid(column=2, row=1)

email_username = Label(text="Email / Username :")
email_username.grid(column=0, row=2)

email_username_entry = Entry(width=40)
email_username_entry.insert(0, "tersly@gmail.com")
email_username_entry.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password :")
password_label.grid(column=0, row=3)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky='E')

password_gen_pass = Button(text="Generate Password", command=generate_pass)
password_gen_pass.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)







window.mainloop()