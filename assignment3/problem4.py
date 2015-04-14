import MapReduce
import sys

"""
Social graph "analyzer"
"""

mr = MapReduce.MapReduce()


def mapper(record):   
	mr.emit_intermediate(record[0], [record[1], 1])
	mr.emit_intermediate(record[1], [record[0], -1])


def reducer(user, relations):
    i=0
    while i<len(relations):
		relationI = relations.pop(i)
		j=0
		found=False
		while j<len(relations):
			relationJ = relations[j]
			if relationI[0]==relationJ[0]: #same name
				found=True
				relations.pop(j) #remove to avoid duplicates
				break
			j=j+1
		if found==False:
			mr.emit((user, relationI[0]))


if __name__ == '__main__':
	inputdata = open(sys.argv[1])
  	mr.execute(inputdata, mapper, reducer)
