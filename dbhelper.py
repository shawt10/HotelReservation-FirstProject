class Auth:

    #Code for the authentication login for the cooks and shit


    def __init__(self, mydb, username, password):
        self.mydb = mydb
        self.username = username
        self.password = password

    def login(self):
        mycursor = self.mydb.cursor()
        mycursor.execute("SELECT * FROM ad_login WHERE user = %s AND password = %s", (self.username, self.password))
        myresult = mycursor.fetchone()
        return True if myresult else False
