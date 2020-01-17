import os
import datetime
import sys
import collections
from openpyxl import Workbook 
from openpyxl import load_workbook

#directory = r'C:\Users\User\Desktop\handl\SRS'
directory = r'C:\Users\User\Desktop\handl\TEST'

date = "20081231"
date_1 = datetime.datetime.strptime(date, "%Y%m%d")

def default():
    print('stuff')
    date = "20081231"
    date_1 = datetime.datetime.strptime(date, "%Y%m%d")
    for filename in os.listdir(directory):
        fh = open(filename).read().splitlines()
        for i, line in enumerate(fh): 
            if "Nmbr Location  Lo  Area  Z   LL   NN Mag Type" in line:
            
                #Uncomment to save output to a file
            
                #sys.stdout = open('results.txt', 'a')
                #sys.stdout = open('results_data_only.txt', 'a')
            
                sh = fh[i+1:i+40]
                s = "\n".join(sh)
                sl = s.rfind('IA.')
                
                
                date_1 = date_1 + datetime.timedelta(days=1)
                end_date = date_1.strftime('%Y-%m-%d')

                #Only-results mode if uncommend if-statement below and comment it from 39 to 42
            
                #if s.startswith("None"):
                    #break
            
                print('- - - - - - - - - - - - - - - - - - - - - - -')
                print('Имя файла: ' + str(filename))
                print('Дата наблюдений: ' + end_date)
                print('Полученные данные: ' + '\n')
            
                #Default: results + empty data
            
                if s.startswith("None"):
                    print('Данные отсутствуют')
                    print('\n')
                    break
            
                
                print(line)
                print(s[:sl])

                nl = s[:sl]
                nls = list(nl.split('\n'))
                nls.pop()
                
                # for loop belov extracts values from table to a list 
                # may be used to write it into a dictionary along with 'line'
                
                for value in nls:
                    res = value.split()
                    print(line)
                    print(res) 



                #print(nls)

def sepdata():
    colnumber = 2
    
    date = "20081231"
    date_1 = datetime.datetime.strptime(date, "%Y%m%d")
    for filename in os.listdir(directory):
        fh = open(filename).read().splitlines()
        for i, line in enumerate(fh): 
            if "Nmbr Location  Lo  Area  Z   LL   NN Mag Type" in line:
            
                sh = fh[i+1:i+40]
                s = "\n".join(sh)
                sl = s.rfind('IA.')
                
                date_1 = date_1 + datetime.timedelta(days=1)
                end_date = date_1.strftime('%Y-%m-%d')

                colA = "A" + str(colnumber)
                colB = "B" + str(colnumber)
                colC = "C" + str(colnumber)
                colD = "D" + str(colnumber)
                colE = "E" + str(colnumber)
                colF = "F" + str(colnumber)
                colG = "G" + str(colnumber)
                colH = "H" + str(colnumber)
                colI = "I" + str(colnumber)
                

                print('Processing date: ' + end_date + '/2018-12-31')

                wb = load_workbook('sample.xlsx')
                ws = wb.active
                ws[colA] = end_date
                wb.save('sample.xlsx')

                if s.startswith("None"):
                    wb = load_workbook('sample.xlsx')
                    ws = wb.active
                    
                    ws[colB] = 0
                    ws[colC] = 0
                    ws[colD] = 0
                    ws[colE] = 0
                    ws[colF] = 0
                    ws[colG] = 0
                    ws[colH] = 0
                    ws[colI] = 0
        
                    wb.save('sample.xlsx')
                    colnumber = colnumber + 1
                    break
                nl = s[:sl]
                nls = list(nl.split('\n'))
                nls.pop()
                
                # for loop belov extracts values from table to a list 
                # may be used to write it into a dictionary along with 'line'
                
                for value in nls:
                    res = value.split()
                    wb = load_workbook('sample.xlsx')
                    ws = wb.active
                   
                    ws[colB] = int(res[0])
                    ws[colC] = res[1]
                    ws[colD] = int(res[2])
                    ws[colE] = int(res[3])
                    ws[colF] = res[4]
                    ws[colG] = int(res[5])                 
                    ws[colH] = int(res[6])
                    try:
                        ws[colI] = res[7]
                    except:
                        ws[colI] = ' '

                    wb.save('sample.xlsx')
                    colnumber = colnumber + 1
                    colA = "A" + str(colnumber)
                    colB = "B" + str(colnumber)
                    colC = "C" + str(colnumber)
                    colD = "D" + str(colnumber)
                    colE = "E" + str(colnumber)
                    colF = "F" + str(colnumber)
                    colG = "G" + str(colnumber)
                    colH = "H" + str(colnumber)
                    colI = "I" + str(colnumber)
                  
def nmbr():
    #colnumber = 2
    nmbrl = list()
    nmbrd = dict()

    date = "20081231"

    date_1 = datetime.datetime.strptime(date, "%Y%m%d")
    for filename in os.listdir(directory):
        fh = open(filename).read().splitlines()
        for i, line in enumerate(fh): 
            if "Nmbr Location  Lo  Area  Z   LL   NN Mag Type" in line:
            
                sh = fh[i+1:i+40]
                s = "\n".join(sh)
                sl = s.rfind('IA.')
                
                date_1 = date_1 + datetime.timedelta(days=1)
                end_date = date_1.strftime('%Y-%m-%d')

                #colA = "A" + str(colnumber)
                #colB = "B" + str(colnumber)
                #colC = "C" + str(colnumber)
                #colD = "D" + str(colnumber)
                #colE = "E" + str(colnumber)
                #colF = "F" + str(colnumber)
                #colG = "G" + str(colnumber)
                #colH = "H" + str(colnumber)
                #colI = "I" + str(colnumber)
                

                #print('Processing date: ' + end_date + '/2018-12-31')

                #wb = load_workbook('sample_nmbr.xlsx')
                #ws = wb.active
                #ws[colA] = end_date
                #wb.save('sample_nmbr.xlsx')

                if s.startswith("None"):
                    break
                nl = s[:sl]
                nls = list(nl.split('\n'))
                nls.pop()
                
                # for loop belov extracts values from table to a list 
                # may be used to write it into a dictionary along with 'line'
                
                
                
                for value in nls:
                    res = value.split()
                    #wb = load_workbook('sample_nmbr.xlsx')
                    #ws = wb.active
                   

                    nmbrn = int(res[0])
                    nvalue = int(res[3])
                    
                    nmbrl.append(nmbrn)
                    
                    if nmbrn not in nmbrd:
                        nmbrd.update({nmbrn:nvalue})
                    else:
                        for k, v in nmbrd.items():
                            if k == nmbrn:
                                if v < nvalue:
                                    nmbrd.update({nmbrn:nvalue})
                    
                    #nmbrd.update({nmbrn:nvalue})

        nmbrl.sort()
        counter=collections.Counter(nmbrl)
        print(counter)
        print(nmbrd)
        
                
nmbr()  





#nmbrd, counter = nmbr()        

#print(counter)
#print(nmbrd)



#colB = "B2" 
        #colC = "C2" 
        #colD = "D2" 
        #colE = "E2" 
        #colA = "A2" 
        #colF = "F2" 
        #colG = "G2" 
        #colH = "H2" 
        #colI = "I2" 

        
        #wb = load_workbook('new_sample.xlsx')
        #ws = wb.active

        #for k, v in counter:
            #ws[colB] = k
            #ws[colC] = v
        #for q, w in nmbrd:
            #ws[colF] = q
            #ws[colG] = w



        #wb.save('new_sample.xlsx')



















        
   
