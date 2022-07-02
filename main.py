from email import message
from tkinter import *
from tkinter import messagebox
from turtle import title#not a class another module
from random import randint, choice, shuffle
#import pyperclip

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    #Password Generator Project

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letter =[choice(letters) for _ in range(randint(8,10))]
    password_number =[choice(numbers) for _ in range(randint(2,4))]
    password_symbols =[choice(symbols) for _ in range(randint(2,4))]

    password_list = password_letter+password_number+password_symbols
    shuffle(password_list)
    password = ""
    password = "".join(password_list)
    password_entry.insert(0, password)
    #pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website_ = website_entry.get()
    email_ = email_entry.get()
    password_ = password_entry.get()
    if website_ == "" or email_ == "" or password_ == "":
        messagebox.showinfo(title ="alert", message ="Don't leave any field empty")
    else:
        if_ok = messagebox.askokcancel(title = website_, message = f"Email/Username: {email_}\n Password : {password_}\n click 'ok' if its correct")
        if if_ok:
            with open("Password_generator.txt", mode = "a") as file:#mode = "a", add
                file.write((f"\n website : {website_}\n Email/Username: {email_}\n Password : {password_}"))

    website_entry.delete(0, END)
    password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager") 
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100, image = logo_img)
canvas.grid(column=1, row=0)
#Label
website_label = Label(text="Website", font=(FONT_NAME, 15, "bold"))
website_label.grid(column=0, row=1)
website_label.focus()
#Label
email_label = Label(text="Email/Username", font=(FONT_NAME, 15, "bold"))
email_label.grid(column=0, row=2)
#Label
password_label = Label(text="Email/Username", font=(FONT_NAME, 15, "bold"))
password_label.grid(column=0, row=3)
#Entry
website_entry = Entry(width = 35)
website_entry.grid(column=1, row=1,columnspan=2)
#Entry
email_entry = Entry(width = 35)
email_entry.grid(column=1, row=2,columnspan=2)
email_entry.insert(0,"google@gmail.com")
#Entry
password_entry = Entry(width = 21)
password_entry.grid(column=1, row=3,columnspan=2)

#Button
generate_password = Button(text = "Generate Password",command=password_generator, highlightthickness=0)
generate_password.grid(column=2, row=3)

#Button
generate_password = Button(text = "Add",command= save_password, highlightthickness=0, width=36)
generate_password.grid(column=1, row=4)

window.mainloop()