from pathlib import Path
import ttkbootstrap as ttk
from tkinter import *
import pandas as pd
from pandastable import Table
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import pymysql
from config import host, user, password, db_name



class Welcom(ttk.Window):
    def __init__(self):
        super().__init__()

        self.geometry("600x400")

        def registration():
            rg = Registration()
            self.destroy

        def signIn():
            rg = SignIn()
            self.destroy

        title = ttk.Label(self, text="Добро Пожаловать!\n Выберите действие:")
        btn1=ttk.Button(self, text="Зарегистрироваться", command=registration)
        btn2=ttk.Button(self, text="Войти", command=signIn)

        title.pack(pady=30)
        btn1.pack(pady=10)
        btn2.pack(pady=10)
        self.resizable(False, False)
        self.mainloop()


class Registration(ttk.Window):
    def __init__(self):
        super().__init__()

        self.geometry("600x400")

        def insert_user():
            login=text_box_login.get()
            pwd=text_box_pwd.get()
        # insert data  - добавление данный в таблицу
            with connection.cursor() as cursor:
                insert_querry=f"INSERT INTO `user`(login, pwd) VALUES ('{login}','{pwd}')"
                cursor.execute(insert_querry)
                connection.commit()
            mw=MainWindow()

        frame = ttk.Frame(self)
        frame.pack(pady=50)
        title = ttk.Label(frame, text="Регистрация")
        label_registration = ttk.Label(frame, text="Логин")
        text_box_login = ttk.Entry(frame)
        label_pwd = ttk.Label(frame, text="Пароль")
        text_box_pwd = ttk.Entry(frame)

        btn1=ttk.Button(frame, text="Закрыть", command=self.destroy)
        btn2=ttk.Button(frame, text="Войти", command=insert_user)

        title.grid(column=3, row=1)
        label_registration.grid(column=3, row=3)
        text_box_login.grid(column=3, row=5)
        label_pwd.grid(column=3, row=7)
        text_box_pwd.grid(column=3, row=9)
        btn1.grid(column=1, row=11)
        btn2.grid(column=5, row=11)

        self.resizable(False, False)
        self.mainloop()


class SignIn(ttk.Window):
    def __init__(self):
        super().__init__()

        self.geometry("600x400")

        def signIn():
            try:
                login=text_box_login.get()
                pwd=text_box_pwd.get()
                #select data - выборка данных из таблицы
                with connection.cursor() as cursor:
                    select_all_rows="select * from `user`"
                    cursor.execute(select_all_rows)
                    rows = cursor.fetchall()
                    for row in rows:
                        if row['login']==login and row['pwd']==pwd:  
                            mw=MainWindow()
                        else:
                            title.config(text="не правильный логин или пароль")
            except:
                title.config(text="что-то пошло не так:(")


        frame = ttk.Frame(self)
        frame.pack(pady=50)
        title = ttk.Label(frame, text="Вход")
        label_registration = ttk.Label(frame, text="Логин")
        text_box_login = ttk.Entry(frame)
        label_pwd = ttk.Label(frame, text="Пароль")
        text_box_pwd = ttk.Entry(frame)
        btn1=ttk.Button(frame, text="Закрыть", command=self.destroy)
        btn2=ttk.Button(frame, text="Войти", command=signIn)

        title.grid(column=3, row=1)
        label_registration.grid(column=3, row=3)
        text_box_login.grid(column=3, row=5)
        label_pwd.grid(column=3, row=7)
        text_box_pwd.grid(column=3, row=9)
        btn1.grid(column=1, row=11)
        btn2.grid(column=5, row=11)

        self.resizable(False, False)
        self.mainloop()


class MainWindow(ttk.Window):
    def __init__(self):
        super().__init__()

        self.geometry("1280x1080")

        columns = ('ip','time','detail')
 
        with open("access_logs.txt", "r") as file: 
            logs = file.readlines()

        date = []
        for log in logs: 
            a = log.split(" ")
            date.append(a[0])
            date.append(a[3]+a[4])
            date.append(a[5:22])

        tree = ttk.Treeview(self,bootstyle="success",columns=columns, show='headings')
        tree.pack(pady=10)

        for c in columns:
            tree.heading(c,text=c)

        for d in date:
            tree.insert('',END,values=date)


        self.resizable(False, False)
        self.mainloop()



try:
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password = password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor

    )
    nw = MainWindow()
    print("succses connection")

except Exception as ex:
    print("Connextion refused...")
    print(ex)