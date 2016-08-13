import csv
import os

print("Bitte Name der .csv Datei eingeben:")
name = input()

#with open('mein_dp.csv',encoding='latin-1') as infile:# ,open("clean_mein_dp.csv", 'a',newline='\n',encoding='latin-1') as outfile :
with open(str(name)+ '.csv',encoding='latin-1') as infile:# ,open("clean_mein_dp.csv", 'a',newline='\n',encoding='latin-1') as outfile :

    data = csv.reader(infile)#, delimiter=',')
    newfile = 'clean_mein_dp.csv'                           # define name for the new file, open later when append
    new_csv  = []
    cnt=-1                                                  #needed for indices -1 for starting at 0

    print("Pls enter which colum to remove.")               
    print("Your options are:" + str(next(data)))            #next() shows first row and sets cursor to second
    print("1 for first, 2 for second, 3 for third and so on")
    #rmv = "'" + str(input()) + "'"                          #Eingabe als String mit '' für if
    rmv = int(input())                                       #Eingabe als Int 
    
#test cmt for push


    for row in data:
        new_csv.append([])                                  #making list 2d
        cnt+=1
        for column in row:                                  #going through columns
            #if column not in rmv:                           #filter csv for array content
            #    new_csv[cnt].append(column)                 #append to list if not keyword
            new_csv[cnt].append(column)
    
                
    for rows in new_csv:                                    #deletes the right column in every row
        del rows[rmv-1]

    for i in range(len(new_csv)):                           #going through every line
        csv.writer(open(newfile,'a')).writerow(new_csv[i])  #append every line to file

