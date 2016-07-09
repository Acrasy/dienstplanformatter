import csv
import os

with open('mein_dp.csv',encoding='latin-1') as infile:# ,open("clean_mein_dp.csv", 'a',newline='\n',encoding='latin-1') as outfile :
    data = csv.reader(infile)#, delimiter=',')
    newfile = 'clean_mein_dp.csv'                           # define name for the new file, open later when append
#next(data, None)                                           #skips first row
    new_csv  = []
    #new_csv.append([])
    cnt=-1                                                  #needed for indices -1 for starting at 0

    for row in data:
        new_csv.append([])                                  #making list 2d
        cnt+=1
        for column in row:                                  #going through columns
            new_csv[cnt].append(column)                     #append to list if not keyword

    for i in range(len(new_csv)):                           #going through every line
        csv.writer(open(newfile,'a')).writerow(new_csv[i])  #append every line to file


#print(new_csv[0][0] +"  " + new_csv[-2][-1])
#print("_________________________")
#print(new_csv)
