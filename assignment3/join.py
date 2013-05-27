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
    table = record[0]
    order_id = record[1]
    mr.emit_intermediate(order_id, record)

def reducer(order_id, recs):
    # key: word
    # value: list of occurrence counts
    
    items = []
    orders = []

    for i in recs:
        if i[0] == 'line_item':
            items.append(i)
        if i[0] == 'order':
            orders.append(i) 
    
 #   res = []
    for i in orders:
         for j in items:
	     mr.emit(map(str,(i+j)))
#    mr.emit(res)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
