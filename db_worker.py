import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='solar',
                                         user='solar',
                                         password='solar')

    nmbr = 1010
    
    sql_select_Query = "SELECT * FROM solar_swpc WHERE Nmbr = " + nmbr + " ORDER BY Date;"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    print("Total number of days the spot presented: ", cursor.rowcount)

    print("\nPrinting each laptop record")
    
    for row in records:
        
        print("Date = ", row[0], )
        print("Nmbr = ", row[1])
        print("Area  = ", row[4])
        

except Error as e:
    print("Error reading data from MySQL table", e)
finally:
    if (connection.is_connected()):
        connection.close()
        cursor.close()
        print("MySQL connection is closed")