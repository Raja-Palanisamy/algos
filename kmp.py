

def lps(pat):
	
	lps = [0] * len(pat)
	i = 1
	ln = 0
	while i < len(pat):
		if pat[i] == pat[ln]:
			ln += 1
			lps[i] = ln
			i += 1
		else:
			if ln != 0:
				ln = lps[ln-1]
			else:
				lps[i] = 0
				i += 1
	return lps


def kmp(pat,txt):
	lp = lps(pat)
	i = 0
	j = 0
	while i < len(txt):
		if txt[i] == pat[j]:
			i += 1
			j += 1
			if j == len(pat):
				return i-j+1
		else:
			if j != 0:
				j = lp[j-1]
			else:
				i += 1
	return 'String not found'

print kmp(raw_input(),raw_input())
