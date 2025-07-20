from pathlib import Path
import ttkbootstrap as ttk
from tkinter import *
import pandas as pd
from pandastable import Table
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import pymysql
from config import host, user, password, db_name, res



class MainWindow(ttk.Window):
    def __init__(self):
        super().__init__()

        self.geometry("1000x600")
        frame_table=ttk.Frame(self)
        frame_duwn = ttk.Frame(self)
        frame_filters = ttk.Frame(frame_duwn)
        frame_insert = ttk.Frame(frame_duwn)
        frame_function=ttk.Frame(frame_duwn)
        

        def char():
            a=res.json()
            dates=a[0]
            d1=dates.split('"ip"')
            d=d1[1:]
            row = []
            #  [71:195]- деталь,[28:55] data, [3:16]вычленить ip, [:203]убрать номер
            for l in d: 
                ip=l[3:16]
                row.append(ip)
                date=l[28:55]
                row.append(date)
                detail=l[71:195]
                row.append(detail)
                tree.insert('',END,values=row)
            # for re in res:
            #     tree.insert('',END,values=re)

        def filter():
            
            for col in tree['columns']:
                tree.heading(col, text='')
            tree.delete(*tree.get_children())
            for c in columns:
                tree.heading(c,text=c)
            a=res.json()
            dates=a[0]
            d1=dates.split('"ip"')
            d=d1[1:]
            row = []
            #  [71:195]- деталь,[28:55] data, [3:16]вычленить ip, [:203]убрать номер
            for l in d: 
                ip=l[3:16]
                date=l[28:55]
                detail=l[71:195]
                if ip in text_ips_filter.get() or date in text_tim_filter.get():
                    row.append(ip)
                    row.append(date)
                    row.append(detail)
                tree.insert('',END,values=row)

        
        def insert():
            row = []
            ip=text_ips_insert.get()
            date=text_tim_insert.get()
            detail=text_detail_insert.get()
            row.append(ip)
            row.append(date)
            row.append(detail)
            tree.insert('',END,values=row)


        frame_table.grid(column=5, row = 1)
        frame_duwn.grid(column=5, row=2)
        frame_table['borderwidth'] = 5
        frame_table['relief'] = 'sunken'
        frame_duwn['borderwidth'] = 5
        frame_duwn['relief'] = 'sunken'
        frame_filters.grid(column=3, row=1)
        frame_function.grid(column=5, row=1)
        frame_insert.grid(column=8, row=1)

        title_insert=ttk.Label(frame_insert, text="Вставить")
        title_ip_insert=ttk.Label(frame_insert, text="ip")
        text_ips_insert=ttk.Entry(frame_insert)
        title_time_insert=ttk.Label(frame_insert, text="time")
        text_tim_insert=ttk.Entry(frame_insert)
        title_detail_insert=ttk.Label(frame_insert, text="detail")
        text_detail_insert=ttk.Entry(frame_insert)
        btn_exec_insert = ttk.Button(frame_insert, text='выдолнить', command=insert)

        title_insert.pack(pady=10)
        title_ip_insert.pack(pady=10)
        text_ips_insert.pack(pady=10)
        title_time_insert.pack(pady=10)
        text_tim_insert.pack(pady=10)
        title_detail_insert.pack(pady=10)
        text_detail_insert.pack(pady=10)
        btn_exec_insert.pack(pady=10)

        title_filter=ttk.Label(frame_filters, text="Фильтрация")
        title_ip_filter=ttk.Label(frame_filters, text="ip")
        text_ips_filter=ttk.Entry(frame_filters)
        title_time_filter=ttk.Label(frame_filters, text="time")
        text_tim_filter=ttk.Entry(frame_filters)
        btn_exec_filter = ttk.Button(frame_filters, text='выдолнить', command=filter)

        title_filter.pack(pady=10)
        title_ip_filter.pack(pady=10)
        text_ips_filter.pack(pady=10)
        title_time_filter.pack(pady=10)
        text_tim_filter.pack(pady=10)
        btn_exec_filter.pack(pady=10)

        columns = ('ip','time','detail')
        tree = ttk.Treeview(frame_table,bootstyle="success",columns=columns,show='headings')
        tree.pack(pady=30, fill=X)

        for c in columns:
            tree.heading(c,text=c)

        btn_update=ttk.Button(frame_function, text='обновить')
        btn_logs=ttk.Button(frame_function, text='Просмотреть логи', command=char)
        btn_append=ttk.Button(frame_function, text='добавить')
        btn_close=ttk.Button(frame_function, text='закрыть')

        btn_update.pack(pady=10)
        btn_logs.pack(pady=10)
        btn_append.pack(pady=10)
        btn_close.pack(pady=10)

        #пример значений
        def char():
            values = (("Большой куш","Гай Ричи",10),("Начало","Кристофер Нолан",10),("Джентльмены","Гай Ричи",9))
            for value in values:
                tree.insert('',END,values=value)

        self.resizable(True, True)
        self.mainloop()

main=MainWindow()