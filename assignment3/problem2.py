import MapReduce
import sys

"""
Join with Map Reduce
"""

mr = MapReduce.MapReduce()


# key: document identifier
# value: document contents
def mapper(record):
	orderId = record[1]
	mr.emit_intermediate(orderId, record)	


def reducer(key, list_of_values): 
	orderFields = []

	#let's find and save the order record
	for record in list_of_values:
		#orderId = record[0]
		recordType = record[0]
		if recordType=="order":
			orderFields.extend(record)
			break

	#manage line_item records
	for record in list_of_values:		
		recordType = record[0]
		if recordType=="line_item":
			joinedRecord = []
			joinedRecord.extend(orderFields)
			joinedRecord.extend(record)
			mr.emit(joinedRecord)


if __name__ == '__main__':
	inputdata = open(sys.argv[1])
  	mr.execute(inputdata, mapper, reducer)
