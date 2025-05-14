import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="pypro"
)


username = input("Enter Username: ")
password = input("Enter Password: ")

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM ad_login WHERE user =%s AND password =%s", (username, password))
myresult = mycursor.fetchone()

if myresult:
    print("Login Successful:", myresult)
else:
    print("Invalid username or password.")

mydb.close()




