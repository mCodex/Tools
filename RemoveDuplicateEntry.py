#Remove duplicate entry from array and save it in a file

from collections import defaultdict
import locale
import os
import csv

columns = defaultdict(list)
aux = defaultdict(list)
vector =[]

def readFile():
	csvName = "diff1.csv" #Put here the CSV name
	with open(csvName) as f:
		reader = csv.reader(f,delimiter=",") 
		#reader.next()
		for row in reader: #
			for (i,v) in enumerate(row): 
				columns[i].append(v)

if __name__ == "__main__":
	readFile()
	for j in range(0, len(columns[0])):
		vector.append(columns[0][j]) #Choose the column that you want to remove duplicate entries in my case "2"

	arq = open ("test.txt", "wt") #Choose the file you may want to save the entries 
	for i in set(vector):
		arq.writelines(i+"\n")
