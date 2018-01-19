import numpy as np
cimport numpy as np
from libcpp cimport bool
from libcpp.pair cimport pair

np.import_array()

cdef extern from "rank.h":
    int rank(double* x, int size)

def rank_func(np.ndarray[double, ndim=1, mode="c"] in_array1 not None):
    rank(<double*>np.PyArray_DATA(in_array1), in_array1.shape[0])
