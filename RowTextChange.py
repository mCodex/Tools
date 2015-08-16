from collections import defaultdict
import locale
import os
import csv

columns = defaultdict(list)
aux = defaultdict(list)
vector =[]

def readFile():
	csvName = ".csv" #Put here the CSV name
	with open(csvName) as f:
		reader = csv.reader(f,delimiter=",") 
		#reader.next()
		for row in reader: #
			for (i,v) in enumerate(row): 
				columns[i].append(v)


if __name__ == "__main__":
	readFile()

	out_file = open("test.csv", "wt") #The name of out file
	writer = csv.writer(out_file)

	for i in range(0, 30):
		for j in range(0,len(columns[0])):
			if (columns[i][j] == "X"): #Type in " " the text you want to change. I.E the script will change the row that contains X
				columns[i][j] = columns[i][0]
		writer.writerow(columns[i])

	out_file.close()


