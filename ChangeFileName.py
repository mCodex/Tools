from collections import defaultdict
import locale
import os
import csv

columns = defaultdict(list)
aux = defaultdict(list)
vector =[]

def readFile():
	csvName = "" #Put here the CSV name
	with open(csvName) as f:
		reader = csv.reader(f,delimiter=",") 
		#reader.next()
		for row in reader: #
			for (i,v) in enumerate(row): 
				columns[i].append(v)


def changeFileName(aux):
    folder = "" #FullPath to photo's path
    folderToRedirect = "NewFolder" #Folder name to redirect new renamed photos
    os.mkdir(folderToRedirect)  
    for root, dirs, filenames in os.walk(folder):
        for filename in filenames:
            fullpath = os.path.join(root, filename)
            filename_split = os.path.splitext(filename) # filename and extensionname (extension in [1])
            filename_zero, fileext = filename_split
            for i in range(0,len(aux)):
                if (filename_zero == aux[i][0]):
                    os.rename(fullpath, folderToRedirect+"/"+aux[i][1] + fileext)

readFile()

for i in range(len(columns[2])):
    vector.append ([columns[0][i], columns[1][i]])

aux = sorted(vetor, key= lambda vetor: vetor[0])

changeFileName(aux)
