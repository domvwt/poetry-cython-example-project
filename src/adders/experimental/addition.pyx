"""Function for adding two numbers"""
from cython import boundscheck, wraparound


@boundscheck(False)
@wraparound(False)
cpdef int add(int a, int b):
    return a + b
