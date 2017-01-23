from collections import defaultdict
from itertools import islice
import locale
import os
import time
import csv

columnsA = defaultdict(list)
columnsB = defaultdict(list)
aux = defaultdict(list)
vector =[]

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
    #print(columnsA[0])
    arq = open ("diff.csv", "wt") #Choose the file you may want to save the entries
    for index, item in enumerate(columnsA[4]):
        if len(item) == 14:
            break
        elif index != 0:
            columnsA[4][index] = item.rjust(14,'0')
    for index, item in enumerate(columnsA[5]):
        if index != 0:
            i = time.strptime(item, "%m/%d/%Y")
            i = time.strftime('%d/%m/%Y', i)
            columnsA[5][index] = i
    for i in range(0, len(columnsA[1])):
        for j in range(0, len(columnsA)):
            arq.writelines(columnsA[j][i]+",")
        arq.writelines('\n')
