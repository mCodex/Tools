from collections import defaultdict
import locale
import os
import csv

columns = defaultdict(list)
aux = defaultdict(list)
vector =[]

def readFile():
	csvName = "sabin.csv" #Put here the CSV name
	with open(csvName) as f:
		reader = csv.reader(f,delimiter=",") 
		#reader.next()
		for row in reader: #
			for (i,v) in enumerate(row): 
				columns[i].append(v)

readFile()

out_file = open("/home/mateus/Área de trabalho/teste.csv", "wt")
writer = csv.writer(out_file)

for i in range(0, 30):
	for j in range(0,len(columns[0])):
		if (columns[i][j] == "X"):
			columns[i][j] = columns[i][0]
	writer.writerow(columns[i])

out_file.close()


