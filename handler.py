import os
import datetime
import sys
import collections
import mysql.connector

directory = '/home/rinat/SRS/'

def handler():
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='solar',
                                             user='solar',
                                             password='solar')
    except Error as e:
        print("Error reading data from MySQL table", e)
    ldir = os.listdir(directory)
    ldir.sort()
    for filename in ldir:
        fh = open(directory + filename).read().splitlines()
        filename = filename
        print(filename)
        for i, line in enumerate(fh):
            if "Nmbr Location  Lo  Area  Z   LL   NN Mag Type" in line:

                sh = fh[i+1:i+40]
                s = "\n".join(sh)
                sl = s.rfind('IA.')

                dta = filename
                date= dta.split("SRS.txt", 1)[0]
                date = datetime.datetime.strptime(date, "%Y%m%d")
                date = date.strftime('%Y-%m-%d')
                #print(date)

                if s.startswith("None"):
                    break
                nl = s[:sl]
                nls = list(nl.split('\n'))
                nls.pop()

                for value in nls:
                    res = value.split()

                    #print(res)
                    Date = date
                    Nmbr = res[0]
                    Location = res[1]
                    Lo = res[2]
                    Area = res[3]
                    Z = res[4]
                    LL = res[5]
                    NN = res[6]
                    try:
                        Mag_Type = res[7]
                    except:
                        Mag_Type = ' '

                    mySql_insert_query = """INSERT INTO `solar_test` (`Date`, `Nmbr`, `Location`, `Lo`, `Area`, `Z`, `LL`, `NN`, `Mag_Type`)
                                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) """


                    recordTuple = (str(Date), str(Nmbr), str(Location), str(Lo), str(Area), str(Z), str(LL), str(NN), str(Mag_Type))
                    cursor = connection.cursor()
                    try:
                        cursor.execute(mySql_insert_query, recordTuple)
                    except:
                        recordTuple = (str(Date), str(Nmbr), str(Location), str(Lo), str(Area), str(Z), str(LL), str(0), str(Mag_Type))
                        cursor.execute(mySql_insert_query, recordTuple)
                    connection.commit()

                    print(Date,Nmbr,Location,Lo,Area,Z,LL,NN,Mag_Type)

handler()

















        
   
