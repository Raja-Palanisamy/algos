

def bin(x):
	t = ''
	while x != 0:
		if x & 1:
			t = '1' + t
		else:
			t = '0' + t
		x >>= 1
	t = '0b' + t
	return t

print bin(int(raw_input()))
