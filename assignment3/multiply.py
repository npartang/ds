import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()
N=5
M=5


# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    #determine table
    table, row, column, value = record
    for n in range(0,5): 
      if table == "a":
        destCell = (row, n)
	serial = column
	tab = "L"
      if table == "b":
        destCell = (n, column)
        serial = row
        tab = "R"
      #print (destCell, (tab, serial, value))
      mr.emit_intermediate(destCell, (tab, serial, value))

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    leftArray = [ (item[1],item[2]) for item in list_of_values if item[0] == 'L' ]
    rightArray = [ (item[1],item[2]) for item in list_of_values if item[0] == 'R' ]
    total = 0
    for arr1 in leftArray:
      for arr2 in rightArray:
        if arr1[0] == arr2[0]:
          total += arr1[1]*arr2[1]
    key0 = str(key[0])
    key1 = str(key[1])
    print (key0+","+key1)
    mr.emit( (key[0], key[1],total) )
    #mr.emit((key,total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
