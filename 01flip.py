# Program to find the subarray to flip 0's to 1's and 1's to 0's so that the final array has maximum number of 1's

def largest0(arr):
	start = 0
	maxstart = 0
	maxdiff01 = 0
	currdiff = 0
	for i in range(0,len(arr)):
		if arr[i] == 0:
			currdiff += 1
		else:
			currdiff -= 1
		if maxdiff01 < currdiff:
			maxdiff01 = currdiff
			maxstart = start
		if currdiff < 0:
			start  = i+1
			currdiff = 0
	print maxdiff01, maxstart


largest0([0,0,0,1,0,1,0,0,1,1,1,1,0,0,0,0])
