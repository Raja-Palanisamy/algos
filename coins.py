
# Program to print the minimum no. of possible coins(1,3,5 cents) needed for a given value


def coins_recursive(num):
	if num<=0:
		return 0
	if num == 1 or num == 3 or num == 5:
		return 1
	x = float('Inf')
	y = float('Inf')
	if num>5:
		x = coins_recursive(num-5)+1
	if num>3:
		y = coins_recursive(num-3)+1
	z = coins_recursive(num-1)+1
	return min(x,y,z)

def coins_DP(num):
	coins = [float('Inf')] * (num+1)
	
	coins[1:6] = [1,2,1,2,1]
	for i in range(6,num+1):
		coins[i] = min(coins[i-1]+1,coins[i-3]+1,coins[i-5]+1)
	return coins[num]

print coins_DP(int(raw_input()))
