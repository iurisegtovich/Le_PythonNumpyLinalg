import numpy

def gs(X, row_vecs=True, norm = True):
	if not row_vecs:
		X = X.T
	Y = X[0:1,:].copy()
	for i in range(1, X.shape[0]):
		proj = numpy.diag((X[i,:].dot(Y.T)/numpy.linalg.norm(Y,axis=1)**2).flat).dot(Y)
		Y = numpy.vstack((Y, X[i,:] - proj.sum(0)))
	if norm:
		Y = numpy.diag(1/numpy.linalg.norm(Y,axis=1)).dot(Y)
	if row_vecs:
		return Y
	else:
		return Y.T
		
def gs(M):
	M = M.T
	N = M[0:1,:].copy() 
	lm = M.shape[0]
	for i in range(1, lm):
		proj = numpy.diag((M[i,:].dot(N.T)/numpy.linalg.norm(N,axis=1)**2).flat).dot(N)
		N = numpy.vstack((N, M[i,:] - proj.sum(0)))
	N = numpy.diag(1/numpy.linalg.norm(N,axis=1)).dot(N)
	return N.T

def gs_ext(M): #assumes M of independent columns
	Mt = M.T #transposes matrix M for convenience
	lN = Mt[0:1,:].copy() #slice of the matrix Mt corresponding to its first line  ( 0:1 ), all elements ( ,: )
	N = lN.copy() #initilize matriz M with the first sliced line
	nlM = Mt.shape[0] #number of lines of the matrix Mt
	for i in range(1, nlM): #for each line in M, from the second ( 1 ), to last, exclusively ( ,nlM )
		Nt=N.T #transposes said line
		li=Mt[i:i+1,:].copy() #slices line i
		n2N=numpy.linalg.norm(N,axis=1) #gets, on the diagonal element ii, the norm of the line i from N
		lidotNt=numpy.dot(li,Nt) #gets a column with, at line i, the dot product of the line i from li with the column i from NT -- line i from N
		projCoefs = lidotNt/n2N #element by element division divides each li[i].N[i] by N[i].N[i]
		diagProjCoefs=numpy.diag(projCoefs.flat) #makes a diagonal matri with projCoefs elements
		proj = numpy.dot(diagProjCoefs,N) #gets actual projections in each line i of proj by multiplying each proj coefficient in diagonal ii for the element in line i of each column of N
		sproj = proj.sum(0) #sums over dimension 0, creates a array , at index i have summation of all lines of colum i of proj -- that is the array that is the summation of all projected arrays
		orth = Mt[i,:] - sproj #subtracts each element j of line i of Mt with each element j of sproj -- therefore, from the line i of Mt subtracts all the projections, leaving the orthogonal complement array
		N = numpy.vstack( ( N, orth ) ) #stacks array back nito matrix structure
	n2N=numpy.linalg.norm(N,axis=1) #norm in diagonal elements
	diaginvnorms=numpy.diag(1./n2N) #element by element division
	N = numpy.dot(diaginvnorms,N) #each line of N is divided by its norm
#	numpy.dot(diaginvnorms,N)
#	N = numpy.diag(1/numpy.linalg.norm(N,axis=1)).dot(N)
	return N.T #return result in original transposition

H=numpy.zeros([3,3])
H[0,0]=1
H[0,1]=H[1,0]=numpy.sin(1.)-numpy.sin(0.)
H[0,2]=H[2,0]=-numpy.cos(1.)+numpy.cos(0.)
H[1,1]= 1./2.+(1./4.)*numpy.sin(2.) - (1./4.)*numpy.sin(0.)
H[1,2]=H[2,1]=(-1./2.)*(numpy.cos(1.)*numpy.cos(1.))-(-1./2.)*(numpy.cos(0.)*numpy.cos(0.))
H[2,2]= 1./2.-(1./4.)*numpy.sin(2.) + (1./4.)*numpy.sin(0.)


