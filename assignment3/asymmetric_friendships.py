import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    pair = tuple(sorted(record))
    mr.emit_intermediate(pair, 1)

def reducer(pair, list_of_values):
    # key: word
    # value: list of occurrence counts
    if len(list_of_values) == 1:
    	mr.emit((pair[0], pair[1] ))
    	mr.emit((pair[1], pair[0] ))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
