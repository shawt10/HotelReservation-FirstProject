import tkinter as tk
from tkinter import Label, messagebox
from dbhelper import Auth    #AUTH DB LOGIN FUNC HERE
import mysql.connector
from screts import newWindow
import customtkinter as ctk
from AnotherTest import mainFile


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="pypro"
)


def submit():
    user = username.get()
    passw = password.get()

    AUTH = Auth(mydb, user, passw)

    if user == "" and passw == "":
        messagebox.showwarning("showwarning", "Please enter both username and password")

    elif AUTH.login():
        app.destroy()
        #window = tk.Tk()
        obj = mainFile()
        obj.newFile()

    else:
        messagebox.showwarning("showwarning", "Wrong username or password")





ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("User Login")
app.geometry("400x400")
app.resizable(False, False)

# Frame code ni
frame = ctk.CTkFrame(app, width=300, height=250, corner_radius=15)
frame.place(relx=0.5, rely=0.5, anchor="center")

# Title Label
title_label = ctk.CTkLabel(frame, text="Hotel Room Reservation and Services", font=("Arial", 16, "bold"))
title_label.pack(pady=(20, 10))

# Username Entry
username = ctk.CTkEntry(frame, width=250, placeholder_text="Username")
username.pack(pady=5)

# Password Entry
password = ctk.CTkEntry(frame, width=250, placeholder_text="Password", show="*")
password.pack(pady=5)

# Login Button
login_button = ctk.CTkButton(frame, text="Login", width=250, command=submit)
login_button.pack(pady=10)


# Run App
app.mainloop()