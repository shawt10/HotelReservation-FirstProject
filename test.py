#Dont change This works
from tkinter import messagebox
import customtkinter as ctk
import mysql.connector

class servicers:
    # Fetch data for services
    def services_window(self):
        def get_all_services():
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="",
                database="pypro"
            )
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM servicestable")
            return mycursor.fetchall()

        # Insert service into the database
        def insertService(stay_id, serviceID, price):
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="",
                database="pypro"
            )
            mycursor = mydb.cursor()
            query_id = "SELECT * FROM information_desk WHERE stay_ID = %s"
            mycursor.execute(query_id, (stay_id,))
            result = mycursor.fetchone()

            if result:
                query = "INSERT INTO services (stay_ID, ServiceID, price) VALUES (%s, %s, %s)"
                mycursor.execute(query, (stay_id, serviceID, price))
                mydb.commit()
            else:
                messagebox.showerror("Input Error", "Stay ID not found in the system.")

            mycursor.close()
            mydb.close()

        # Fetch data for Stay ID and Room ID from the Information Desk
        def get_information_desk():
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="",
                database="pypro"
            )
            mycursor = mydb.cursor()
            mycursor.execute("SELECT stay_ID, RoomNo FROM checkedin WHERE CheckStatus = 'checked'")
            return mycursor.fetchall()

        # Function to handle label click for Stay ID
        def on_label_click(stay_id):
            # Set the clicked Stay ID to the text field
            entry.delete(0, "end")
            entry.insert(0, stay_id)

        # Main application setup
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        app = ctk.CTk()
        app.geometry("1000x540")
        app.title("Hotel Services")

        # Entry at the top for Stay ID
        entry = ctk.CTkEntry(app, placeholder_text="Enter Stay ID here", width=780)
        entry.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")

        # Fixed-size scrollable frame for services
        table_height = 350
        scrollable_frame = ctk.CTkScrollableFrame(app, width=780, height=table_height)
        scrollable_frame.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        # Column widths for services table
        column_widths = [30, 60, 150, 350, 100, 120]
        headers = ["", "Service ID", "Service Name", "Description", "Price", "Availability"]

        # Create headers for the services table
        for col, header in enumerate(headers):
            label = ctk.CTkLabel(scrollable_frame, text=header, font=("Arial", 14, "bold"),
                                 anchor="w", width=column_widths[col])
            label.grid(row=0, column=col, padx=5, pady=5, sticky="w")
            scrollable_frame.grid_columnconfigure(col, weight=column_widths[col])

        # Get and display services data
        services = get_all_services()
        checkboxes = []

        for row, service in enumerate(services, start=1):
            var = ctk.BooleanVar()
            checkbox = ctk.CTkCheckBox(scrollable_frame, variable=var, text="")
            checkbox.grid(row=row, column=0, padx=5, pady=2, sticky="w")
            checkboxes.append(var)

            for col, item in enumerate(service, start=1):
                text = str(item) if item is not None else ""
                wraplength = column_widths[col] - 10
                label = ctk.CTkLabel(scrollable_frame, text=text, font=("Arial", 12),
                                     anchor="w", wraplength=wraplength,
                                     width=column_widths[col])
                label.grid(row=row, column=col, padx=5, pady=2, sticky="w")

        # Function to show selected services
        def show_selected():
            stay_id = entry.get().strip()
            if not stay_id:
                messagebox.showerror("Input Error", "Please enter a Stay ID.")
                return

            selected = [services[i] for i, var in enumerate(checkboxes) if var.get()]
            if not selected:
                messagebox.showwarning("No Selection", "Please select at least one service.")
                return

            for service in selected:
                serviceID = service[0]  # Assuming ServiceID is column 0
                price = service[3]      # Assuming Price is column 4
                insertService(stay_id, serviceID, price)

        # Button to show selected services
        btn = ctk.CTkButton(app, text="Enter", command=show_selected)
        btn.grid(row=2, column=0, pady=10)
        app.grid_columnconfigure(0, weight=1)
        btn.grid_configure(sticky="n")

        # Right-side area for Information Desk with Stay ID and Room No.
        info_desk_scrollable_frame = ctk.CTkScrollableFrame(app, width=200, height=400)
        info_desk_scrollable_frame.grid(row=1, column=1, padx=10, pady=10, sticky="n")

        app.grid_columnconfigure(1, weight=0)

        info_desk_column_widths = [90, 90]
        info_desk_headers = ["Stay ID", "Room No."]

        # Create headers for the information desk table
        for col, header in enumerate(info_desk_headers):
            label = ctk.CTkLabel(info_desk_scrollable_frame, text=header, font=("Arial", 14, "bold"),
                                 anchor="w", width=info_desk_column_widths[col])
            label.grid(row=0, column=col, padx=5, pady=5, sticky="w")
            info_desk_scrollable_frame.grid_columnconfigure(col, weight=info_desk_column_widths[col])

        # Get and display information desk data
        info_desk_data = get_information_desk()

        for row, desk_info in enumerate(info_desk_data, start=1):
            for col, item in enumerate(desk_info):
                text = str(item) if item is not None else ""
                wraplength = info_desk_column_widths[col] - 10
                label = ctk.CTkLabel(info_desk_scrollable_frame, text=text, font=("Arial", 12),
                                     anchor="w", wraplength=wraplength,
                                     width=info_desk_column_widths[col], fg_color="transparent")
                label.grid(row=row, column=col, padx=5, pady=2, sticky="w")

                if col == 0:  # If it's the Stay ID column, bind click event
                    label.bind("<Button-1>", lambda e, stay_id=text: on_label_click(stay_id))

        # Start the application
        app.mainloop()
