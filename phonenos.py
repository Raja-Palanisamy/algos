
def phoneprint(num,chrs,string,k):
	for i in list(chrs[num[k]]):
		string.append(i)
		if len(string) == len(num):
			print ''.join(string)
		else:
			phoneprint(num,chrs,string,k+1)
		string.pop()
	return

chrs = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz','0':'+','1':'1'}
phoneprint(raw_input(),chrs,[],0)
		
