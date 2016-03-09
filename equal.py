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
	arq = open ("equal.csv", "wt") #Choose the file you may want to save the entries
	for i in range(0,len(columnsA[0])):
		for j in range(0,len(columnsB[0])):
			if(columnsA[0][i]==columnsB[0][j]):
				arq.writelines(columnsA[0][i]+"\n")
