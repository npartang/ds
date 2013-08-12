import MapReduce
import sys
import json
# Part 1
mr = MapReduce.MapReduce()

# Part 2
def mapper(record):
	try:
    		# key: document identifier
    		# value: document contents
		#print len(record)
		key = record[1]
		#print key
		#print value
		mr.emit_intermediate(key, record)
	except KeyError:
		pass
# Part 3
def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    #get the order record
    for orderid in list_of_values:
	if orderid[0] == "order":
		finalorder = orderid
    for order_id in list_of_values:
    	result = []
	if order_id[0] == "line_item":
		for order in finalorder:
			result.append(order)
		for val in order_id:
			result.append(val)
		#print len(result)
    		mr.emit((result))

# Part 4
inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
