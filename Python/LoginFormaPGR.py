#
from tkinter import *
import tkinter.font
import mysql.connector
from functools import partial
from GUI import *

root = Tk()  # sukuriamas pagrindinis langas

root.title('Prisijungimas')


mydb = mysql.connector.connect(
  host="localhost",
  user="admin",
  passwd="laukas12",
    database="BLE"
)

cursor = mydb.cursor()

def validateLogin(username, password):  # cia patikrinti su duomenu baze
    PJ = " "
    SL = []
    cursor = mydb.cursor()
    PJ = username.get()  # PJ = prisijungimas
    print("username entered :", PJ)
    cursor.execute("SELECT Slaptazodis FROM AdminPrisijungimas WHERE Prisijungimas = %s", (PJ,))
    myresult = str(cursor.fetchone())
    SL.append(re.sub(r"[\,'(\)]",'',myresult))   # SL = slaptazodis
    if( SL[0] == password.get()):
        root.destroy()
        main()
    else :
        Label(root,fg = "red", text = " Netinka prisijungimas arba slaptazodis").grid(row=6, column=1)
    return

#username label and text entry box
usernameLabel = Label(root, text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(root, textvariable=username).grid(row=0, column=1)

#password label and password entry box
passwordLabel = Label(root, text="Password").grid(row=1, column=0)
password = StringVar()
passwordEntry = Entry(root, textvariable=password, show='*').grid(row=1, column=1)


validateLogin = partial(validateLogin, username, password)

#login button
loginButton = Button(root, text="Login", command=validateLogin).grid(row=5, column=0)

root.mainloop()