

def chainMult_rec(mat,strt,end,mem):
	if mem.has_key((strt,end)):
		return mem[(strt,end)]
	if len(mat) <= 1 or strt>=end:
		return 0
	overal_min = float('Inf')
	for i in range(strt,end):
		num1 = chainMult_rec(mat,i+1,end,mem)
		num2 = chainMult_rec(mat,strt,i,mem)
		num3 = mat[strt][0]*mat[i][1]*mat[end][1]
		if overal_min > float(num1+num2+num3):
			overal_min = num1+num2+num3
	mem[(strt,end)] = overal_min
	return overal_min

def chainMult(mat):
	num = [0]
	mem = {}
	num = chainMult_rec(mat,0,len(mat)-1,mem)
	print mem
	print mat
	return num

mat = [(10,30),(30,5),(5,60),(60,2),(2,10),(10,45),(45,30)]
print chainMult(mat)
