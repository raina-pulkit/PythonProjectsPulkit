'''
Program that saves password locally for user so they dont have to remember,
also allows for searching password for a given mail and website name
'''

from tkinter import *

FONT = ("Arial", 15, "bold")

# Window making
window = Tk()
window.title("Password Generator")
window.config(bg="white", padx=50, pady=50)
# window.geometry("500x500")

# Adding a canvas
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
canvas.grid(row=0, column=1)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)


# Creating the Labels needed
website = Label(text="Website: ", font=FONT, bg="white", fg="green", width=15)
password = Label(text="Password: ", font=FONT, bg="white", fg="green", width=15)
email = Label(text="Email/UserName: ", font=FONT, bg="white", fg="green", width=15)
website.grid(row=1, column=0)
email.grid(row=2, column=0)
password.grid(row=3, column=0)


# Creating the Entries needed
websiteText = Entry(width=32)
emailText = Entry(width=55)
passwordText = Entry(width=32)
websiteText.grid(row=1, column=1, columnspan=1, sticky=W)
emailText.grid(row=2, column=1, columnspan=2, sticky=W)
passwordText.grid(row=3, column=1, sticky=W)

websiteText.focus()

# Defining functions for the buttons to be added
import pandas as pd
from pathlib import Path
from tkinter import messagebox


def add_data():
    wbs = websiteText.get()
    mail = emailText.get()
    pwd = passwordText.get()

    if not len(wbs) or not len(mail) or not len(pwd):
        messagebox.showwarning(title="WARNING", message="YOU ARE LEAVING FIELDS EMPTY BITCH")
    # We should first ask the user whether they are satisfied with their inputs

    confirm = messagebox.askokcancel(title="Confirm password",
                                     message=f"Details entered\nWebsite: {wbs}\nEmail/Username: {mail}\nPassword: {pwd}")
    if not confirm:
        return

    # Instead of using Path, we can even use try catch exception
    file = Path("CSV_Files/passwords.csv")
    if not file.exists():
        data = {"Website": [], "Email/Username": [], "Password": []}
        data = pd.DataFrame(data)
        data.to_csv("passwords.csv")

    data = pd.read_csv("CSV_Files/passwords.csv")
    data = data.to_dict("list")
    del data[list(data)[0]]
    if (wbs not in data["Website"]) or (wbs in data["Website"] and mail not in data["Email/Username"]):
        data["Website"].append(wbs)
        data["Email/Username"].append(mail)
        data["Password"].append(pwd)
    else:
        for i in range(len(data["Website"])):
            if data["Website"][i] == wbs and data["Email/Username"][i] == mail:
                data["Password"][i] = pwd

    data = pd.DataFrame(data)
    data.to_csv("passwords.csv")
    websiteText.delete(0, END)
    passwordText.delete(0, END)
    emailText.delete(0, END)

    messagebox.showinfo(title="Password Saver", message="PASSWORD ADDED SUCCESSFULLY")


import random
import pyperclip

letters = [chr(i + 65) for i in range(26)]
letters.extend([chr(i + 97) for i in range(26)])
nums = [str(i) for i in range(10)]
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+', '_', '`']


def generate_password():
    nl = random.randint(8, 10)
    nn = random.randint(5, 6)
    ns = random.randint(2, 4)

    res = [random.choice(letters) for _ in range(nl)]
    res.extend([random.choice(nums) for _ in range(nn)])
    res.extend(([random.choice(symbols) for _ in range(ns)]))
    random.shuffle(res)
    res = "".join(res)
    passwordText.delete(0, END)
    passwordText.insert(0, res)
    pyperclip.copy(res)

def search():
    wbs = websiteText.get()
    mail = emailText.get()
    data = pd.read_csv("CSV_Files/passwords.csv")
    data.to_dict("list")

    for i in range(len(data["Website"])):
        if data["Website"][i] == wbs and data["Email/Username"][i] == mail:
            messagebox.showinfo(title="Password Matched", message=f"Password is: {data['Password'][i]}")
            return
    messagebox.showinfo(title="No Match", message=f"No Password found\nfor given credentials")


genPassBtn = Button(text=f"Generate Password\nand Copy", width=16, command=generate_password)
addBtn = Button(text="Add", width=46, command=add_data, borderwidth=5)
searchBtn = Button(text="Search", width=16, command=search)
genPassBtn.grid(row=3, column=2)
addBtn.grid(row=4, column=1, columnspan=2, sticky=W)
searchBtn.grid(row=1, column=2)

window.mainloop()
