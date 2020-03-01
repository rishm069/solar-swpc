import os
import datetime
import sys
import collections
import mysql.connector
from mysql.connector import Error
from progress.bar import Bar
import argparse

def db_worker():
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='solar',
                                             user='solar',
                                             password='solar')

        cursor = connection.cursor()

        sql_select_Query = "SELECT * FROM solar_test ORDER BY Date ASC LIMIT 1;"
        cursor.execute(sql_select_Query)
        start_nmbr = cursor.fetchall()

        sql_select_Query = "SELECT * FROM solar_test ORDER BY Date DESC LIMIT 1;"
        cursor.execute(sql_select_Query)
        end_nmbr = cursor.fetchall()

        start_nmbr = start_nmbr[0]
        start_nmbr = start_nmbr[1]
        end_nmbr = end_nmbr[0]
        end_nmbr = end_nmbr[1]
        end_nmbr = end_nmbr + 1

        w_nmbr = int(end_nmbr) - int(start_nmbr)
        nmbr = start_nmbr
        print(w_nmbr, end_nmbr)
        bar = Bar('Processing', max=w_nmbr)
        for i in range(w_nmbr):
            while nmbr < end_nmbr:

                sql_select_Query = "SELECT * FROM solar_test WHERE Nmbr = " + str(nmbr) + " ORDER BY Date;"
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

                    #bigdate = str(row[0])
                    if row[4] > bigarea:
                        bigarea = row[4]
                        bigdate = str(row[0])
                        bignmbr = str(row[1])
                        bigdays = index + 1
                    index = index + 1

                try:
                    vlst = int(bigarea) / int(bigdays)
                except:
                    vlst = 0
                mySql_insert_query = """INSERT INTO `solar_result` (`Nmbr`, `Days lasted`, `Max Area`, `Days till Max Area`, `Date on the Max Area`, `Velocity`)
                                        VALUES (%s, %s, %s, %s, %s, %s) """

                recordTuple = (str(bignmbr), str(index), str(bigarea), str(bigdays), str(bigdate), str(vlst))
                cursor.execute(mySql_insert_query, recordTuple)
                connection.commit()

                nmbr = nmbr + 1
                bar.next()
        bar.finish()

    except Error as e:
        print("Error reading data from MySQL table", e)
def handler():

    directory = '/home/rinat/SRS/'

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

parser = argparse.ArgumentParser()

parser.add_argument('--handler', help='description for handler')
parser.add_argument('--db_worker', help='description for db_worker')
parser.add_argument('--option3', help='description for option3')
parser.add_argument('--option4', help='description for option4')

args = parser.parse_args()

if args.handler:
    try:
        handler()
    except Error as err:
        print('')
if args.db_worker:
    try:
        db_worker()
    except Error as err:
        print()
