"""
Assignment 3, problem 5: Consider a set of key-value pairs where each key is sequence id and 
each value is a string of nucleotides, e.g., GCTTCCGAAATGCTCGAA....
Write a MapReduce query to remove the last 10 characters from each string of nucleotides, 
then remove any duplicates generated.
"""
import sys

import MapReduce


# Part 1
mr = MapReduce.MapReduce()

# Part 2
def mapper(record):
    # record[0]: sequence id 
    # record[1]: the sequence itself 
    mr.emit_intermediate(record[1][:-10], "")

# Part 3
def reducer(key, list_of_values):
    mr.emit(key)


# Part 4
inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
