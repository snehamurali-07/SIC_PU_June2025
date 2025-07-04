import pymysql

def connect_db():
    connection = None
    try:
        connection = pymysql.connect(
            host = "localhost",
            user = "****",
            password = "**********",
            database = "samsung_db"
        )
        print("Database connected")
    except:
        print("Database connection failed")
    return connection


def disconnect_db(connection):
    try:
        connection.close()    # to disconnect the database
        print("Database disconnected")
    except:
        print("Database disconnection failed")


def create_db():
    query = 'create database IF NOT EXISTS samsung_db'
    try:
        connection = connect_db()
        cursor = connection.cursor()
        cursor.execute(query)
        print("Database created")
        cursor.close()
        disconnect_db(connection)
    except:
        print("Database creation failed")


def create_table():
    query = 'create table IF NOT EXISTS employees(id int primary key auto_increment, name varchar(50) not null, designation varchar(30), phone_number bigint unique, salary float, commission float default(0), years_of_experience tinyint, technology	varchar(30)	not null)'
    connection = connect_db()
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        print('Table created')
        cursor.close()
        disconnect_db(connection)
    except:
        print('Table creation failed')


def read_employee_details():
    connection = connect_db()
    name = input("Enter employee name:")
    designation = input("Enter employee designation:")
    phone_number = int(input("Enter employee phone number:"))
    salary = float(input("Enter employee salary:"))
    commission = float(input("Enter employee commission:"))
    years_of_experience = input("Enter employee years of experience:")
    technology = input("Enter employee technology:")
    return (name, designation, phone_number, salary, commission, years_of_experience, technology)


def insert_employee():
    employee = read_employee_details()
    query = 'insert into employees (name, designation, phone_number, salary, commission, years_of_experience, technology) values (%s, %s, %s, %s, %s, %s, %s)'
    try:
        connection = connect_db()
        cursor = connection.cursor()
        cursor.execute(query, employee)
        connection.commit()
        print("Employee details inserted")
        cursor.close()
        disconnect_db(connection)
    except:
        print("Employee details insertion failed")


def read_all_employees():
    query = 'select * from employees'
    try:
        connection = connect_db()
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        print("All rows retrived")
        cursor.close()
        disconnect_db(connection)
    except:
        print("Rows retrival failed")


def search_employee():
    id = int(input("Enter id of employee to search:"))
    query = f'select * from employees where id = {id}'
    try:
        connection = connect_db()
        cursor = connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        print("Employee retrived")
        cursor.close()
        disconnect_db(connection)
    except:
        print("Employee retrival failed")

connection = connect_db()
read_all_employees()