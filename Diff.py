from collections import defaultdict
import locale
import os
import csv

columnsA = defaultdict(list)
columnsB = defaultdict(list)
aux = defaultdict(list)
vector =[]

def readFileB():
	csvName = "b.csv" #Put here the CSV name
	with open(csvName) as f:
		reader = csv.reader(f,delimiter=",")
		#reader.next()
		for row in reader: #
			for (i,v) in enumerate(row):
				columnsB[i].append(v.title())

def readFileA():
	csvName = "a.csv" #Put here the CSV name
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
	arq = open ("diff.csv", "wt") #Choose the file you may want to save the entries
	for i in set(list(set(columnsA[0]) - set(columnsB[0]))):
		arq.writelines(i+"\n")
