"""
Assignment 3, problem 2: Implement a relational join as a MapReduce query
Assume the tables are called order and line_item
"""
import sys

import MapReduce


# Part 1
mr = MapReduce.MapReduce()

# Part 2
def mapper(record):
    # record[0]: table name
    # record[1]: order id
    # record[2:]: other fields
    mr.emit_intermediate(record[1], record)

# Part 3
def reducer(key, list_of_values):
    # key: field on which the join is done
    # value: record (from one of the tables)
    order_records = [v for v in list_of_values if v[0] == 'order']
    line_item_records = [v for v in list_of_values if v[0] == 'line_item']

    for o in order_records:
        for l in line_item_records:
            mr.emit((o + l))

# Part 4
inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
