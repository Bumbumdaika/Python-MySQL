import pymysql
from config import host, user, password, db_name

try:
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password = password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor

    )
    print("succses connection")
    try:
        #create table - создание таблицы
        # with connection.cursor() as cursor:
        #     create_table_querry="CREATE TABLE sakila.`users` (id int AUTO_INCREMENT,"\
        #                         "name varchar(32),"\
        #                         "password varchar(32),"\
        #                         "email varchar(32), PRIMARY KEY(id));"
        # cursor.execute(create_table_querry)
        # print("Table created successfully")


        # insert data  - добавление данный в таблицу
        # with connection.cursor() as cursor:
        #     insert_querry="INSERT INTO `user`(login, pwd) VALUES ('white_wolf','geralt')"
        #     cursor.execute(insert_querry)
        #     connection.commit()

        # insert data  - добавление данный в таблицу
        with connection.cursor() as cursor:
            insert_querry="INSERT INTO `mydb`.`logs`(ip, time, another) VALUES ('23.12.32.104','[06/Sep/2016:21:43:23-0400]','что-то делал')"
            cursor.execute(insert_querry)
            connection.commit()

        #update data  - изменение данных в таблице
        # with connection.cursor() as cursor:
        #     update_querry="UPDATE `user` SET password = 'xxxXXX' where id=3"
        #     cursor.execute(update_querry)
        #     connection.commit()
         
        #delete data - удаление данных из таблицы
        # with connection.cursor() as cursor:
        #     delete_querry="DELETE FROM `user` where id = 5:"
        #     cursor.execute(delete_querry)
        #     connection.commit()

        #delete data - удаление данных из таблицы
        # with connection.cursor() as cursor:
        #     drop_table_querry="Drop TABLE `user`"
        #     cursor.execute(drop_table_querry)
        #     print("Table delete")

        #select data - выборка данных из таблицы
        with connection.cursor() as cursor:
            select_all_rows="select * from `mydb`.`logs`"
            cursor.execute(select_all_rows)
            rows = cursor.fetchall()
        
            print(rows)
    finally:
        connection.close()
except Exception as ex:
    print("Connextion refused...")
    print(ex)



    