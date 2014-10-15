# Program to print a square root of a number

def binsearch(num, min, max):
	mid = min + (max-min)/2.0
	
	if mid*mid <= num + 0.00000001 and mid*mid >= num - 0.00000001:
		return "{0:.2f}".format(mid)
	if mid*mid < num:
		return binsearch(num,mid,max)
	if mid*mid > num:
		return binsearch(num,min,mid)

def sqrt(num):
	if num >= 4:
		return binsearch(num, float(1), float(num)/float(2))
	elif num > 1:
		return binsearch(num, float(1), float(num))
	elif num >= 0:
		return binsearch(num, float(0), float(1))
	else:
		return 'i'+str(sqrt(-num))

print sqrt(int(raw_input()))
