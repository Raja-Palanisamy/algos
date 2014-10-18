
def prime_nos(num):
	arr = [1] * num
	primes = []
	for i in range(2,num):
		if arr[i-1] == 1:
			j = 2
			primes.append(i)
			while j*i<num:
				arr[j*i-1] = -1
				j += 1
	return primes


def check_prime(num):
	for i in range(2,num/2):
		if num%i == 0:
			return num,0
	return num,1


print check_prime(sum(prime_nos(int(raw_input()))))

