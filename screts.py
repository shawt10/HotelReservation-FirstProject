from datetime import datetime, timedelta
from tkinter import messagebox

from tkcalendar import DateEntry
import customtkinter as ctk
from Roobdb import Roomres, reserveRoom
from RandomOOP import OPFUN
from ReserveConfirm import Conf


class newWindow:
    @staticmethod
    def new():

        #def unreserve():



        def checkRoom():
            # Getting datas from the user input
            roomTY = roomtype.get()
            checkin = checkinDate.get()
            checkout = checkoutDate.get()
            room = Roomres(roomTY, checkin, checkout)
            results = room.get_Avroom()
            #Creating format for the returned value
            formatted_results = "\n".join([f"Room Number: {row[2]}, Type: {row[4]}, Price ${row[5]}" for row in results])

            result_Box(formatted_results)


        #Changing the results on the box
        def result_Box(Results):
            result_box.configure(state='normal')
            result_box.delete("1.0", "end")
            result_box.insert("1.0", Results)
            result_box.configure(state='disabled')

            #Entering information to database

        def personal_Info_Entry():

            days_of_stay = num_days.get()
            current_datetime = datetime.now()
            formatted_date = current_datetime.strftime("%Y-%m-%d")

            tomorrow = datetime.now() + timedelta(days=int(days_of_stay))
            formatted_tomorrow = tomorrow.strftime("%Y-%m-%d")

            opfunc = OPFUN()  # Create an instance
            Recit = opfunc.generate_custom_id()  # Getting the custom ID or sting of characters

            firstname = first_name.get()
            middlename = middle_name.get()
            lastname = last_name.get()
            Email = email.get()
            contactNumber = contact_number.get()
            addy = guest_address.get()
            child = num_children.get()
            adults = num_adults.get()
            roomNo = room_number.get()
            dateStart = start_date.get()
            dateEnd = formatted_tomorrow

            #
            reserve = reserveRoom(Recit, firstname, middlename, lastname,contactNumber,Email,addy,child,adults,roomNo,dateStart,dateEnd)
            messagebox.showinfo("Info", f"Reservation completed successfully! {Recit}")
            conf_instance = Conf(Recit,firstname,middlename,lastname,roomNo,dateStart)
            conf_instance.ok()

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")



        roots = ctk.CTk()
        roots.title("Reservation Panel")
        roots.geometry("1000x500")
        roots.resizable(False, False)

        # THE BIG BLACK FRAME
        outer_frame = ctk.CTkFrame(roots, width=850, height=400, corner_radius=15, fg_color="black")
        outer_frame.place(relx=0.7, rely=0.58, anchor="e")

        # LABEL FUNC
        def create_section_label(parent, text):
            label = ctk.CTkLabel(parent, text=text, font=("Arial", 16, "bold"))
            label.pack(pady=(10, 5))

        # Personal Info
        create_section_label(outer_frame, "Personal Information")
        personal_frame = ctk.CTkFrame(outer_frame, fg_color="transparent")
        personal_frame.pack(pady=5)

        first_name = ctk.CTkEntry(personal_frame, placeholder_text="First Name *", width=200)
        middle_name = ctk.CTkEntry(personal_frame, placeholder_text="Middle Name", width=200)
        last_name = ctk.CTkEntry(personal_frame, placeholder_text="Last Name *", width=200)

        first_name.grid(row=0, column=0, padx=10, pady=5)
        middle_name.grid(row=0, column=1, padx=10, pady=5)
        last_name.grid(row=0, column=2, padx=10, pady=5)

        # Contact Information Data
        create_section_label(outer_frame, "Contact Information")
        contact_frame = ctk.CTkFrame(outer_frame, fg_color="transparent")
        contact_frame.pack(pady=5)

        contact_number = ctk.CTkEntry(contact_frame, placeholder_text="Contact Number *", width=200)
        email = ctk.CTkEntry(contact_frame, placeholder_text="Email *", width=200)
        guest_address = ctk.CTkEntry(contact_frame, placeholder_text="Guest's Address *", width=200)

        contact_number.grid(row=0, column=0, padx=10, pady=5)
        email.grid(row=0, column=1, padx=10, pady=5)
        guest_address.grid(row=0, column=2, padx=10, pady=5)

        # Change some of this to date picker probably or add something
        create_section_label(outer_frame, "Reservation Information")
        reservation_frame = ctk.CTkFrame(outer_frame, fg_color="transparent")
        reservation_frame.pack(pady=5)

        num_children = ctk.CTkEntry(reservation_frame, placeholder_text="Number of Children *", width=200)
        num_adults = ctk.CTkEntry(reservation_frame, placeholder_text="Number of Adults *", width=200)
        num_days = ctk.CTkEntry(reservation_frame, placeholder_text="Number of Days of Stay *", width=200)  # Could  be number of rooms to stay in shits

        date_label = ctk.CTkLabel(reservation_frame, text="Start Date:")
        date_label.grid(row=1, column=0, padx=10, pady=5)

        start_date = DateEntry(reservation_frame, width=18, background='darkblue', foreground='white', borderwidth=2, date_pattern='yyyy-MM-dd')
        start_date.grid(row=1, column=1, padx=10, pady=5)


        num_children.grid(row=0, column=0, padx=10, pady=5)
        num_adults.grid(row=0, column=1, padx=10, pady=5)
        num_days.grid(row=0, column=2, padx=10, pady=5)

        # Room and btns
        room_frame = ctk.CTkFrame(outer_frame, fg_color="transparent")
        room_frame.pack(pady=10)

        room_number = ctk.CTkEntry(room_frame, placeholder_text="Enter Room Number *", width=200)
        reserve_btn = ctk.CTkButton(room_frame, text="Reserve", width=100,command=personal_Info_Entry)


        room_number.grid(row=0, column=0, padx=10)
        reserve_btn.grid(row=0, column=1, padx=5)


        # Outer Frame Left side tung naay personal informations sa users
        filter_frame = ctk.CTkFrame(roots, width=250, height=400, corner_radius=15, fg_color="black")
        filter_frame.place(relx=0.98, rely=0.5, anchor="e") # Positioned to the left

        # Label sa title
        title_label = ctk.CTkLabel(filter_frame, text="Filter", font=("Arial", 16, "bold"))
        title_label.pack(pady=(10, 5))


        # How to create combobox tutorial 101 python so good and great
        def create_filter_option(parent, label_text, values=None, is_date=False):
            frame = ctk.CTkFrame(parent, fg_color="transparent")
            frame.pack(fill="x", padx=10, pady=5)

            label = ctk.CTkLabel(frame, text=label_text, anchor="w")
            label.pack(side="left", padx=(5, 10))

            if is_date:
                # Same sa else but with the date
                date_entry = DateEntry(frame, width=15, background="gray", foreground="black", borderwidth=2)
                date_entry.pack(side="right")
                return date_entry
            else:
                # Para ma kuha ang data na naa sa Sulod sa dropdown option
                combo = ctk.CTkComboBox(frame, values=values, width=120)
                combo.pack(side="right")
                return combo


        # Filters with different dropdown options, Naa pani need I polish like Date pickers and shits to database
        roomtype = create_filter_option(filter_frame, "Room Type :", ["please select...", "Single", "Deluxe", "Suite", "Double"])
        bedconf = create_filter_option(filter_frame, "Additional Bed :", ["please select...", "Yes", "No"])
        checkinDate = create_filter_option(filter_frame, "Check In Date :", is_date=True)
        checkoutDate = create_filter_option(filter_frame, "Check Out Date :", is_date=True)



        # Basta Button ni siya diri na part
        find_button = ctk.CTkButton(filter_frame, text="Find Rooms", width=200, command=checkRoom)
        find_button.pack(pady=10)

                #For result display lang ni siya
        result_box = ctk.CTkTextbox(filter_frame, width=220, height=120)
        result_box.pack(pady=10)
        result_box.insert("1.0", "Rooms of Your Choice will appear Here\nonce you apply filter")
        result_box.configure(state="disabled")  # Read only na option


        roots.mainloop()










