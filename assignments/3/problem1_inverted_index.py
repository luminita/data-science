"""
Assignment 3, problem 1: Create an Inverted index. Given a set of documents, 
an inverted index is a dictionary where each word is associated with a list 
of the document identifiers in which that word appears.
"""
import sys

import MapReduce


# Part 1
mr = MapReduce.MapReduce()

# Part 2
def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]
    words = value.split()
    emitted_words = set({})
    for w in words:
        if not w in emitted_words:
            emitted_words = emitted_words.union([w])
            mr.emit_intermediate(w, key)

# Part 3
def reducer(key, list_of_values):
    # key: word
    # value: list of documents where this word occurs
    mr.emit((key, list_of_values))

# Part 4
inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
