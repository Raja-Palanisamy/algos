

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

print subset_sum([3, 34, 4, 12, 5, 2],int(raw_input()))
