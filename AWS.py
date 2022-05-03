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

    #cursor.execute("drop table firetable")

    # create a table
    cursor.execute("""create table if not exists firetable (
        `id` integer primary key auto_increment not null,
        `time` timestamp not null,
        `station` integer not null,
        `temp` float not null,
        `humid` integer not null,
        `colevel` float not null
        )""")

def insert(fire):
    global db_connection, cursor
    time = fire.get("time")
    station = fire.get("station")
    temp = fire.get("temp")
    humid = fire.get("humid")
    colevel = fire.get("colevel")
    # insert each book as a row in MySQL
    cursor.execute("""insert into firetable (time, station, temp, humid, colevel) values (
        %s, %s, %s, %s, %s
    )
    """, params=(time, station, temp, humid, colevel))

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
            "colevel": 3.2,
        },
        {
            "time": "1998-01-29 12:03:04",
            "station": 2,
            "temp": 200.5,
            "humid": 5,
            "colevel": 7.7,
        }
    ]
    for fire in fires:
        insert(fire)

    # fetch the database
    cursor.execute("select * from firetable order by time")
    
    # get all selected rows
    rows = cursor.fetchall()

    # print all rows in a tabular format
    print(tabulate(rows, headers=cursor.column_names))
    
    # delete test data
    cursor.execute("delete from firetable where time < '2000-01-01'")

    # commit delete
    db_connection.commit()

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
