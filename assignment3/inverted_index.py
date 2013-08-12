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
		key = record[0]
		value = record[1]
		#print key
		#print value
		words = value.split()
		for w in words:
			#print w
			mr.emit_intermediate(w, key)
	except KeyError:
		pass
# Part 3
def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    result = []
    for doc_id in list_of_values:
	if doc_id not in result:
		result.append(doc_id)
    mr.emit((key, result))

# Part 4
inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
