#Important: You need to download transposer.py and put it into same folder
#This code will help you change the following name on csv column: Andrade, João Marcos to João Marcos Andrade 


from collections import defaultdict
import locale
import os
import csv

columns = defaultdict(list)
aux = defaultdict(list)

def readFile():
	csvName = "alunos.csv" #Put here the CSV name
	with open(csvName) as f:
		reader = csv.reader(f,delimiter=",") 
		#reader.next()
		for row in reader: #
			for (i,v) in enumerate(row): 
				columns[i].append(v)

def doChange():
	for i in range(1,len(columns[1])):
		secondName, firstName = columns[1][i].split(", ",1)
		columns[1][i] = firstName + " "+secondName
		#print(i)

def savingInFileTwo():
	out_file = open("test.csv", "wt") #The name of out file
	writer = csv.writer(out_file)

	for i in range(0, 11):
		writer.writerow(columns[i])

	out_file.close()


if __name__ == "__main__":
	readFile()
	doChange()
	savingInFileTwo()
	os.system("python transposer.py test.csv transposed.csv") #This will transpose test.csv
	#print (columns[1])

