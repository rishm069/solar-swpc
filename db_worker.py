import mysql.connector
from mysql.connector import Error
from progress.bar import Bar

#worker needs the following:

# CREATE USER 'solar'@'localhost' IDENTIFIED BY 'solar';
# GRANT ALL PRIVILEGES ON solar.* TO 'solar'@'localhost';

#CREATE TABLE `solar_result` 
#(`Nmbr` int,`Days lasted` varchar(100) DEFAULT NULL,
#`Max Area` int DEFAULT NULL,`Days till Max Area` varchar(100) DEFAULT NULL,
#`Date on the Max Area` varchar(100) DEFAULT NULL);


try:
    connection = mysql.connector.connect(host='localhost',
                                         database='solar',
                                         user='solar',
                                         password='solar')

    nmbr = 1010
    bar = Bar('Processing', max=1721)
    for i in range(1721):
        while nmbr < 2731:

            sql_select_Query = "SELECT * FROM solar_swpc WHERE Nmbr = " + str(nmbr) + " ORDER BY Date;"
            cursor = connection.cursor()
            cursor.execute(sql_select_Query)
            records = cursor.fetchall()

            bigarea = 0
            bignmbr = nmbr
            rcount = 0
            index = 1
            bigdate = None
            bigdays = 0
            for index, row in enumerate(records):

                bigdate = str(row[0])
                if row[4] > bigarea:
                    bigarea = row[4]
                    bigdate = str(row[0])
                    bignmbr = str(row[1])
                    bigdays = index + 1
                index = index + 1

            mySql_insert_query = """INSERT INTO `solar_result` (`Nmbr`, `Days lasted`, `Max Area`, `Days till Max Area`, `Date on the Max Area`)
                                    VALUES (%s, %s, %s, %s, %s) """

            recordTuple = (str(bignmbr), str(index), str(bigarea), str(bigdays), str(bigdate))
            cursor.execute(mySql_insert_query, recordTuple)
            connection.commit()

            nmbr = nmbr + 1
            bar.next()
    bar.finish()

except Error as e:
    print("Error reading data from MySQL table", e)