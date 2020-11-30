from tkinter import *
import sqlite3


def LoginPage():

    def dbcon():
        con = sqlite3.connect("test")
        con.execute("CREATE TABLE IF NOT EXISTS testtable(user varchar(50), password varchar(71))")
        con.execute("Insert into testtable values (?, ?)", (username.get(), password.get()))
        con.commit()
        con.close()

    login_screen=Tk()
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter login details").pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Username").pack()
    username = StringVar()
    username_login_entry = Entry(login_screen, textvariable="username")
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password").pack()
    password = StringVar()
    password__login_entry = Entry(login_screen, textvariable="password", show= '*')
    password__login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=dbcon).pack()
    login_screen.mainloop()


LoginPage()
