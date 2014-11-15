
# Program to print the number of possible paths in a phone keypad given N
# For more details refer http://www.geeksforgeeks.org/mobile-numeric-keypad-problem/

def keypad_util(N,strt,neigh):
	if N == 1:
		return 1
	count = 0
	neig = neigh[strt]
	cnt = []
	for i in neig:
		cnt.append(keypad_util(N-1,i,neigh))
	return sum(cnt)

def keypad(N):
	neigh = {0:[8,0],1:[2,4,1],2:[1,5,3,2],3:[2,6,3],4:[1,5,7,4],5:[4,2,6,8,5],6:[5,3,9,6],7:[4,8,7],8:[7,5,9,0,8],9:[8,6,9]}
	cnt = 0
	for i in range(0,10):
		cnt += keypad_util(N,i,neigh)
	return cnt

print keypad(int(raw_input()))
