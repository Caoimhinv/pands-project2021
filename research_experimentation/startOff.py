# a bit of initial reading/parsing of the dataset
# Author: Caoimhin Vallely

# conventional method to open and print dataset as lists
import csv
with open('irisDataset.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# Nice way of opening and printing out the dataset
# From https://www.geeksforgeeks.org/working-csv-files-python/

# importing csv module 
import csv 
  
# csv file name 
filename = "irisDataset.csv"
  
# initializing the titles and rows list 
fields = [] 
rows = [] 
  
# reading csv file 
with open(filename, 'r') as csvfile: 
    # creating a csv reader object 
    csvreader = csv.reader(csvfile) 
      
    # extracting field names through first row 
    fields = next(csvreader) 
  
    # extracting each data row one by one 
    for row in csvreader: 
        rows.append(row) 
  
    # get total number of rows 
    print("Total no. of rows: %d"%(csvreader.line_num)) 
  
# printing the field names 
print('Field names are:' + ', '.join(field for field in fields)) 
  
#  printing the first 5 rows
print('\nFirst 5 rows are:\n') 
for row in rows[:5]: 
    # parsing each column of a row 
    for i in row: 
        print("%10s"%i), 
    print('\n') 
