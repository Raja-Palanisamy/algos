import time
def sieve_for_primes_to(n):
    size = n//2
    sieve = [1]*size
    limit = int(n**0.5)
    for i in range(1,limit):
        if sieve[i]:
            val = 2*i+1
            tmp = ((size-1) - i)//val 
            sieve[i+val::val] = [0]*tmp
    return [2] + [i*2+1 for i, v in enumerate(sieve) if v and i>0]

def prime_nos(num):
	arr = [1] * (num)
	primes = []
	for i in range(2,int(num**0.5)):
		if arr[i-1] == 1:
			j = 2
			primes.append(i)
			arr[2*i-1::i] = [-1]*((num-2*i)/i+1)
	return primes

def check_prime(num):
	for i in range(2,num/2):
		if num%i == 0:
			return num,0
	return num,1

int1 = int(raw_input())
x = time.time()
y1 = prime_nos(int1)
print time.time()-x
x = time.time()
y2 = sieve_for_primes_to(int1)
print time.time()-x

#print check_prime(sum(prime_nos(int(raw_input()))))

