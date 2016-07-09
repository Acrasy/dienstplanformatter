import csv
import os

with open('mein_dp.csv',encoding='latin-1') as infile:# ,open("clean_mein_dp.csv", 'a',newline='\n',encoding='latin-1') as outfile :
    data = csv.reader(infile)#, delimiter=',')
    newfile = 'clean_mein_dp.csv'                            # define name for the new file, open later when append
#next(data, None)                                            #skips first row
    new_csv  = [][]
    for row in data:
        for column in row:                                  #going through columns
            new_csv.append(column)                      #append to list if not keyword

    for i in range(length(new_csv)):
        csv.writer(open(newfile,'a')).writerow(new_csv[i])    
