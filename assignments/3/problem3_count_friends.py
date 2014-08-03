"""
Assignment 3, problem 3: Consider a simple social network dataset consisting of 
a set of key-value pairs (person, friend) representing a friend relationship 
between two people. Describe a MapReduce algorithm to count the number of friends 
for each person.
"""
import sys

import MapReduce


# Part 1
mr = MapReduce.MapReduce()

# Part 2
def mapper(record):
    # record[0]: name of person A
    # record[1]: name of person B (which is a friend of person A)
    mr.emit_intermediate(record[0], 1)

# Part 3
def reducer(key, list_of_values):
    # key: name of person A 
    # value: 1 
    nfriends = sum(list_of_values)
    mr.emit((key, nfriends))

# Part 4
inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
