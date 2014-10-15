# Program to print the transpose of a matrix (1-d) given rows and columns
# Can also be used to separate the letters from numbers - look at the example below

def swap(x, y):
	(x,y) = (y,x)
def mat_trans(A,r,c):
	
	size = r*c -1
	flag = {}
	for i in range(1,size):
		flag[i] = 0
	flag[0] = 1
	flag[size] = 1
	i = 1
	while i < size:
		start = i
		t = A[i]
		nxt = (i*r)%size
		(t,A[nxt]) = (A[nxt],t)
		flag[i] = 1
		i = nxt
		while i != start:
			nxt = (i*r)%size
	                (t,A[nxt]) = (A[nxt],t)
        	        flag[i] = 1
                	i = nxt
		while i<size and flag[i] == 1:
			i += 1

A = list('a1b2c3d4e5f6g7h8i9j1k2l3m4')
r = 13
c = 2
mat_trans(A,r,c)
print ''.join(A)


