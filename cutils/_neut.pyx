import numpy as np
cimport numpy as np

np.import_array()

cdef extern from "neut.h":
     void neut(double* alpha, double* group, int size)

def neut_func(np.ndarray[double, ndim=1, mode="c"] in_array1 not None, np.ndarray[double, ndim=1, mode="c"] in_array2 not None):
    neut(<double*>np.PyArray_DATA(in_array1), <double*>np.PyArray_DATA(in_array2), in_array1.shape[0])
