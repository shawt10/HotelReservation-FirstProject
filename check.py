import customtkinter as ctk
import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="pypro"
)
cursor = mydb.cursor(dictionary=True)

class checkedInWindow:
    def newCheck(self):

        def fetch_and_display_info(insert_to_db=False):
            text = text_field.get()
            cursor.execute("SELECT * FROM information_desk WHERE stay_ID = %s", (text,))
            result = cursor.fetchall()

            if not result:
                show_message("No matching stay_ID found.")
                return

            receipt_lines = ["======== Reservation Information ========"]
            for row in result:
                stay_id = row['stay_ID']
                fname = row['fName']
                mname = row['mName']
                email = row['email']
                contact = row['contactNo']
                lname = row['lName']
                roomNo = row['roomNo']
                date = row['dateStart']
                receipt_lines.append(f"Stay ID    : {stay_id}")
                receipt_lines.append(f"Reservationist Name: {fname} {mname} {lname}")
                receipt_lines.append(f"Reservationist Email: {email}")
                receipt_lines.append(f"Reservationist Contact: {contact}")
                receipt_lines.append(f"Room No    : {roomNo}")
                receipt_lines.append(f"Check-In   : {date}")

            cursor.execute("SELECT * FROM rooms WHERE room_number = %s", (roomNo,))
            result1 = cursor.fetchall()

            for row in result1:
                price = row['Price']
                roomtype = row['Roomtype']
                receipt_lines.append(f"Room Type  : {roomtype}")
                receipt_lines.append(f"Price      : ${price}")

            if insert_to_db:
                cursor.execute("INSERT INTO checkedin (stay_ID, RoomType, Price, CheckInDate, CheckStatus, RoomNo) VALUES (%s, %s, %s, %s, %s, %s)",
                               (stay_id, roomtype, price, date, "checked ", roomNo))
                mydb.commit()



            receipt_lines.append("=========================")
            display_receipt("\n".join(receipt_lines))

        def display_receipt(receipt_text):
            scrollable_text.configure(state="normal")
            scrollable_text.delete("0.0", "end")
            scrollable_text.insert("0.0", receipt_text)
            scrollable_text.configure(state="disabled")

        def show_message(msg):
            scrollable_text.configure(state="normal")
            scrollable_text.delete("0.0", "end")
            scrollable_text.insert("0.0", msg)
            scrollable_text.configure(state="disabled")

        # Set up portrait-like window
        root = ctk.CTk()
        root.title("Check In")
        root.geometry("350x400")

        # Entry + side button
        entry_frame = ctk.CTkFrame(root)
        entry_frame.pack(pady=10, padx=10, fill="x")

        text_field = ctk.CTkEntry(entry_frame, width=200)
        text_field.pack(side="left", padx=(0, 10), expand=True, fill="x")

        side_button = ctk.CTkButton(entry_frame, text="→", width=30, command=lambda: fetch_and_display_info(insert_to_db=False))
        side_button.pack(side="left")

        # Receipt-style output box
        scrollable_text = ctk.CTkTextbox(root, height=250)
        scrollable_text.pack(pady=10, padx=10, fill="both", expand=True)
        scrollable_text.configure(state="disabled", font=("Courier New", 12), wrap="word")

        # Insert Button to Database
        submit_button = ctk.CTkButton(root, text="Check In", command=lambda: fetch_and_display_info(insert_to_db=True))
        submit_button.pack(pady=15)

        root.mainloop()
