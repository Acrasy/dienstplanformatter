import csv
import os

with open('mein_dp.csv',encoding='latin-1') as infile:# ,open("clean_mein_dp.csv", 'a',newline='\n',encoding='latin-1') as outfile :
    data = csv.reader(infile)#, delimiter=',')
    newfile = 'clean_mein_dp.csv'                           # define name for the new file, open later when append
#next(data, None)                                           #skips first row
    new_csv  = []
    cnt=-1                                                  #needed for indices -1 for starting at 0


    #Production block
    print("Pls enter which colum to remove.")               
    print("Your options are:" + str(next(data)))            #next() shows first row and sets cursor to second
    print("1 for first, 2 for second, 3 for third and so on")
    #rmv = "'" + str(input()) + "'"                          #Eingabe als String mit '' für if
    rmv = int(input())                                       #Eingabe als Int 
    
    #Testing block
    #rmv = {'Microsoft Promotion 2016' , 'Mariahilfer Straße 42-48-1070-Wien' , 'Sales Promotion', 'Microsoft Promotion 2016' , 'Inaktiv'}                                                   #helper,what to remove


    for row in data:
        new_csv.append([])                                  #making list 2d
        cnt+=1
        for column in row:                                  #going through columns
            #if column not in rmv:                           #filter csv for array content
            #    new_csv[cnt].append(column)                 #append to list if not keyword
            new_csv[cnt].append(column)
    
    #index = 0
    #while(rmv != new_csv[0][index]):                        #set rmv to column index via cycling
    #    if rmv == new_csv[0][index]:                        #decided to use number as input
    #        rmv = index
    #    else:
    #        index +=1
    clean = []
    
    for final_row in new_csv:                               #versuch jedes elemnt in zeile zu durchgehn
        for final_elem in final_row:                        #um dann den index zu überprüfen
            if final_row.index(final_elem) != rmv:          #wenn der index nicht dem rmv entspricht dann append
                clean.append(final_elem)
                
        

    for i in range(len(clean)):                           #going through every line
        csv.writer(open(newfile,'a')).writerow(new_csv[i])  #append every line to file

