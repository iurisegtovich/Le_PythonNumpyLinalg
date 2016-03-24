import numpy
v1 = numpy.array([1,2]) #um array, uma estrutura unidimensional, não é equivalente a uma matriz linha nem a auma matriz coluna, as quais tem duas dimensões, contudo com 1 dimensão de tamanho igual a 1.
v2 = numpy.array([3,4]) #um array, uma estrutura unidimensional, não é equivalente a uma matriz linha nem a auma matriz coluna, as quais tem duas dimensões, contudo com 1 dimensão de tamanho igual a 1.

a1 = numpy.zeros((2)) #um array, uma estrutura unidimensional, não é equivalente a uma matriz linha nem a auma matriz coluna, as quais tem duas dimensões, contudo com 1 dimensão de tamanho igual a 1.
l1 = numpy.zeros((1, 2)) #allocate structure for a line matrix with 2 columns with zeros
c1 = numpy.zeros((2, 1)) #allocate structure for a column matrix with 2 lines with zeros

l1[0,:]=v1 #fill the line matrix with array values
c1[:,0]=v2 #fill the column matrix with array values
l1
#array([[ 1.,  2.]])
c1
#array([[ 3.],
#	   [ 4.]])
A = numpy.zeros((2, 2)) #allocate structure for a matrix with 2 lines and 2 columns using zeros
A[:,0]=l1 #fills first column of matrix A with values from the line matrix, the 
A
#array([[ 1.,  0.],
#	   [ 2.,  0.]])

M = numpy.zeros((2, 2)) #allocate structure for a matrix with 2 lines and 2 columns using zeros

#slicing:
A=numpy.zeros(6)
#full slice
A[:]=[0,1,2,3,4,5]
A[0] #element
A[1:] #slice from element 1 and on
A[0:2] #slice from element 0 up to element 2 excluding it
A[0:5:2] #slice from element 0, picknd every 2nd element up to element 5 excluding it
A[0] #scalar
A[0:1] #array of the same shape with only 1 element
#:slicing


M[:,0]=v1
M[:,1]=v2
MT=M.transpose()
M[:,:] # a matriz toda
M[0,:] # a primeira linha
M[:,0] # a primeira coluna

#structure initiation
l0 = numpy.zeros((1, 2))
c0 = numpy.zeros((2, 1))
M0 = numpy.zeros((2, 2))
#n1 = c0[:] #this binding(=) for unallocated anme n1 will act as a pointer
n1 = numpy.zeros((2, 1)) #this binding(=) for unallocated anme n1 will act as a automatic allocation with a cast
n2 = numpy.zeros((2, 1))
v1 = numpy.zeros((2, 1))
v2 = numpy.zeros((2, 1))
v3 = numpy.zeros((2, 1))
v4 = numpy.zeros((2, 1))
NB1 = numpy.zeros((2, 2))
B2 = numpy.zeros((2, 2))
B3 = numpy.zeros((2, 2))


#value insertion
n1[:,0]=[1,0]
n2[:,0]=[0,1]
v1[:,0]=[1,2]
v2[:,0]=[3,4]
v3[:,0]=[5,6]
v4[:,0]=[7,8]

NB1[:,0]=n1[:,0]
NB1[:,1]=n2[:,0]

B2[:,0]=v1[:,0]
B2[:,1]=v2[:,0]

B3[:,0]=v3[:,0]
B3[:,1]=v4[:,0]

B2
#array([[ 1.,  3.],
#	   [ 2.,  4.]])
B3
#array([[ 5.,  7.],
#	   [ 6.,  8.]])


#C = numpy.dot(A,B) <=> C[i,j]=summation_in_k(A[i,k]*B[k,j])
C = numpy.dot(B2,B3)
#( 1*5+3*6=5+18=23 ) ( );
#( ) ( )

D = numpy.dot(B3,B2)
#( 5*1+7*2=5+14=19 ) ( );
#( ) ( )


