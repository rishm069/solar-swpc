import mysql.connector
from mysql.connector import Error

#worker needs the following:
# CREATE USER 'solar'@'localhost' IDENTIFIED BY 'solar';
# GRANT ALL PRIVILEGES ON solar.* TO 'solar'@'localhost';


try:
    connection = mysql.connector.connect(host='localhost',
                                         database='solar',
                                         user='solar',
                                         password='solar')

    nmbr = 1010
    while nmbr < 2731:
        
        sql_select_Query = "SELECT * FROM solar_swpc WHERE Nmbr = " + str(nmbr) + " ORDER BY Date;"
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        records = cursor.fetchall()
        print("Total number of days the spot presented: " + str(cursor.rowcount))

        bigarea = 0
        bignmbr = 0
        rcount = 0
        index = 1
        bigdate = None
        for index, row in enumerate(records):

            print("Date = " + str(row[0]))
            print("Nmbr = " + str(row[1]))
            print("Area  = " + str(row[4]) + "\n")
            bigdate = str(row[0])
            if row[4] > bigarea:
                bigarea = row[4]
                bigdate = str(row[0])
                bignmbr = str(row[1])
                bigday = index + 1
            index = index + 1
            print(index)

        print("The biggest area was reached on: " + str(bigdate) + " with area size: " + str(bigarea) + " The number: " + str(bignmbr) + " has reached the biggest area within " + str(bigday) + " days.")
        nmbr = nmbr + 1

except Error as e:
    print("Error reading data from MySQL table", e)