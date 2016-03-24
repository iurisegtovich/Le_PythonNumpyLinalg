#!/usr/bin/env python

#ref: http://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.linalg.eig.html

import numpy
from numpy import linalg

#(Almost) trivial example with real e-values and e-vectors.
M = numpy.diag((1, 2, 3))
w, v = linalg.eig(M)
w; v
#array([ 1.,  2.,  3.])
#array([[ 1.,  0.,  0.],
#       [ 0.,  1.,  0.],
#       [ 0.,  0.,  1.]])

#Real matrix possessing complex e-values and e-vectors; note that the e-values are complex conjugates of each other.
M=numpy.array([[1, -1], [1, 1]])
w, v = linalg.eig(M)
w; v
#array([ 1. + 1.j,  1. - 1.j])
#array([[ 0.70710678+0.j        ,  0.70710678+0.j        ],
#       [ 0.00000000-0.70710678j,  0.00000000+0.70710678j]])

#Complex-valued matrix with real e-values (but complex-valued e-vectors); note that a.conj().T = a, i.e., a is Hermitian.
M = numpy.array([[1, 1j], [-1j, 1]])
w, v = linalg.eig(M)
w; v
#array([  2.00000000e+00+0.j,   5.98651912e-36+0.j]) # i.e., {2, 0}
#array([[ 0.00000000+0.70710678j,  0.70710678+0.j        ],
#       [ 0.70710678+0.j        ,  0.00000000+0.70710678j]])
