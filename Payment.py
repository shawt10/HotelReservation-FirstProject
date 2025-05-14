import customtkinter as ctk
from tkinter import messagebox
from PIL import Image
from datetime import date
import mysql.connector

mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="pypro"
    )
cursor = mydb.cursor(dictionary=True)


class paymentClass:
    def newPayment(self):

        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        app = ctk.CTk()
        app.title("Payment Panel")
        app.geometry("700x500")

        selected_method = ctk.StringVar(value="")

        def select_payment(method):
            selected_method.set(method)
            update_receipt()
            chosen_method = method

        def process_payment():
            total = 0
            stay_id = entry_stay_id.get()
            global chosen_method

            # Get checked-in details for the stay
            cursor.execute("SELECT * FROM checkedin WHERE stay_ID = %s", (stay_id,))
            result = cursor.fetchone()
            cursor.nextset()
            if result is None:
                messagebox.showerror("Error", f"{stay_id} Reference/ Room is not Found on the system, Please check the Reference/ Room if it's correct")
            else:
                # Query prices from services and checkedin table
                cursor.execute("""
                    SELECT Price FROM services WHERE Stay_ID = %s
                    UNION
                    SELECT Price FROM checkedin WHERE Stay_ID = %s
                """, (stay_id, stay_id))

                prices = cursor.fetchall()

                for row in prices:
                    price_str = row['Price']
                    price_value = float(price_str.replace('%', '').strip())  # Clean and convert to float
                    total += price_value

                print(f"Total: {total}")

                # Update payment status in information_desk
                cursor.execute("UPDATE information_desk SET paymentStatus = %s WHERE stay_ID = %s", ('PAID', stay_id))
                mydb.commit()

                try:
                    cursor.execute("INSERT INTO payment (TotalPaid, stay_ID, mop) VALUES (%s, %s, %s)",
                                   (total, stay_id, chosen_method))
                    connection.commit()  # Don't forget to commit the changes
                    messagebox.showinfo("Success", "Payment recorded successfully.")
                except Exception as e:
                    messagebox.showerror("Database Error", f"Failed to record payment:\n{e}")



            method = selected_method.get()
            update_receipt()
            app.destroy()

        def update_receipt():
            method = selected_method.get()
            stay_id = entry_stay_id.get()
            total = 0
            cursor.execute("""
                        SELECT Price FROM services WHERE Stay_ID = %s
                        UNION
                        SELECT Price FROM checkedin WHERE Stay_ID = %s
                    """, (stay_id, stay_id))

            prices = cursor.fetchall()

            for row in prices:
                price_str = row['Price']
                price_value = float(price_str.replace('%', '').strip())  # Clean and convert to float
                total += price_value
                cursor.nextset()

            cursor.execute("UPDATE checkedin SET CheckStatus = %s WHERE stay_ID = %s", ('out', stay_id))
            cursor.nextset()



            cursor.execute("SELECT * FROM checkedin WHERE stay_ID = %s", (stay_id,))
            result1 = cursor.fetchone()
            cursor.nextset()
            cursor.execute("SELECT * FROM services WHERE stay_ID = %s", (stay_id,))
            result2 = cursor.fetchall()
            cursor.nextset()
            cursor.execute("SELECT * FROM information_desk WHERE stay_ID = %s", (stay_id,))
            result3 = cursor.fetchone()
            cursor.nextset()
            # Extracting the necessary data from the fetched results
            fname = result3['fName']
            mname = result3['mName']
            lname = result3['lName']
            chekinData = result1['CheckInDate']
            roomtype = result1['RoomType']
            today = date.today()

            # Fetch service details
            service_lines = []
            for row in result2:
                cursor.execute("SELECT * FROM servicestable WHERE ServiceID = %s", (row['ServiceID'],))
                result4 = cursor.fetchall()
                for service_row in result4:
                    service_name = service_row['Sevice_Name']
                    price = service_row['Price']
                    service_lines.append(f"{service_name:<35}: ${price}")

            # Format the receipt text
            receipt_text = f"""\
            *** Ram Hotel and Services Receipt ***
            ----------------------------------------
            Stay ID       : {stay_id}
            Payment Method: {method}
            Guest Name    : {fname} {mname} {lname}
            Check-in Date : {chekinData}
            Check-out Date: {today}
            Room Type     : {roomtype}

            Charges:
            ----------------------------------------
            {'\n'.join(service_lines)}

            ----------------------------------------
            TOTAL AMOUNT                 : ${total}

            ----------------------------------------
            Thank you for choosing our hotel!
            Visit us again. Have a pleasant day!
            ----------------------------------------
            Generated on: {today}
            """

            # Display the receipt in the Textbox
            receipt_box.configure(state="normal")
            receipt_box.delete("1.0", "end")
            receipt_box.insert("1.0", receipt_text.strip())
            receipt_box.configure(state="disabled")


        # Layout setup
        main_frame = ctk.CTkFrame(app)
        main_frame.pack(padx=10, pady=10, fill="both", expand=True)

        left_frame = ctk.CTkFrame(main_frame)
        left_frame.pack(side="left", padx=10, pady=10, fill="y")

        right_frame = ctk.CTkFrame(main_frame)
        right_frame.pack(side="right", padx=10, pady=10, fill="both", expand=True)

        # Stay ID Entry
        ctk.CTkLabel(left_frame, text="Stay/Room ID:").pack(pady=(10, 0))
        entry_stay_id = ctk.CTkEntry(left_frame, width=200)
        entry_stay_id.pack(pady=(0, 20))

        # Load Images
        def load_img(file):
            return ctk.CTkImage(Image.open(file), size=(60, 60))

        img_paypal = ctk.CTkImage(Image.open(r"paypal.png"), size=(60, 60))
        img_mastercard = load_img(r"mastercard.png")
        img_cash = load_img("cash.png")
        img_gcash = load_img("gcash.png")

        # 2x2 Grid of Buttons
        grid_frame = ctk.CTkFrame(left_frame)
        grid_frame.pack()

        buttons = [
            ("PayPal", img_paypal),
            ("Mastercard", img_mastercard),
            ("Cash", img_cash),
            ("GCash", img_gcash),
        ]

        for idx, (name, img) in enumerate(buttons):
            r, c = divmod(idx, 2)
            # btn = ctk.CTkButton(grid_frame, text=name, image=img, compound="left", width=150,
            #                     command=lambda m=name: select_payment(m)) WITH IMAGE YAWA
            btn = ctk.CTkButton(grid_frame, text=name, compound="left", width=150,
                                                     command=lambda m=name: select_payment(m))
            btn.grid(row=r, column=c, padx=5, pady=5)

        # Pay Button
        ctk.CTkButton(left_frame, text="Pay Now", width=200, command=process_payment).pack(pady=20)

        # Receipt Viewer
        ctk.CTkLabel(right_frame, text="Receipt Preview").pack(anchor="w", padx=5, pady=5)

        receipt_box = ctk.CTkTextbox(right_frame, state="disabled", width=320, height=360, wrap="word")
        receipt_box.pack(fill="both", expand=True, padx=5, pady=(0, 10))

        scrollbar = ctk.CTkScrollbar(right_frame, command=receipt_box.yview)
        scrollbar.pack(side="right", fill="y")
        receipt_box.configure(yscrollcommand=scrollbar.set)

        app.mainloop()


