import MapReduce
import sys

"""
Inverted Index Builder
"""

mr = MapReduce.MapReduce()


# key: document identifier
# value: document contents
def mapper(record):   
	documentId = record[0]
	documentContent = record[1]
	words = documentContent.split()
	words = list(set(words)) #let's remove duplicates
	for word in words:
		mr.emit_intermediate(word, documentId)


def reducer(key, list_of_values): 
    mr.emit((key, sorted(list_of_values)))


# the input file is a txt file where every line has this forma: <id>,<document> 
# Example:
# 1,this is the first document
# 2,this is the second document bla bla bla
# 432,this is a document with id 432
if __name__ == '__main__':
	inputdata = open(sys.argv[1])
  	mr.execute(inputdata, mapper, reducer)
