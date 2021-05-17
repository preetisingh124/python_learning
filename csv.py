import csv
with open('ceo.csv', mode ='r')as file
   csvFile = csv.reader(file)
for lines in csvFile:
  print(lines)
