from secrets import password, username
import mysql.connector as mysql
from tabulate import tabulate

# Username and Password are hidden for security
HOST = 'seniorprojectdatabase.cemghzzxxgym.us-west-1.rds.amazonaws.com'
USER = username
PASSWORD = password

def init():
    global db_connection, cursor
    # connect to the database
    db_connection = mysql.connect(host=HOST, user=USER, password=PASSWORD)

    # get the db cursor
    cursor = db_connection.cursor()

    # get database information
    cursor.execute("select database();")
    database_name = cursor.fetchone()
    print("[+] You are connected to the database:")

    # create a new database called library
    cursor.execute("create database if not exists datalog")

    # use that database
    cursor.execute("use datalog")

    # create a table
    cursor.execute("""create table if not exists firetable (
        `id` integer primary key auto_increment not null,
        `time` timestamp not null,
        `station` integer not null,
        `temp` float not null,
        `humid` integer not null,
        `firestatus` boolean not null
        )""")

def insert(fires):
    global db_connection, cursor
    # iterate over books list
    for fire in fires:
        time = fire.get("time")
        station = fire.get("station")
        temp = fire.get("temp")
        humid = fire.get("humid")
        firestatus = fire.get("firestatus")
        # insert each book as a row in MySQL
        cursor.execute("""insert into firetable (time, station, temp, humid, firestatus) values (
            %s, %s, %s, %s, %s
        )
        """, params=(time, station, temp, humid, firestatus))

    # commit insertion
    db_connection.commit()

# main ioop
def main():
    global db_connection, cursor
    init()
    # insert some books
    fires = [
        {
            "time": "1999-01-28 12:01:02",
            "station": 1,
            "temp": 20.5,
            "humid": 35,
            "firestatus": False,
        },
        {
            "time": "1998-01-29 12:03:04",
            "station": 2,
            "temp": 200.5,
            "humid": 5,
            "firestatus": True,
        }
    ]
    insert(fires)

    # fetch the database
    cursor.execute("select * from firetable")
    
    # get all selected rows
    rows = cursor.fetchall()

    # print all rows in a tabular format
    print(tabulate(rows, headers=cursor.column_names))

    # close the cursor
    cursor.close()

    # close the DB connection
    db_connection.close()


if __name__ == '__main__':
    try:
        main()
        pass
    except KeyboardInterrupt:
        pass
