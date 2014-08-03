"""
Assignment 3, problem 6: Assume you have two matrices A and B in a sparse matrix format, 
where each record is of the form i, j, value. Design a MapReduce algorithm to compute the 
matrix multiplication A x B
"""
import sys

import MapReduce


# Part 1
mr = MapReduce.MapReduce()

# Part 2
N = 5
M = 5
K = 5
def mapper(record):
    # record[0]: which matrix ('a' or 'b')
    # record[1]: the row number 
    # record[2]: the column number 
    # record[3]: value
    if record[0] == 'a':
        for k in range(K):
            mr.emit_intermediate((record[1], k), record)

    if record[0] == 'b':
        for k in range(N):
            mr.emit_intermediate((k, record[2]), record)

# Part 3
def reducer(key, list_of_values):
    val = 0
    a = {}
    b = {}
    for r in list_of_values:
        if r[0] == 'a':
            a[r[2]] = r[3]
        else:
            b[r[1]] = r[3]
    common = False
    for k, v in a.iteritems():
        if k in b:
            common = True
            val += v*b[k]
    
    if common:
        mr.emit((key[0], key[1], val))


# Part 4
inputdata = open(sys.argv[1])

mr.execute(inputdata, mapper, reducer)
