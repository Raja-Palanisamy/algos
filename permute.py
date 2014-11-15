

def swap(string,i,j):
	(string[i],string[j]) = (string[j],string[i])

def permute(string,i=0):
	if i==len(string):
		print ''.join(string)
	for j in range(i,len(string)):
		if string[i] != string[j] or i==j:
			swap(string,i,j)
			permute(string,i+1)
			swap(string,i,j)

permute(list(raw_input('Enter the string to permute:\t')))
