"""Function for adding two numbers"""
from cython import boundscheck, wraparound


@boundscheck(False)
@wraparound(False)
cpdef int add(int a, int b):
    return a + b

@boundscheck(False)
@wraparound(False)
cpdef int sum_list(list input_list):
    cdef int total = 0
    for value in input_list:
        total += value
    return total
