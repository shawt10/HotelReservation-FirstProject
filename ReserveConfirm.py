import customtkinter as ctk
from tkinter import messagebox
import mysql.connector

# MySQL connection setup
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="pypro"
)
cursor = mydb.cursor(dictionary=True)


class Conf:
    def __init__(self, stay_ID, fName, mName, lName, roomNo,date):
        self.stay_ID = stay_ID
        self.fName = fName
        self.mName = mName
        self.lName = lName
        self.roomNo = roomNo
        self.date = date

    def ok(self):
        def show_latest_checkin():
            # Get latest entry by stay_ID (you can modify the field based on your table)


            # Display confirmation window
            window = ctk.CTk()
            window.title("Latest Check-in Confirmation")
            window.geometry("400x300")

            # Create confirmation text
            text = f"""
            ✅ Check-in Confirmed!

            Stay ID   : {self.stay_ID}
            Fullname  : {self.fName} {self.mName} {self.lName}
            Room No   : {self.roomNo}
            Date      : {self.date}
            
            """

            label = ctk.CTkLabel(window, text=text.strip(), justify="left")
            label.pack(padx=20, pady=20)

            ctk.CTkButton(window, text="OK", command=window.destroy).pack(pady=10)

            window.mainloop()

        # Run the function to show the window
        show_latest_checkin()
