import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
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
    list = []
    for v in list_of_values:
		#if v not in list: #duplicates already removed in the mapper
		list.append(v)
    mr.emit((key, list))


# the input file is a txt file where every line has this forma: <id>,<document> 
# Example:
# 1,this is the first document
# 2,this is the second document bla bla bla
# 432,this is a document with id 432
if __name__ == '__main__':
	inputdata = open(sys.argv[1])
  	mr.execute(inputdata, mapper, reducer)
