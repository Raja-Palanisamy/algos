
def possDecomp(compword,start, diction, output, finalout):
    if start == len(compword):
        finalout.append(''.join(output))
        return
    else:
	if len(output)>0:
        	output.append(' ')
        prefix = []
        for i in range(start,len(compword)):
            prefix.append(compword[i])
            if diction.has_key(''.join(prefix)):
                possDecomp(compword,i+1,diction,output+prefix,finalout)
        return

string = 'blackleatherjacket'
finalout = []
diction = {'black':1,'leather':1,'jacket':1,'leat':1,'her':1,'et':1,'jack':1}
possDecomp(list(string),0,diction,[],finalout)
print finalout
