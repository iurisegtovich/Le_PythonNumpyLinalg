#!/usr/bin/env python

#REF http://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.poly.html

import numpy
from numpy import linalg

M = numpy.diag((1, 2))

#det( 1 0   wi 0
#     0 2 - 0 wi ) = 0

#det( 1-wi 0
#     0 2-wi ) = 0

#(1-wi)*(2-wi) - (0)*(0) = 0

#(1)*w1^2 + (-3)*wi + (2) = 0

p0 = numpy.poly(numpy.matrix(M))

#>>> p0
#array([ 1., -3.,  2.])

M = numpy.diag((1, 2, 3))

p1 = numpy.poly(numpy.matrix(M))

M = numpy.array([[1, -1], [1, 1]])

p2 = numpy.poly(numpy.matrix(M))

M= numpy.array([[1, 1j], [-1j, 1]])

p3 = numpy.poly(numpy.matrix(M))
