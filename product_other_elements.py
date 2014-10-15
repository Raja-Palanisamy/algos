# Given an array of numbers, return array of products of all other numbers
# Time Complexity : O(n) ; Space: O(n)
a = [1,2,3]
output = [0]*len(a)
forw = [1]*len(a)

forw[0] = a[0]

for i in range(1,len(a)):
    forw[i] = forw[i-1]*a[i]

forw[-1] = a[-1]
output[-1] = forw[-2]

for i in range(1,len(a)-1):
    forw[len(a)-1-i] = forw[len(a)-i]*a[len(a)-1-i]
    output[len(a)-1-i] = forw[len(a)-i-2]*forw[len(a)-i]

output[0] = forw[1]

print output
