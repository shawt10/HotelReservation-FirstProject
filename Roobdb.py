import mysql.connector
# from RandomOOP import OPFUN



#DB CONNECTION CODE
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="pypro"
)
#Ani pag OOP HAHAHAHAHA
# FOR GETTING THE ROOM TYPE AND AVAILABLE ROOMS ON THE HOTEL
class Roomres:
    def __init__(self, roomtype, ciDate, coDate):
        self.roomtype = roomtype
        self.ciDate = ciDate
        self.coDate = coDate
        self.avail = "Available"

    def get_Avroom(self):
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM rooms WHERE Roomtype = %s AND status = %s", (self.roomtype, self.avail))
        s = mycursor.fetchall()
        return s

class reserveRoom:
    def __init__(self,StayID,Fname, Mname, Lname, Cnum, Email, GuestAdd, Child, Adults, RoomNo, dateStart, dateEnd):
        self.Fname = Fname
        self.Mname = Mname
        self.Lname = Lname
        self.Cnum = Cnum
        self.Email = Email
        self.GuestAdd = GuestAdd
        self.Child = Child
        self.Adults = Adults
        self.RoomNo = RoomNo
        self.dateStart = dateStart
        self.dateEnd = dateEnd
        self.stayID = StayID


        # try catch method ni siya to insert and data didto sa sql
        try:
            mycursor = mydb.cursor()

            sql = """INSERT INTO information_desk 
                     (stay_ID, fName, mName, lName, email, contactNo, address, child, adult, roomNo, dateStart, dateOut) 
                     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""   #String form of the sql command

            values = (
                self.stayID, self.Fname, self.Mname, self.Lname,
                self.Email, self.Cnum, self.GuestAdd,
                self.Child, self.Adults, self.RoomNo,
                self.dateStart, self.dateEnd
            )       #Values of the supposed db table

            mycursor.execute(sql, values)
            mydb.commit()  # Save changes to the database
            print("Data inserted successfully")

        except mysql.connector.Error as err:
            print("Error:", err)

        finally:
            mycursor.close()


# class ServiceData:
#     @classmethod
#     def get_all_services(cls):
#         mycursor = mydb.cursor()
#         mycursor.execute("SELECT * FROM servicetable")
#         return mycursor.fetchall()







