from collections import defaultdict
import locale
import os
import csv

columnsA = defaultdict(list)
columnsB = defaultdict(list)
aux = defaultdict(list)
vector =[]

def readFileB():
	csvName = "C.csv" #Put here the CSV name
	with open(csvName) as f:
		reader = csv.reader(f,delimiter=",")
		#reader.next()
		for row in reader: #
			for (i,v) in enumerate(row):
				columnsB[i].append(v.title())

def readFileA():
	csvName = "diff.csv" #Put here the CSV name
	with open(csvName) as f:
		reader = csv.reader(f,delimiter=",")
		#reader.next()
		for row in reader: #
			for (i,v) in enumerate(row):
				columnsA[i].append(v.title())

if __name__ == "__main__":
	readFileA()
	readFileB()
	#print(columnsA[0])
	arq = open ("brian.csv", "wt") #Choose the file you may want to save the entries
	for i in range(0, len(columnsB[1])):
		columnsB[1][i] = columnsB[1][i].lower()
		for j in range(0, len(columnsA[0])):
			columnsA[0][j] = columnsA[0][j].lower()
			if(columnsA[0][j] == columnsB[1][i]):
				arq.writelines(columnsB[0][i]+'/'+columnsB[1][i]+'/'+columnsB[2][i]+columnsB[3][i]+'/'+columnsB[4][i]+'\n')
	arq.close()
