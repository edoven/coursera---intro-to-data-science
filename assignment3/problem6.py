import MapReduce
import sys

"""
Matrix Multiplication

Assumption: the sizes of the matrixes are given: A[5x5] and B[5x5]
"""

size = 4

mr = MapReduce.MapReduce()


def mapper(record):
	matrixId = record[0]
	if matrixId=="a":
		row=record[1]
		for i in range(0,5):
			cIndex = str(row)+str(i)
			mr.emit_intermediate(cIndex, record)
	if matrixId=="b":
		column=record[2]
		for i in range(0,5):
			cIndex = str(i)+str(column)
			mr.emit_intermediate(cIndex, record)
    


def reducer(key, list_of_values):
	tot = 0
	for elementA in list_of_values:
		if (elementA[0]=="a"):
			columnElementA = elementA[2]
			for elementB in list_of_values:
				if (elementB[0]=="b"):
					rowElementB = elementB[1]
					if columnElementA==rowElementB:
						tot = tot + elementA[3]*elementB[3]
						break
	if tot!=0:
		mr.emit([int(key[0]), int(key[1]), tot])


if __name__ == '__main__':
	inputdata = open(sys.argv[1])
  	mr.execute(inputdata, mapper, reducer)
