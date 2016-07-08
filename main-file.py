import csv
import os

with open('mein_dp.csv',encoding='latin-1') as infile:# ,open("clean_mein_dp.csv", 'a',newline='\n',encoding='latin-1') as outfile :
    data = csv.reader(infile)#, delimiter=',')
    newfile = 'clean_mein_dp.csv'                            # define name for the new file, open later when append
#next(data, None)                                            #skips first row
    rmv = {'Microsoft Promotion 2016' , 'Mariahilfer Straße 42-48-1070-Wien' , 'Sales Promotion', 'Microsoft Promotion 2016' , 'Inaktiv'}                                                   #helper,what to remove
    for row in data:                                        # going through rows
        new_csv  = []                                       #new list we are going to write to
        for column in row:                                  #going through columns
            if column not in rmv:                           #filter keywords
                new_csv.append(column)                      #append to list if not keyword
        csv.writer(open(newfile,'a')).writerow(new_csv)     #write row (open file,append)
