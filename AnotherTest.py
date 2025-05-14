import mysql.connector
from PIL import Image, ImageTk
import customtkinter as ctk
from screts import newWindow
from test import servicers
from Payment import paymentClass
from check import checkedInWindow


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="pypro"
)
cursor = mydb.cursor(dictionary=True)

class mainFile:
    def newFile(self):


        def submit():
            obj = newWindow()
            obj.new()


        def servs():
            servi = servicers()
            servi.services_window()

        def checkthis():
            c1 = checkedInWindow()
            c1.newCheck()




        def destroyer():
            app.destroy()

        def paynow():
            payment = paymentClass()
            payment.newPayment()



        # Fetch data from the database
        def roomData():
            query = "SELECT * FROM rooms"
            cursor.execute(query)
            roomsData = cursor.fetchall()
            return roomsData
            cursor.nextset()


        def refresh_room_cards(frame, floor_number):
            for widget in frame.winfo_children():
                widget.destroy()
            add_room_cards(frame, floor_number)


        def add_room_cards(frame, floor_number):
            room_data = roomData()  # Fetch room data from the database

            canvas = ctk.CTkCanvas(frame, width=1000, height=500, bg="gray17", highlightthickness=0)
            canvas.propagate(False)

            scrollbar = ctk.CTkScrollbar(frame, orientation="vertical", command=canvas.yview)
            scrollable_frame = ctk.CTkFrame(canvas, fg_color="gray20")

            scrollable_frame.bind(
                "<Configure>",
                lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
            )
            canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
            canvas.configure(yscrollcommand=scrollbar.set)

            canvas.pack(side="left", fill="both", expand=True)
            scrollbar.pack(side="right", fill="y")

            # Configure grid column weights for 4 columns
            for col in range(4):
                scrollable_frame.grid_columnconfigure(col, weight=1)

            def on_room_click(room_id):
                cursor = mydb.cursor(dictionary=True)
                cursor.execute("SELECT status FROM rooms WHERE room_number = %s", (room_id,))
                result = cursor.fetchone()
                cursor.nextset()

                if result:
                    status = result['status'].lower()
                    if status == 'available':
                        # paynow()
                        try:
                            cursor = mydb.cursor(dictionary=True)
                            cursor.execute("UPDATE rooms SET status = %s WHERE room_number = %s", ('Occupied', int(room_id)))
                            mydb.commit()
                            print("Room status updated successfully.")
                            cursor.nextset()
                        except Exception as e:
                            print("Error:", e)
                        finally:
                            cursor.close()
                    elif status == 'occupied':  # need this code to update

                        # checkthis()

                        try:
                            cursor = mydb.cursor(dictionary=True)
                            cursor.execute("UPDATE rooms SET status = %s WHERE room_number = %s", ('Available', int(room_id)))
                            mydb.commit()
                            print("Room status updated successfully.")
                            cursor.nextset()
                        except Exception as e:
                            print("Error:", e)
                        finally:
                            cursor.close()
                    else:
                        print(f"Room {room_id} has unknown status: {status}")
                else:
                    print(f"No room found with room number: {room_id}")

                for i, floor in enumerate(floors):
                    refresh_room_cards(tabview.tab(floor), i + 1)

            row_index = 0
            # Create room cards based on the fetched data
            for room in room_data:
                if room['floor_number'] != floor_number:
                    continue

                room_status = room['status'].lower()
                room_number = room['room_number']

                # decide color
                if room_status == "occupied":
                    button_color = "gray"

                else:
                    button_color = "black"

                cursor.execute("Select stay_ID FROM checkedin WHERE RoomNo = %s and CheckStatus = %s ",
                               (room_number, "checked"))
                res = cursor.fetchall()

                # create the button
                room_button = ctk.CTkButton(
                    scrollable_frame,
                    text=f"Room {room_number} - {room_status.capitalize()} \n {res}",
                    fg_color=button_color,
                    text_color="white",
                    width=210,
                    height=140,
                    corner_radius=10,
                    command=lambda rn=room_number: on_room_click(rn)
                )
                room_button.grid(row=row_index // 5, column=row_index % 5, padx=10, pady=10)
                row_index += 1
                cursor.nextset()


        # Create the main app window
        app = ctk.CTk()
        app.geometry("1600x800+0+0")
        app.grid_rowconfigure(0, weight=1)
        app.grid_columnconfigure(0, weight=1)
        app.title("Room Management")

        # ==== FLOOR TABS ====
        tabview = ctk.CTkTabview(app, width=1000, height=500)  # Smaller width for the tabview
        tabview.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        # Example Floors
        floors = ["Floor 1", "Floor 2", "Floor 3"]
        for floor in floors:
            tabview.add(floor)

        # Add rooms to each floor based on fetched data
        for index, floor_name in enumerate(floors, start=1):
            add_room_cards(tabview.tab(floor_name), floor_number=index)

        # ==== ADD A RIGHT FRAME WITH COMPANY NAME AND 4 BUTTONS ====
        right_frame = ctk.CTkFrame(app, width=300, height=800, fg_color="gray15")
        right_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        # Company Name Label
        company_label = ctk.CTkLabel(right_frame, text="Ram Hotel Reservation", font=("Arial", 20, "bold"), text_color="white")
        company_label.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # ==== Add an image to the frame ====
        img_path = "asdasd.png"  # Replace with your image path
        image = Image.open(img_path)
        image = image.resize((300, 300))  # Resize the image to fit in the frame
        photo = ImageTk.PhotoImage(image)

        image_label = ctk.CTkLabel(right_frame, image=photo, text="")  # No text for the image
        image_label.image = photo  # Keep reference to avoid garbage collection
        image_label.grid(row=1, column=0, padx=10, pady=10, sticky="nsew", columnspan=2,
                         rowspan=2)  # Make it fill the right frame

        # Create buttons in 2x2 grid inside right_frame, aligned at the bottom
        reservbtn = ctk.CTkButton(right_frame, text="Reserve a Room", width=120, height=60, command=submit)
        reservbtn.grid(row=3, column=0, padx=10, pady=10, sticky="s")

        button2 = ctk.CTkButton(right_frame, text="Check In", width=120, height=60, command=checkthis)
        button2.grid(row=3, column=1, padx=10, pady=10, sticky="s")

        servBtn = ctk.CTkButton(right_frame, text="Services", width=120, height=60, command=servs)
        servBtn.grid(row=4, column=0, padx=10, pady=10, sticky="s")

        button4 = ctk.CTkButton(right_frame, text="Payment", width=120, height=60, command=paynow)
        button4.grid(row=4, column=1, padx=10, pady=10, sticky="s")

        # Created by label at the bottom right
        created_by_label = ctk.CTkLabel(app, text="Created by USSSSSSSSSSS", font=("Arial", 14), text_color="white")
        created_by_label.grid(row=1, column=1, padx=20, pady=20, sticky="se")

        # ==== LOGOUT BUTTON ====
        logout_btn = ctk.CTkButton(right_frame, text="Logout", width=120, height=40, command=destroyer)
        logout_btn.grid(row=5, column=0, columnspan=2, padx=10, pady=20, sticky="s")

        app.mainloop()
