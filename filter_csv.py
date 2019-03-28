import csv

with open('\C:\Users\afink\Downloads\data.csv','r') as fin, open('\C:\Users\afink\Downloads\jobs.csv','w')as fout:
#opens an initial .csv and creates a new .csv containing the filtered rows from the original dataset
    writer = csv.writer(fout, delimiter=",")
    header = fin.readline()
    fout.write(header)
    for row in csv.reader(fin, delimiter=","):
        #Alter row to match year and month in the original .csv
        if row[2] == '24643':
             writer.writerow(row)
