# Program to print sum of two binary numbers

def add(x,y,car):
	return [x^y^car, (x&y)|(y&car)|(x&car)]

def digits(x):
	return len(str(x))

def binarysum(num1,num2):

	i,j = 0,0
	result = []
	car = 0
	final = 0 
	n1 = int(num1)
	n2 = int(num2)
	while n1 != 0 or n2 != 0:
		if n2 == 0:
			if n1 == 0:
				break
			if car == 0:
				break
			else:
				n2 = car
				car = 0
		elif n1 ==0:
			if car == 0:
				break
			else:
				n1 = car
				car = 0
		
		x = n1 % 10
		y = n2 % 10
		[res,car] = add(x,y,car)
		result.append(res)
		n1 = n1/10
		n2 = n2/10

	if n1 != 0:
		result.append(n1)
	if n2 != 0:
		result.append(n2)
	if car != 0:
		result.append(car)
	for i in result[::-1]:
		final = 10*final + i
	print final, int('0b'+str(final),2)

binarysum(raw_input(),raw_input())