def gs_ext_hermit(M,H): #assumes M of independent columns, accepts an hermitian matrix, so that the dot product of vector a and b is the dot product sequence of line alpha . hermitian matrix . column beta of coeficients of both vectors in a common base
	Mt = M.T #transposes matrix M for convenience
	lN = Mt[0:1,:].copy() #slice of the matrix Mt corresponding to its first line  ( 0:1 ), all elements ( ,: )
	N = lN.copy() #initilize matriz M with the first sliced line
	nlM = Mt.shape[0] #number of lines of the matrix Mt
	for i in range(1, nlM): #for each line in M, from the second ( 1 ), to last, exclusively ( ,nlM )
		Nt=N.T #transposes said line
		li=Mt[i:i+1,:].copy() #slices line i
		n2N=numpy.dot(N,numpy.dot(H,Nt)) #gets, on the diagonal element ii, the norm of the line i from N
		n2N=numpy.diag(n2N)#extract diagonal
		lidotNt=numpy.dot(li,numpy.dot(H,Nt)) #gets a column with, at line i, the dot product of the line i from li with the column i from NT -- line i from N
		projCoefs = lidotNt/n2N #element by element division divides each li[i].N[i] by N[i].N[i]
		diagProjCoefs=numpy.diag(projCoefs.flat) #makes a diagonal matri with projCoefs elements
		proj = numpy.dot(diagProjCoefs,N) #gets actual projections in each line i of proj by multiplying each proj coefficient in diagonal ii for the element in line i of each column of N
		sproj = proj.sum(0) #sums over dimension 0, creates a array , at index i have summation of all lines of colum i of proj -- that is the array that is the summation of all projected arrays
		orth = Mt[i,:] - sproj #subtracts each element j of line i of Mt with each element j of sproj -- therefore, from the line i of Mt subtracts all the projections, leaving the orthogonal complement array
		N = numpy.vstack( ( N, orth ) ) #stacks array back nito matrix structure
	Nt=N.T
	n2N=numpy.dot(N,numpy.dot(H,Nt)) #gets, on the diagonal element ii, the norm of the line i from N
	n2N=numpy.sqrt(n2N) #sqrt element by element
	n2N=numpy.diag(n2N) #extract diagonal
	diaginvnorms=numpy.diag(1./n2N) #element by element division and diagonal matrix
	N = numpy.dot(diaginvnorms,N) #each line of N is divided by its sqrt norm
	return N.T #return result in original transposition

gs_ext_hermit(M,H)
array([[ 1.        , -0.64385175, -0.43321119],
       [ 0.        ,  0.76515026,  0.0226026 ],
       [ 0.        ,  0.        ,  0.90100898]])


(0.76515026)*(numpy.sin(1.)-numpy.sin(0.)) + (-0.64385175) = -7.1917819477462785e-09 ~ 0


NB=gs_ext_hermit(M,H)
numpy.dot(NB[:,0],numpy.dot(H,NB[:,0]))
numpy.dot(NB[:,0],numpy.dot(H,NB[:,1]))
numpy.dot(NB[:,0],numpy.dot(H,NB[:,2]))
numpy.dot(NB[:,1],numpy.dot(H,NB[:,0]))
numpy.dot(NB[:,1],numpy.dot(H,NB[:,1]))
numpy.dot(NB[:,1],numpy.dot(H,NB[:,2]))
numpy.dot(NB[:,2],numpy.dot(H,NB[:,0]))
numpy.dot(NB[:,2],numpy.dot(H,NB[:,1]))
numpy.dot(NB[:,2],numpy.dot(H,NB[:,2]))


>>> numpy.dot(NB[:,0],numpy.dot(H,NB[:,0]))
1.0
>>> numpy.dot(NB[:,0],numpy.dot(H,NB[:,1]))
0.0
>>> numpy.dot(NB[:,0],numpy.dot(H,NB[:,2]))
3.5527136788005009e-15
>>> numpy.dot(NB[:,1],numpy.dot(H,NB[:,0]))
0.0
>>> numpy.dot(NB[:,1],numpy.dot(H,NB[:,1]))
1.0000000000000027
>>> numpy.dot(NB[:,1],numpy.dot(H,NB[:,2]))
4.0592239970058735e-15
>>> numpy.dot(NB[:,2],numpy.dot(H,NB[:,0]))
1.7763568394002505e-15
>>> numpy.dot(NB[:,2],numpy.dot(H,NB[:,1]))
5.773159728050814e-15
>>> numpy.dot(NB[:,2],numpy.dot(H,NB[:,2]))
0.99999999999999312

