

def subset_sum(arr,sum):
	
	x = len(arr)
	mat = [[0]*(x+1) for i in range(0,sum+1)]
	mat[0] = [1]*(x+1)
	
	for i in range(1,sum+1):
		for j in range(1,x+1):
			mat[i][j] = mat[i][j-1]
			if i-arr[j-1] >= 0:
				mat[i][j] = mat[i][j] | mat[i-arr[j-1]][j-1]
	return mat[sum][x]

def subset_nos(Numbers,Maximum):

	Array = {}
	Array[0] = 1

	for CurrentNum in Numbers:
	    for Num in xrange(Maximum - CurrentNum, -1, -1):
        	if (Num in Array):
            		Array[Num + CurrentNum] = Array.get(Num + CurrentNum,0) + Array[Num]
	print Array.has_key(Maximum)

arr = [3,34,5,12,5,2,]
Num = int(raw_input())
print subset_sum(arr,Num)
subset_nos(arr,Num)
