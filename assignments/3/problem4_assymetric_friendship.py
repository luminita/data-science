"""
Assignment 3, problem 4: The relationship "friend" is often symmetric, meaning that if I 
am your friend, you are my friend. Implement a MapReduce algorithm to check whether this 
property holds. Generate a list of all non-symmetric friend relationships.
"""
import sys

import MapReduce


# Part 1
mr = MapReduce.MapReduce()

# Part 2
def mapper(record):
    # record[0]: person A
    # record[1]: person B (friend of person A)
    
    mr.emit_intermediate(record[0], record[1])
    mr.emit_intermediate(record[1], record[0])

# Part 3
def reducer(key, list_of_values):

    is_assymetric = False
    for friend in set(list_of_values):
        if list_of_values.count(friend) == 1:
            is_assymetric = True
            break
        
    if is_assymetric:
        for friend in set(list_of_values):
            if list_of_values.count(friend) == 1:
                mr.emit((key, friend))


# Part 4
inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
